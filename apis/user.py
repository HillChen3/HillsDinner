from flask_restplus import Resource, abort, reqparse, Namespace
from models.models import user_model, operation_model, group_model, group_user_verify_model
from common import utils, db_utils

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

query_user = 'SELECT id, username, nickname, avatar, gender, ' \
                     'phone_num, job, wechat_id, constellation, pet_plant, ' \
                     'hobbies, fav_event_type, self_intro FROM users'

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
        result = db_utils.query(query_user)
        if not result:
            return 'no content', 204
        response = db_utils.set_response_data(values=result, model=user_model)
        print(response)
        return response, 200

    @api.doc(body=user_model_reg)
    def post(self):
        add_user = ('INSERT INTO users '
                    '(username, nickname, avatar, gender, '
                    'phone_num, job, wechat_id, constellation, pet_plant, '
                    'hobbies, fav_event_type, self_intro ) values ('
                    '"{}", "{}", "{}", {}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")')

        for key, value in user_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        # for item in args:
        #     add_user += '"' + item + '", '
        add_user = add_user.format(
            args['username'], args['nickname'], args['avatar'], args['gender'],
            args['phone_num'], args['job'], args['wechat_id'], args['constellation'], args['pet_plant'],
            args['hobbies'], args['fav_event_type'], args['self_intro'])
        # 需要检查电话号码格式
        if utils.check_phone_num(args['phone_num']):
            db_utils.no_query(add_user)
            return 'success', 200

        return "invalid phone num", 422


@api.route('/<user_id>')
class User(Resource):
    @api.marshal_with(user_model_reg)
    def get(self, user_id):
        query_single_user = query_user + "WHERE id = {}".format(user_id)
        result = db_utils.query(query_single_user)
        if result:
            response = db_utils.make_dict_by_model(value=result[0], model=user_model)
            print(response)
            return response, 200
        return "no content", 204

    @api.doc(body=user_model_reg)
    def put(self, user_id):
        print('get ', User.get(self, user_id))
        if User.get(self, user_id)[1] == 204:
            return "can not found this user_id", 204
        update_user = ('UPDATE users '
                       'SET username = "{}", nickname = "{}", avatar = "{}", gender = {} '
                       'WHERE id = {}')

        for key, value in user_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        update_user = update_user.format(
            args['username'], args['nickname'], args['avatar'], args['gender'],
            args['phone_num'], args['job'], args['wechat_id'], args['constellation'], args['pet_plant'],
            args['hobbies'], args['fav_event_type'], args['self_intro'],
            user_id)
        # 需要检查电话号码格式
        if utils.check_phone_num(args['phone_num']):
            db_utils.no_query(update_user)
            return 'success', 200

        return "invalid phone num", 422

    def delete(self, user_id):
        delete_user = 'DELETE FROM users where id = {}'.format(user_id)
        db_utils.no_query(delete_user)
        return 'success', 200


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
