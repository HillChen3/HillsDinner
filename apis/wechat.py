from flask import request, current_app, Response
from flask_restplus import Namespace, reqparse, Resource
from wechatpy import WeChatClient
from wechatpy.utils import check_signature
from models.models import wechat_user_info_model
from models.models import WechatUserInfo
from playhouse.shortcuts import model_to_dict, dict_to_model

from resource import settings
parser = reqparse.RequestParser()
api = Namespace('wechat', description='wechat operation')


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
        if client.user.get(openid):
            print(client.user.get(openid))
        user = client.user.get(openid)
        if not WechatUserInfo.get(WechatUserInfo.openid == openid):
            wechat_userinfo = dict_to_model(WechatUserInfo, user)
            result = wechat_userinfo.save()
            print(result)
        else:
            print("user has saved")





