from flask_restplus import Resource, abort, reqparse, Namespace
from models.models import operation_model

api = Namespace('Operation', description="like, follow, unlike, unfollow etc")
operation_model = api.model('OperationModel', operation_model)
in_progress = "Interface is still in progress"

APIS = {
    'group-user-link': {'task': 'follow, like, join, unfollow, unlike, leave'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('type', type=str)


@api.route('/like')
class Like(Resource):
    @api.marshal_list_with(operation_model)
    def get(self):
        return in_progress, 200

    @api.doc(body=operation_model)
    def post(self):
        args = parser.parse_args()
        return in_progress, 200


@api.route('/follow')
class Like(Resource):
    @api.marshal_list_with(operation_model)
    def get(self):
        return in_progress, 200

    @api.doc(body=operation_model)
    def post(self):
        args = parser.parse_args()
        return in_progress, 200
