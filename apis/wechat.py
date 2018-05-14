from flask import request, current_app, Response
from flask_restplus import Namespace, reqparse, Resource
from wechatpy import WeChatClient
from wechatpy.utils import check_signature

from common import db_utils
from resource import settings
parser = reqparse.RequestParser()
api = Namespace('wechat', description='wechat operation')
query_user = 'SELECT id, username FROM users'

@api.route('/settings')
class SetWeChatServer(Resource):

    def get(self):
        token = settings.get_token()
        print(token)
        data = request.args
        signature = data.get('signature', '')
        timestamp = data.get('timestamp', '')
        nonce = data.get('nonce', '')
        echostr = data.get('echostr', '')
        try:
            check_signature(token, signature, timestamp, nonce)
            return Response(response=echostr, content_type='text/html')
            print("set wechat server successfully")
        except InvalidSignatureException:
            return "check signature failed"

    def post(self):
        appid = settings.get_appid()
        appsecret = settings.get_appsecret()
        menu_data = settings.get_menudata()
        openid = request.args.get('openid')
        print(openid)
        client = WeChatClient(appid, appsecret)
        client.menu.create(menu_data)
#        client.user.get(openid)
        query_single_user = query_user + " WHERE wechat_id =\"\"".format(openid)
        result = db_utils.query(query_single_user)
        if result:
            return "user has saved"
        else:
            return "need add the user"
