from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'session': {'task': 'register login logout etc'},
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Session(Resource):
    def put(self):
        return in_progress, 200

    def get(self):
        return in_progress + " get", 200

    def post(self):
        return in_progress, 200

    def delete(self):
        return in_progress, 200