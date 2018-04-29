from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'comm-group': {'task': 'manage comm-groups'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


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


class CommGroup(Resource):
    def get(self, group_id):
        return in_progress, 200

    def post(self, group_id):
        return in_progress, 200

    def delete(self, group_id):
        return in_progress, 200


class CommGroupByUser(Resource):
    def get(self, user_id):
        return in_progress, 200

