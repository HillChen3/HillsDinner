from flask_restplus import Resource, abort, reqparse
from flask import request

in_progress = "Interface is still in progress"

APIS = {
    'group_user_verify': {'task': 'verify user who wanna join group'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Group_User_Verify(Resource):
    def get(self, verify_id):
        return in_progress, 200

    def put(self, verify_id):
        message = reqparse.form['message']
        # 需要检查电话号码格式
        return in_progress, 200

    def post(self, verify_id):
        message = reqparse.form['message']
        return in_progress, 200

class Group_User_Verify_List(Resource):
    def get(self, group_id):
        return in_progress, 200


