from flask_restplus import Resource, abort, reqparse, Namespace
from models.models import group_user_verify_model


api = Namespace('user_verify', description="verify user who wanna join group")
group_user_verify_model = api.model('VerifyModel', group_user_verify_model)
in_progress = "Interface is still in progress"

APIS = {
    'group_user_verify': {'task': 'verify user who wanna join group'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('content', type=str)


@api.route('/<verify_id>')
class Verify(Resource):
    @api.marshal_with(group_user_verify_model)
    def get(self, verify_id):
        return in_progress, 200
    @api.doc(body=group_user_verify_model)
    def post(self, verify_id):
        return in_progress, 200



