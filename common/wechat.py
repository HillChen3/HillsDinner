
from flask_restplus import Resource, abort, reqparse, api

from wechatpy import WeChatClient

TOKEN = '123456'
APPID = 'wx7293651d4f67e9d5'
APPSECRET = '28d394c4e3b83b4145642eec67a5c5d4'



@api.route('/wechat/getuserinfo')
class GetUserInfo(Resource):
    def get(self):
        appID = APPID
        appSecret = APPSECRET
        client = WeChatClient(appID, appSecret)
        user = client.user.get('openid')
        return user