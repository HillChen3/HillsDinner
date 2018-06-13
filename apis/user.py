from flask_restplus import Resource, abort, reqparse, Namespace
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.models import operation_model, group_model, group_user_verify_model, user_model
from models.models import User, ActivityUserRelation
from common import utils, db_utils

parser = reqparse.RequestParser()
api = Namespace('user', description='users operation')

in_progress = "Interface is still in progress"
APIS = {
    'user': {'task': 'manage users'}
}
user_model_reg = api.model('UserModel', user_model)
# operation_model_reg = api.model('OperationModel', operation_model)
group_model_reg = api.model('GroupModel', group_model)


# group_user_verify_model_reg = api.model('VerifyModel', group_user_verify_model)


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


def set_in_progress_model(args):
    for key, value in args.items():
        args[key] = in_progress
    return args


@api.route('')
class UserList(Resource):
    @api.marshal_list_with(user_model_reg)
    def get(self):
        result = User.select()
        if not result:
            return 'no content', 204
        response = [model_to_dict(user, recurse=True) for user in result]
        # print(response)
        return response, 200

    @api.doc(body=user_model_reg)
    def post(self):
        for key, value in user_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        # 需要检查电话号码格式
        if not utils.check_phone_num(args['phone_num']):
            return "invalid phone num", 422
        args.pop('id', None)
        User.create(**args)
        return 'success', 200


@api.route('/<user_id>')
class SingleUser(Resource):
    @api.marshal_with(user_model_reg)
    def get(self, user_id):
        single_user = User.get_or_none(User.id == user_id)
        if single_user:
            response = model_to_dict(single_user)
            print(response)
            return response, 200
        return "no content", 204

    @api.doc(body=user_model_reg)
    def put(self, user_id):
        print('get ', SingleUser.get(self, user_id))
        if SingleUser.get(self, user_id)[1] == 204:
            return "can not found this user_id", 422
        for key, value in user_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)

        # 需要检查电话号码格式
        if not utils.check_phone_num(args['phone_num']):
            return "invalid phone num", 422
        update_user = dict_to_model(User, args)
        update_user.id = user_id
        update_user.save()

        return 'success', 200

    def delete(self, user_id):
        delete_user = User.get_or_none(User.id == user_id)
        if not delete_user:
            return "can not found this user_id", 204
        delete_user.delete_instance()
        return 'success', 200


@api.route('/<user_id>/group')
class CommGroupByUser(Resource):
    @api.marshal_list_with(group_model_reg)
    def get(self, user_id):
        user = User.get_or_none(User.id == user_id)
        if not user or not user.groups:
            return "can't find this user or user don't own any group", 204
        result = [group for group in user.groups]
        return result, 200


@api.route('/<user_id>/activities')
class CommActivityByUser(Resource):
    @api.marshal_list_with(group_model_reg)
    def get(self, user_id):
        user = User.get_or_none(User.id == user_id)
        activity_user_relation = ActivityUserRelation.select().where(ActivityUserRelation.user == user)
        response = [relation.user for relation in activity_user_relation]
        print(response)
        return response


# @api.route('/<user_id>/group/<group_id>/like')
# class UserLikeGroup(Resource):
#     @api.marshal_with(operation_model_reg)
#     def get(self, user_id, group_id):
#         return in_progress, 200
#
#
# @api.route('/<user_id>/group/<group_id>/follow')
# class UserFollowGroup(Resource):
#     @api.marshal_with(operation_model_reg)
#     def get(self, user_id, group_id):
#         return in_progress, 200
