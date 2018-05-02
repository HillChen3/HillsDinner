import hashlib

from flask import Flask, request
from flask_restplus import Api
from common import wechat
from resource import Session, User, CommGroup, GroupUserLink, GroupUserVerify, GroupNews, SMS


app = Flask(__name__)
api = Api(app)
#api.add_resource(wechat.SetWechat, "/wechat/setwechat")
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

@app.route('/wechat/setwechat',methods=['GET','POST'])
def wechat():

    if request.method == 'GET':
        #这里改写你在微信公众平台里输入的token
        token = '123456'
        #获取输入参数
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        #字典排序
        list = [token, timestamp, nonce]
        list.sort()

        s = list[0] + list[1] + list[2]
        #sha1加密算法
        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        #如果是来自微信的请求，则回复echostr
        if hascode == signature:
            return echostr
        else:
            return ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
