from flask_restplus import Resource, abort, reqparse, Namespace, fields
from flask import request
from common import utils

in_progress = "Interface is still in progress"
api = Namespace('group', description="group operation")

APIS = {
    'comm-group': {'task': 'manage comm-groups'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()


@api.route('/')
class CommGroupList(Resource):
    def get(self):
        return in_progress, 200

    def put(self):
        group_name = request.form['group_name']
        host_username = reqparse.form['host_name']
        phone_number = reqparse.form['phone']
        password = reqparse.form['password']
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_number):
            return in_progress, 200
        return "invalid phone num", 401


@api.route('/<group_id>')
class CommGroup(Resource):
    def get(self, group_id):
        return in_progress, 200

    def post(self, group_id):
        return in_progress, 200

    def delete(self, group_id):
        return in_progress, 200


@api.route('/<group_id>/user')
class GroupUserList(Resource):
    def get(self, group_id):
        return in_progress, 200

    def put(self, group_id):
        return in_progress, 200


@api.route('/<group_id>/user/<user_id>')
class GroupUser(Resource):
    def delete(self, user_id):
        group_id = reqparse.form['group_id']
        return in_progress, 200


@api.route('/<group_id>/news')
class GroupNewsList(Resource):
    def get(self, group_id):
        return in_progress, 200

    def put(self, group_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200


@api.route('/<group_id>/news/<news_id>')
class GroupNews(Resource):
    def get(self, news_id):
        return in_progress, 200

    def post(self, news_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200

    def delete(self, news_id):
        return in_progress, 200


group_verify_model = api.model('VerifyModel', {
    'username': fields.String(description="username", required=True),
    'content': fields.String(description="Why you wanna join", required=True)
})


@api.route('/<group_id>/verify')
class GroupUserVerifyList(Resource):
    def get(self, group_id):
        return in_progress, 200

    @api.expect(group_verify_model)
    def put(self, group_id):
        parser.add_argument('username', type=str)
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
    def get(self, group_id):
        return in_progress, 200


@api.route('/<group_id>/like')
class UsersWhoLikeGroup(Resource):
    def get(self, group_id):
        return in_progress, 200
