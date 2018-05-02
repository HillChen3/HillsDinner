from flask_restplus import Resource, abort, reqparse, fields, marshal_with, Namespace
from flask import request, Flask
from common import utils

api = Namespace('user', description='users operation')

in_progress = "Interface is still in progress"
APIS = {
    'user': {'task': 'manage users'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


@api.route('/')
class UserList(Resource):
    def get(self):
        return in_progress, 200


@api.route('/<user_id>')
class User(Resource):
    def get(self, user_id):
        args = parser.parse_args()
        return in_progress, 200

    def put(self, **kwargs):
        username = request.form['username']
        email = reqparse.form['email']
        phone_number = reqparse.form['phone']
        password = reqparse.form['password']
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_number):
            return in_progress, 200
        return "invalid phone num", 401

    def post(self):
        return in_progress, 200

    def delete(self):
        return in_progress, 200


@api.route('/<user_id>/group')
class CommGroupByUser(Resource):
    def get(self, user_id):
        return in_progress, 200