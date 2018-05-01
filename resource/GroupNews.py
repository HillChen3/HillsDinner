from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'group-news': {'task': 'the event or message published by group'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class GroupNewsList(Resource):
    def get(self, group_id):
        return in_progress, 200

    def put(self, group_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200


class GroupNews(Resource):
    def get(self, news_id):
        return in_progress, 200

    def post(self, news_id):
        title = reqparse.form['title']
        context = reqparse.form['context']
        return in_progress, 200

    def delete(self, news_id):
        return in_progress, 200
