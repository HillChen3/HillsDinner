from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import group_model, user_model, operation_model, group_user_verify_model
from common import db_utils

in_progress = "Interface is still in progress"
api = Namespace('group', description="group operation")

user_model = api.model('UserModel', user_model)
operation_model = api.model('OperationModel', operation_model)
group_model = api.model('GroupModel', group_model)
group_user_verify_model = api.model('VerifyModel', group_user_verify_model)
APIS = {
    'comm-group': {'task': 'manage comm-groups'}
}
query_group = ('SELECT id, group_name, group_topic, build_time, event_location, '
               'group_QRCode, is_verify_need, join_question, group_desc '
               'FROM comm_groups')


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()


@api.route('/')
class GroupList(Resource):
    @api.marshal_list_with(group_model)
    def get(self):
        result = db_utils.query(query_group)
        if not result:
            return 'no content', 204
        response = db_utils.set_response_data(values=result, model=group_model)
        print(response)
        return response, 200

    @api.doc(body=group_model)
    def post(self):
        add_group = ('INSERT INTO comm_groups '
                     '(group_name, group_topic, build_time, event_location, '
                     'group_QRCode, is_verify_need, join_question, group_desc)'
                     ' values ('
                     '"{}", "{}", "{}", "{}", "{}", {}, "{}", "{}")')

        for key, value in group_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        # for item in args:
        #     add_user += '"' + item + '", '
        add_group = add_group.format(
            args['group_name'], args['group_topic'], args['build_time'], args['event_location'],
            args['group_QRCode'], args['is_verify_need'], args['join_question'], args['group_desc'])
        db_utils.no_query(add_group)
        return 'success', 200


@api.route('/<group_id>')
class Group(Resource):
    @api.marshal_with(group_model)
    def get(self, group_id):
        query_single_group = query_group + ' WHERE id = {}'.format(group_id)
        result = db_utils.query(query_single_group)
        if not result:
            return 'no content', 204
        response = db_utils.make_dict_by_model(value=result[0], model=group_model)
        print(response)
        return response, 200

    @api.doc(body=group_model)
    def put(self, group_id):
        print('get ', Group.get(self, group_id))
        if Group.get(self, group_id)[1] == 204:
            return "can not found this group_id", 204
        update_group = ('UPDATE comm_groups '
                        'SET group_name = "{}", group_topic = "{}", build_time = "{}", event_location = "{}", '
                        'group_QRCode = "{}", is_verify_need = {}, join_question = "{}", group_desc = "{}" '
                        'WHERE id = {}')

        for key, value in group_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        update_group = update_group.format(
            args['group_name'], args['group_topic'], args['build_time'], args['event_location'],
            args['group_QRCode'], args['is_verify_need'], args['join_question'], args['group_desc'],
            group_id)
        db_utils.no_query(update_group)
        return 'success', 200

    def delete(self, group_id):
        delete_group = 'DELETE FROM comm_groups where id = {}'.format(group_id)
        db_utils.no_query(delete_group)
        return 'success', 200


@api.route('/<group_id>/user')
class GroupUserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self, group_id):
        return in_progress, 200

    @api.doc(body=user_model)
    def post(self, group_id):
        return in_progress, 200


@api.route('/<group_id>/user/<user_id>')
class GroupUser(Resource):
    def delete(self, group_id, user_id):
        group_id = reqparse.form['group_id']
        return in_progress, 200


@api.route('/<group_id>/news')
class GroupNewsList(Resource):
    def get(self, group_id):
        return in_progress, 200

    def post(self, group_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200


@api.route('/<group_id>/news/<news_id>')
class GroupNews(Resource):
    def get(self, news_id):
        return in_progress, 200

    def put(self, news_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200

    def delete(self, news_id):
        return in_progress, 200


@api.route('/<group_id>/verify')
class GroupUserVerifyList(Resource):
    @api.marshal_list_with(group_user_verify_model)
    def get(self, group_id):
        return in_progress, 200

    @api.expect(group_user_verify_model)
    def post(self, group_id):
        parser.add_argument('username', type=str)
        parser.add_argument('group_name', type=str)
        parser.add_argument('content', type=str)
        args = parser.parse_args()
        print(args, group_id)
        return in_progress, 200


@api.route('/<group_id>/follow/count')
class GroupFollowCount(Resource):
    def get(self, group_id):
        return 0, 200


@api.route('/<group_id>/like/count')
class GroupLikeCount(Resource):
    def get(self, group_id):
        return 0, 200


@api.route('/<group_id>/follow')
class UsersWhoFollowGroup(Resource):
    @api.marshal_list_with(operation_model)
    def get(self, group_id):
        return in_progress, 200


@api.route('/<group_id>/like')
class UsersWhoLikeGroup(Resource):
    @api.marshal_list_with(operation_model)
    def get(self, group_id):
        return in_progress, 200
