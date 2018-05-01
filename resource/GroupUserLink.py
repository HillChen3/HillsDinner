from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'group-user-link': {'task': 'follow, like, join, unfollow, unlike, leave'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class UserLinkList(Resource):
    def get(self, user_id):
        return in_progress, 200


class GroupUserLink(Resource):
    def get(self, user_id, group_id):
        return in_progress, 200

    def post(self, user_id, group_id):
        action_type = request.form['action_type']
        return in_progress, 200


