from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import activity_info_model
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.models import Group, ActivityInfo

in_progress = "Interface is still in progress"
api = Namespace('activity', description="activity operation")
activity_info_model = api.model('ActivityModel', activity_info_model)

activity_model_reg = api.model('ActivityModel', activity_info_model)
parser = reqparse.RequestParser()


def check_group(args):
    if not args['group']:
        return "group must not be none"
    group = Group.get_or_none(Group.id == args["group"])
    if not group:
        return "group not found"
    else:
        return group


@api.route('/')
class ActivityList(Resource):
    @api.marshal_list_with(activity_info_model)
    def get(self):
        result = ActivityInfo.select()
        if not result:
            return 'no content', 204
        response = [model_to_dict(activity, recurse=True) for activity in result]
        print(response)
        return response, 200

    @api.doc(body=activity_info_model)
    def post(self):
        for key, value in activity_info_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        group = check_group(args)
        if isinstance(group, str):
            return group, 422
        args['group'] = group
        args.pop('id', None)
        print(args)

        activity = ActivityInfo.create(**args)
        return 'Activity id {} created'.format(activity.id), 200


@api.route('/<activity_id>')
class SingleGroup(Resource):
    @api.marshal_with(activity_info_model)
    def get(self, activity_id):
        query_single_activity = ActivityInfo.get_or_none(ActivityInfo.id == activity_id)
        if not query_single_activity:
            return 'no content', 204
        response = model_to_dict(query_single_activity)
        print(response)
        return response, 200

    @api.doc(body=activity_info_model)
    def put(self, activity_id):
        print('get ', SingleGroup.get(self, activity_id))
        if SingleGroup.get(self, activity_id)[1] == 204:
            return "can not found this group_id", 204

        for key, value in activity_info_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        group = check_group(args)
        if isinstance(group, str):
            return group, 422
        update_activity = dict_to_model(ActivityInfo, args)
        update_activity.id = activity_id
        update_activity.save()

        return 'success', 200

    def delete(self, activity_id):
        delete_activity = ActivityInfo.get_or_none(ActivityInfo.id == activity_id)
        if not delete_activity:
            return "can not found this group_id", 204
        delete_activity.delete_instance()
        return 'success', 200
