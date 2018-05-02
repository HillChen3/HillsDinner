from flask_restplus import Resource, abort, reqparse, Namespace
from flask import request
from common import utils

api = Namespace('GroupNews', description="event or new in group")
in_progress = "Interface is still in progress"

APIS = {
    'group-news': {'task': 'the event or message published by group'}
}
parser = reqparse.RequestParser()


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


