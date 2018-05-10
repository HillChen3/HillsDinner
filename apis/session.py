from flask_restplus import Resource, abort, reqparse, Namespace
from flask import request
from common import utils


api = Namespace('session', description='login, verify, logout etc')
in_progress = "Interface is still in progress"

APIS = {
    'session': {'task': 'register login logout etc'},
}

parser = reqparse.RequestParser()


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


@api.route('/<username>, <password>')
class Session(Resource):
    def get(self, username, password):
        return in_progress + " get", 200


@api.route('/<username>')
class Logout(Resource):
    def delete(self, username):
        return in_progress, 200