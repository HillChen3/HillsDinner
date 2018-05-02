from flask import Flask
from flask_restplus import Api, fields, Resource, reqparse
from resource import Session, User, CommGroup, Operation, GroupUserVerify, GroupNews, SMS
from resource.User import api as users
from resource.CommGroup import api as groups
from resource.SMS import api as SMS
from resource.Session import api as session
from resource.GroupUserVerify import api as verify

app = Flask(__name__)
api = Api(app,
          title='ace-youth',
          version='0.1',
          description='restful api for ace-youth',
          # # All API metadatas
          )

api.add_namespace(users)
api.add_namespace(groups)
api.add_namespace(SMS)
api.add_namespace(session)
api.add_namespace(verify)


@api.route('/Template')
class Template(Resource):
    template_model = api.model('TempModel',
                               {
                                   'user_name': fields.String,
                                   'password': fields.String
                               })

    @api.marshal_list_with(template_model)
    @api.doc(params={"user_name": "username", "password": "password"})
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', type=str, required=True, help="input your username")
        parser.add_argument('password', type=str, required=True, help="input your password")
        args = parser.parse_args()
        return args


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
