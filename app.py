from flask import *
from flask.ext.restful import Api
from resource import Register
app = Flask(__name__)
api = Api(app)
api.add_resource(Register.SendSMS, '/register/sendSMS')
api.add_resource(Register.VerifySMS, '/register/verifySMS')


if __name__ == '__main__':
    app.run(debug=True)
