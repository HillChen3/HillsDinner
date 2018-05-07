from flask import request, Response
from flask_restplus import Resource, abort, reqparse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from common import wechat_util
from wechatpy import WeChatClient


TOKEN = '123456'
APPID = 'wx1010fd146b9b290c'
APPSECRET = '28d394c4e3b83b4145642eec67a5c5d4'

class SetWechatServer(Resource):
    def get(self):
        token = TOKEN
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        try:
            check_signature(token, signature, timestamp, nonce)
            return Response(response=echostr, content_type='text/html')
            print("set wechat server successfully")
        except InvalidSignatureException:
            return "check signature failed"


class GetUserInfo(Resource):
    def get(self):
        appID = APPID
        appSecret = APPSECRET
        client = WeChatClient(appID, appSecret)
        user = client.user.get('openid')



