from flask import Flask
from flask_restplus import Api, fields, Resource, reqparse
from resource import Session, User, CommGroup, GroupUserLink, GroupUserVerify, GroupNews, SMS
from resource.User import api as users
from resource.CommGroup import api as groups

app = Flask(__name__)
api = Api(app,
          title='ace-youth',
          version='0.1',
          description='restful api for ace-youth',
          # All API metadatas
          )

api.add_resource(SMS.SendSMS, '/SMS/<phone_num>')
api.add_resource(SMS.VerifySMS, '/SMS/<verify_code>,<phone_num>')
api.add_resource(Session.Session, '/session')
# api.add_resource(User.User, '/user/<user_id>')
# api.add_resource(User.UserList, '/user/<group_id>')
# api.add_resource(CommGroup.CommGroup, '/group/<group_id>')
# api.add_resource(CommGroup.CommGroupList, '/group')
# api.add_resource(CommGroup.CommGroupByUser, '/user/<user_id>/group')
# api.add_resource(User.GroupUser, '/group/<group_id>/user/<user_id>')
# api.add_resource(User.GroupUserList, '/group/<group_id>/user')
api.add_resource(GroupUserLink.UserLinkList, '/group_user_link/<user_id>')
api.add_resource(GroupUserLink.GroupUserLink, '/group_user_link/<user_id>,<group_id>')
api.add_resource(GroupUserVerify.Group_User_Verify, '/group_user_verify/<verify_id>')
api.add_resource(GroupUserVerify.Group_User_Verify_List, '/group_user_verify/<group_id>/list')
api.add_resource(GroupNews.GroupNews, '/group_news/<news_id>')
api.add_resource(GroupNews.GroupNewsList, '/group_news/<group_id>')

api.add_namespace(users, '/user')
api.add_namespace(groups, '/group')


template_model = api.model('TempModel',
                           {
                               'user_name': fields.String,
                               'password': fields.String
                           })


@api.route('/Template')
class Template(Resource):
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
