from flask import Flask
from flask_restplus import Api
from resource import Account, User, CommGroup, GroupUserLink


app = Flask(__name__)
api = Api(app)
api.add_resource(Account.SendSMS, '/account/sendSMS')
api.add_resource(Account.VerifySMS, '/account/verifySMS')
api.add_resource(Account.Register, '/account/register')
api.add_resource(Account.Login, '/account/login')
api.add_resource(User.User, '/user/<user_id>')
api.add_resource(User.UserList, '/user/<group_id>')
api.add_resource(CommGroup.Comm_groups, '/comm_group')
api.add_resource(GroupUserLink.Group_User_link, '/group_user_link')

if __name__ == '__main__':
    app.run(debug=True)
