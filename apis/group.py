from flask_restplus import Resource, abort, reqparse, Namespace, fields
from models.models import group_model, operation_model, group_user_verify_model, user_model, activity_info_model, \
    ActivityInfo
from models.models import group_model, operation_model, group_user_verify_model, user_model, group_news_model
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.models import Group, User, GroupUserRelation, GroupNews

in_progress = "Interface is still in progress"
api = Namespace('group', description="group operation")

user_model = api.model('UserModel', user_model)
operation_model = api.model('OperationModel', operation_model)
group_model = api.model('GroupModel', group_model)
group_user_verify_model = api.model('VerifyModel', group_user_verify_model)
group_news_model = api.model('GroupNewsModel', group_news_model)
APIS = {
    'comm-group': {'task': 'manage comm-groups'}
}


def check_owner(args):
    if not args['owner']:
        return "owner mustn't be none"
    owner = User.get_or_none(User.id == args['owner'])
    if not owner:
        return 'owner not found'
    return owner


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()


@api.route('/')
class GroupList(Resource):
    @api.marshal_list_with(group_model)
    def get(self):
        result = Group.select()
        if not result:
            return 'no content', 204
        response = [model_to_dict(group, recurse=True) for group in result]
        print(response)
        return response, 200

    @api.doc(body=group_model)
    def post(self):
        for key, value in group_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        owner = check_owner(args)
        if isinstance(owner, str):
            return owner, 422
        args['is_verify_need'] = args['is_verify_need'] == 'True'
        args['owner'] = owner
        args.pop('id', None)
        print(args)
        group = Group.create(**args)
        return 'Group id {} created'.format(group.id), 200


@api.route('/<group_id>')
class SingleGroup(Resource):
    @api.marshal_with(group_model)
    def get(self, group_id):
        query_single_group = Group.get_or_none(Group.id == group_id)
        if not query_single_group:
            return 'no content', 204
        response = model_to_dict(query_single_group)
        print(response)
        return response, 200

    @api.doc(body=group_model)
    def put(self, group_id):
        print('get ', SingleGroup.get(self, group_id))
        if SingleGroup.get(self, group_id)[1] == 204:
            return "can not found this group_id", 204

        for key, value in group_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        print(args)
        owner = check_owner(args)
        if isinstance(owner, str):
            return owner, 422
        args['is_verify_need'] = args['is_verify_need'] == 'True'
        update_group = dict_to_model(Group, args)
        update_group.id = group_id
        update_group.save()

        return 'success', 200

    def delete(self, group_id):
        delete_group = Group.get_or_none(Group.id == group_id)
        if not delete_group:
            return "can not found this group_id", 204
        delete_group.delete_instance()
        return 'success', 200


@api.route('/<group_id>/owner')
class GroupUserList(Resource):
    @api.marshal_with(user_model)
    def get(self, group_id):
        group = Group.get_or_none(Group.id == group_id)
        if not group:
            return "Can't find this group", 204
        return group.owner, 200

    # @api.doc(body=user_model)
    # def post(self, group_id):
    #     return in_progress, 200


@api.route('/<group_id>/user')
class GroupUserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self, group_id):
        group = Group.get_or_none(Group.id == group_id)
        print(model_to_dict(group))
        if not group:
            return 'group not found', 204
        group_user_relations = GroupUserRelation.select().where(
            GroupUserRelation.group == group, GroupUserRelation.action == 1)
        return [group.owner] + [relation.user for relation in group_user_relations], 200


@api.route('/<group_id>/user/<user_id>')
class GroupUser(Resource):
    def put(self, group_id):
        parser.add_argument('id', type=str, required=True)
        args = parser.parse_args()
        user = User.get_or_none(User.id == args['id'])
        if not user:
            return 'user not found', 204
        group = Group.get_or_none(Group.id == group_id)
        if not group:
            return 'group not found', 204

        GroupUserRelation.create(user=user, group=group, action=1)
        return 'success', 200

    def delete(self, group_id, user_id):
        group = Group.get_or_none(Group.id == group_id)
        user = User.get_or_none(User.id == user_id)
        if not group or not user:
            return 'group or user not found', 204
        relation = GroupUserRelation.get_or_none(GroupUserRelation.group == group, GroupUserRelation.user == user,
                                                 GroupUserRelation.action == 1)
        if not relation:
            return "user didn't join this group", 204
        relation.delete_instance()
        return 'success', 200


@api.route('/<group_id>/activity')
class GroupActivityList(Resource):
    # @api.marshal_list_with(activity_info_model)
    def get(self, group_id):
        group = Group.get_or_none(Group.id == group_id)
        print(group)
        # print(model_to_dict(group))
        if not group:
            print("group not found")
            return 'group not found', 204
        query_single_activity = ActivityInfo.get_or_none(ActivityInfo.group == group_id)
        if not query_single_activity:
            return 'no content', 204
            print("no content")
        response = model_to_dict(query_single_activity)
        print(response)
        return response, 200


# @api.route('/<group_id>/news')
# class GroupNewsList(Resource):
#     def get(self, group_id):
#         return in_progress, 200
#
#     def post(self, group_id):
#         title = reqparse.form['title']
#         context = reqparse.form['context']
#         return in_progress, 200
#
#
# @api.route('/<group_id>/news/<news_id>')
# class GroupNews(Resource):
#     def get(self, news_id):
#         return in_progress, 200
#
#     def put(self, news_id):
#         title = reqparse.form['title']
#         context = reqparse.form['context']
#         return in_progress, 200
#
#     def delete(self, news_id):
#         return in_progress, 200

@api.route('/<group_id>/news')
class GroupNewsList(Resource):
    @api.marshal_list_with(group_news_model)
    def get(self, group_id):
        group = Group.get_or_none(Group.id == group_id)
        if not group:
            return 'group not find', 204

        return [news for news in group.news], 200

    @api.doc(body=group_news_model)
    def post(self, group_id):
        group = Group.get_or_none(Group.id == group_id)
        if not group:
            return 'group not find', 204
        for key, value in group_news_model.items():
            parser.add_argument(key, type=str, required=True)
        args = parser.parse_args()
        args['owner'] = group
        if not args['create_time']:
            args.pop('create_time', None)
        GroupNews.create(**args)
        return 'success', 200



#
#
# @api.route('/<group_id>/verify')
# class GroupUserVerifyList(Resource):
#     @api.marshal_list_with(group_user_verify_model)
#     def get(self, group_id):
#         return in_progress, 200
#
#     @api.expect(group_user_verify_model)
#     def post(self, group_id):
#         parser.add_argument('username', type=str)
#         parser.add_argument('group_name', type=str)
#         parser.add_argument('content', type=str)
#         args = parser.parse_args()
#         print(args, group_id)
#         return in_progress, 200
#
#
# @api.route('/<group_id>/follow/count')
# class GroupFollowCount(Resource):
#     def get(self, group_id):
#         return 0, 200
#
#
# @api.route('/<group_id>/like/count')
# class GroupLikeCount(Resource):
#     def get(self, group_id):
#         return 0, 200
#
#
# @api.route('/<group_id>/follow')
# class UsersWhoFollowGroup(Resource):
#     @api.marshal_list_with(operation_model)
#     def get(self, group_id):
#         return in_progress, 200
#
#
# @api.route('/<group_id>/like')
# class UsersWhoLikeGroup(Resource):
#     @api.marshal_list_with(operation_model)
#     def get(self, group_id):
#         return in_progress, 200
