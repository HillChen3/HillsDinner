import hashlib

from flask import Flask, request
from flask_restplus import Api
from common import wechat
from resource import Session, User, CommGroup, GroupUserLink, GroupUserVerify, GroupNews, SMS


app = Flask(__name__)
api = Api(app)
api.add_resource(wechat.SetWechatServer, "/wechat/setwechat")
api.add_resource(wechat.GetAccessToken, "/wechat/getaccessstoken")
api.add_resource(SMS.SendSMS, '/SMS/<phone_num>')
api.add_resource(SMS.VerifySMS, '/SMS/<verify_code>,<phone_num>')
api.add_resource(Session.Session, '/session')
api.add_resource(User.User, '/user/<user_id>')
api.add_resource(User.UserList, '/user/<group_id>')
api.add_resource(CommGroup.CommGroup, '/group/<group_id>')
api.add_resource(CommGroup.CommGroupList, '/group')
api.add_resource(CommGroup.CommGroupByUser, '/user/<user_id>/group')
api.add_resource(User.GroupUser, '/group/<group_id>/user/<user_id>')
api.add_resource(User.GroupUserList, '/group/<group_id>/user')
api.add_resource(GroupUserLink.UserLinkList, '/group_user_link/<user_id>')
api.add_resource(GroupUserLink.GroupUserLink, '/group_user_link/<user_id>,<group_id>')
api.add_resource(GroupUserVerify.Group_User_Verify, '/group_user_verify/<verify_id>')
api.add_resource(GroupUserVerify.Group_User_Verify_List, '/group_user_verify/<group_id>/list')
api.add_resource(GroupNews.GroupNews, '/group_news/<news_id>')
api.add_resource(GroupNews.GroupNewsList, '/group_news/<group_id>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
