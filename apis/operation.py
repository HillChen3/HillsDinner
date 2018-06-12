from flask_restplus import Resource, abort, reqparse, Namespace
from models.models import operation_model
from models.models import User, Group, GroupUserRelation
from playhouse.shortcuts import model_to_dict, dict_to_model

api = Namespace('operation', description="like, follow, unlike, unfollow etc")
operation_model = api.model('OperationModel', operation_model)
in_progress = "Interface is still in progress"

APIS = {
    'group-user-link': {'task': 'follow, like, join, unfollow, unlike, leave'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()


@api.route('/')
class GroupUserOperation(Resource):
    error_message = None
    user = None
    group = None
    action = None

    def get_params(self):
        parser.add_argument('user_id', type=str)
        parser.add_argument('action', type=str)
        parser.add_argument('group_id', type=str)

        args = parser.parse_args()
        print(args)
        if args['action']:
            self.action = args['action']
            if not '1' <= args['action'] <= '4':
                self.error_message = 'type can only be 1 - 4'
                return
        if args['user_id']:
            self.user = User.get_or_none(User.id == args['user_id'])
            print(model_to_dict(self.user))
            if not self.user:
                self.error_message = 'user not found'
                return
        if args['group_id']:
            self.group = Group.get_or_none(Group.id == args['group_id'])
            if not self.group:
                self.error_message = 'group not found'
                return
        return args

    def check_user_and_group(self, args):
        if not args['user_id']:
            self.error_message = 'user_id is required'
        if not args['group_id']:
            self.error_message = 'group_id is required'

    def get_relations(self, group=None, user=None, action=None):
        relations = None
        print(group, user, action)
        if not group and not user:
            relations = GroupUserRelation.select()
        elif group and user:
            relations = GroupUserRelation.select().where(GroupUserRelation.group == group,
                                                         GroupUserRelation.user == user)
        elif group:
            relations = GroupUserRelation.select().where(GroupUserRelation.group == group)
        elif user:
            relations = GroupUserRelation.select().where(GroupUserRelation.user == user)

        if action:
            result = relations.where(GroupUserRelation.action == action)
        else:
            result = relations
        print(([relation for relation in result]))
        return result

    @api.expect(operation_model)
    def post(self):
        args = self.get_params()
        self.check_user_and_group(args)
        if self.error_message:
            return self.error_message, 422
        user = User.get_or_none(User.id == args['user_id'])
        if not user:
            return 'user not found', 204
        group = Group.get_or_none(Group.id == args['group_id'])
        if not group:
            return 'group not found', 204
        GroupUserRelation.create(user=user, group=group, action=args['action'])
        return 'success', 200

    @api.expect(operation_model)
    def delete(self):
        args = self.get_params()
        self.check_user_and_group(args)
        if self.error_message:
            return self.error_message, 422
        group = Group.get_or_none(Group.id == args['group_id'])
        user = User.get_or_none(User.id == args['user_id'])
        if not group or not user:
            return 'group or user not found', 204
        relation = GroupUserRelation.get_or_none(GroupUserRelation.group == group, GroupUserRelation.user == user,
                                                 GroupUserRelation.action == args['action'])
        if not relation:
            return "user didn't do this operation to the group", 204
        relation.delete_instance()
        return 'success', 200

    @api.marshal_list_with(operation_model)
    @api.doc(params={'user_id': 'User id', 'group_id': 'Group id', 'action': 'action type'})
    def get(self):
        self.get_params()
        if self.error_message:
            return self.error_message, 422
        relations = self.get_relations(self.group, self.user, self.action)

        if not relations:
            return "user didn't do this operation to the group", 204
        result = []
        for relation in relations:
            relation = model_to_dict(relation)
            relation['user_id'] = relation['user']['id']
            relation['group_id'] = relation['group']['id']
            result.append(relation)
        return result, 200
