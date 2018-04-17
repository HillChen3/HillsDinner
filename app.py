from flask import Flask
from flask.ext.restful import Api
from resource import Account, User, CommGroup


app = Flask(__name__)
api = Api(app)
api.add_resource(Account.SendSMS, '/account/sendSMS')
api.add_resource(Account.VerifySMS, '/account/verifySMS')
api.add_resource(Account.Register, '/account/register')
api.add_resource(Account.Login, '/account/login')
api.add_resource(User.User, 'user/')
api.add_resource(CommGroup.Comm_groups, 'Comm_group')

if __name__ == '__main__':
    app.run(debug=True)
