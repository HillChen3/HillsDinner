from flask import Flask
from flask_restplus import Api, fields, Resource, reqparse
from resource import api

app = Flask(__name__)
api.init_app(app)


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
