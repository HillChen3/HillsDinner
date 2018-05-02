from flask_restplus import Resource, abort, reqparse, fields, marshal_with, Namespace
from flask import request, Flask
from common import utils

api = Namespace('user', description='users operation')

in_progress = "Interface is still in progress"
APIS = {
    'user': {'task': 'manage users'}
}
parser = reqparse.RequestParser()


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


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


@api.route('/<user_id>/verify')
class VerifyByUser(Resource):
    def get(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/verify/<verify_id>')
class VerifyByUser(Resource):
    def get(self, user_id, verify_id):
        return in_progress, 200

    def  delete(self, user_id, verify_id):
        return in_progress, 200


OperationModel = api.model('OperationModel', {
    'group_id': fields.String(description="group_id", required=True),
    'type': fields.String(description="1 = follow, 2 = like", required=True)
})


@api.route('/<user_id>/operation')
class UserOperationGroup(Resource):
    def get(self, user_id):
        return in_progress, 200

    @api.expect(OperationModel)
    def post(self, user_id):
        return in_progress, 200


