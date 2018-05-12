from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import group_model, user_model, operation_model, group_user_verify_model
from common import utils

in_progress = "Interface is still in progress"
api = Namespace('group', description="group operation")

user_model = api.model('UserModel', user_model)
operation_model = api.model('OperationModel', operation_model)
group_model = api.model('GroupModel', group_model)
group_user_verify_model = api.model('VerifyModel', group_user_verify_model)
APIS = {
    'comm-group': {'task': 'manage comm-groups'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()


@api.route('/')
class GroupList(Resource):
    @api.marshal_list_with(group_model)
    def get(self):
        return in_progress, 200

    @api.doc(body=group_model)
    def post(self):
        phone_number = 18688888888
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_number):
            return in_progress, 200
        return "invalid phone num", 401


@api.route('/<group_id>')
class Group(Resource):
    @api.marshal_with(group_model)
    def get(self, group_id):
        return in_progress, 200

    @api.doc(body=group_model)
    def put(self, group_id):
        return in_progress, 200

    def delete(self, group_id):
        return in_progress, 200


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
