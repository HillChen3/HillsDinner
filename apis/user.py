from flask_restplus import Resource, abort, reqparse, fields, marshal_with, Namespace
from models.models import user_model, operation_model, group_model, group_user_verify_model
from common import utils

parser = reqparse.RequestParser()
api = Namespace('user', description='users operation')

in_progress = "Interface is still in progress"
APIS = {
    'user': {'task': 'manage users'}
}
user_model_reg = api.model('UserModel', user_model)
operation_model_reg = api.model('OperationModel', operation_model)
group_model_reg = api.model('GroupModel', group_model)
group_user_verify_model_reg = api.model('VerifyModel', group_user_verify_model)


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


def set_in_progress_model(args):
    for key, value in args.items():
        args[key] = in_progress
    return args


@api.route('/')
class UserList(Resource):
    @api.marshal_list_with(user_model_reg)
    def get(self):
        args = user_model
        args = set_in_progress_model(args)
        return args, 200

    @api.doc(body=user_model_reg)
    def post(self):
        for key, value in user_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        # 需要检查电话号码格式
        if utils.check_phone_num(args['phone_num']):
            return in_progress, 200
        return "invalid phone num", 401


@api.route('/<user_id>')
class User(Resource):
    @api.marshal_with(user_model_reg)
    def get(self, user_id):
        args = user_model
        args = set_in_progress_model(args)
        args['user_id'] = user_id
        return args, 200

    @api.doc(body=user_model_reg)
    def put(self, user_id):
        for key, value in user_model.items():
            parser.add_argument(key, type=str)
        args = parser.parse_args()
        args['user_id'] = user_id
        print(args)
        return in_progress, 200

    def delete(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/group')
class CommGroupByUser(Resource):
    @api.marshal_list_with(group_model_reg)
    def get(self, user_id):
        result = [group_model, group_model]
        return result, 200


@api.route('/<user_id>/verify')
class VerifyByUser(Resource):
    @api.marshal_list_with(group_user_verify_model_reg)
    def get(self, user_id):
        result = [group_user_verify_model, group_user_verify_model]
        return result, 200


@api.route('/<user_id>/operation')
class UserOperationList(Resource):
    @api.marshal_list_with(operation_model_reg)
    def get(self, user_id):
        return in_progress, 200

    @api.expect(operation_model)
    def delete(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/operation/<operation_id>')
class UserOperation(Resource):
    @api.marshal_list_with(operation_model_reg)
    def get(self, user_id):
        return in_progress, 200

    @api.expect(operation_model)
    def put(self, user_id):
        return in_progress, 200

    @api.expect(operation_model)
    def delete(self, user_id):
        return in_progress, 200


@api.route('/<user_id>/group/<group_id>/like')
class UserLikeGroup(Resource):
    @api.marshal_with(operation_model_reg)
    def get(self, user_id, group_id):
        return in_progress, 200


@api.route('/<user_id>/group/<group_id>/follow')
class UserFollowGroup(Resource):
    @api.marshal_with(operation_model_reg)
    def get(self, user_id, group_id):
        return in_progress, 200


