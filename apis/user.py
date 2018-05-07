from flask_restplus import Resource, abort, reqparse, fields, marshal_with, Namespace
from models.models import user_model, operation_model, group_model, group_user_verify_model
from common import utils

parser = reqparse.RequestParser()
api = Namespace('user', description='users operation')

in_progress = "Interface is still in progress"
APIS = {
    'user': {'task': 'manage users'}
}
user_model = api.model('UserModel', user_model)
operation_model = api.model('OperationModel', operation_model)
group_model = api.model('GroupModel', group_model)
group_user_verify_model = api.model('VerifyModel', group_user_verify_model)


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return in_progress, 200

    @api.doc(body=user_model)
    def put(self):
        parser.add_argument('phone_num', type=str, required=True)
        parser.add_argument('username', type=str, required=True, help='username test')
        args = parser.parse_args()
        print(args)
        # 需要检查电话号码格式
        if utils.check_phone_num(args['phone_num']):
            return in_progress, 200
        return "invalid phone num", 401


@api.route('/<user_id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, user_id):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        return in_progress, 200

    @api.doc(body=user_model)
    def post(self):
        return in_progress, 200

    def delete(self):
        return in_progress, 200


@api.route('/<user_id>/group')
class CommGroupByUser(Resource):
    @api.marshal_list_with(group_model)
    def get(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/verify')
class VerifyByUser(Resource):
    @api.marshal_list_with(group_user_verify_model)
    def get(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/verify/<verify_id>')
class VerifyByUser(Resource):
    @api.marshal_with(group_user_verify_model)
    def get(self, user_id, verify_id):
        return in_progress, 200

    def delete(self, user_id, verify_id):
        return in_progress, 200


@api.route('/<user_id>/operation')
class UserOperationGroup(Resource):
    @api.marshal_list_with(operation_model)
    def get(self, user_id):
        return in_progress, 200

    @api.expect(operation_model)
    def post(self, user_id):
        return in_progress, 200


