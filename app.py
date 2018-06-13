from flask import Flask
from flask_restplus import fields, Resource, reqparse
from flask_cors import CORS

from apis import api


app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
app.config['RESTPLUS_VALIDATE'] = True
app.config['BUNDLE_ERRORS'] = True
CORS(app)

@api.route('/Template')
class Template(Resource):
    template_model = api.model('TempModel',
                               {
                                   'username': fields.String,
                                   'password': fields.String
                               })

    @api.marshal_list_with(template_model)
    @api.doc(params={"username": "username", "password": "password"})
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="input your username")
        parser.add_argument('password', type=str, required=True, help="input your password")
        args = parser.parse_args()
        return args


api.init_app(app)
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
