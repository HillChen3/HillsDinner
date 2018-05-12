from flask import request
from flask_restplus import Resource

from wechatpy import WeChatClient

from common import db_utils

TOKEN = '123456'
APPID = 'wx7293651d4f67e9d5'
APPSECRET = '28d394c4e3b83b4145642eec67a5c5d4'

class GetWechatInfo(Resource):
    def get(self,appid,appsecret):
        data = request.args
        openid = data.get('openid')
        client = WeChatClient(appid, appsecret)
        user = client.user.get(openid)
        nickname = user.get('nickname')
        sex = user.get('sex')
        language = user.get('language')
        city = user.get('city')
        province = user.get('province')
        country = user.get('country')
        headimgurl = user.get('headimgurl')
        add_user = ('INSERT INTO users '
                   '(wechat_id, nickname, gender,city,province, country, headimgurl) values ("{}", "{}", "{}", "{}", "{}", "{}", "{}")')
        add_user = add_user.format(openid, nickname, sex, city,province, country,headimgurl)
        if user is not None:
            db_utils.no_query(add_user)
            return "add wechat information for user successfully"