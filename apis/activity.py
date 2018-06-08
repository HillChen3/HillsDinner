from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import activity_info_model
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.models import Group, ActivityInfo

in_progress = "Interface is still in progress"
api = Namespace('activity', description="activity operation")
activity_model_reg = api.model('ActivityModel', activity_info_model)
parser = reqparse.RequestParser()


def check_group_owner(args):
    if not args['group_owner']:
        return "group_owner must not be none"


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

    def post(self):
        for key, value in activity_info_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        owner = check_group_owner(args)
        if isinstance(owner, str):
            return owner, 422
        args['is_verify_need'] = args['is_verify_need'] == 'True'
        args['owner'] = owner
        args.pop('id', None)
        print(args)
        activity = ActivityInfo.create(**args)
        return 'Activity id {} created'.format(activity.id), 200
