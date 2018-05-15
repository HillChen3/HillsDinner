import mysql
from flask import request, current_app, Response
from flask_restplus import Namespace, reqparse, Resource
from wechatpy import WeChatClient
from wechatpy.utils import check_signature

from common import db_utils,create_tables
from resource import settings
parser = reqparse.RequestParser()
api = Namespace('wechat', description='wechat operation')
query_user = 'SELECT nickname FROM wechatinfo'

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
        print(client.user.get(openid))
        user = client.user.get(openid)
        insertdict('wechatinfo',user)
        # query_single_user = query_user + " WHERE wechat_id ={}".format(openid)
        # result = db_utils.query(query_single_user)
        # if result:
        #     return "user has saved"
        # else:
        #     db_utils.insertdict('wechatinfo',user)
# 插入字典到数据库
def insertdict(tablename, dict):

    ROWstr = ''  # 行字段

    for key in dict.keys():
        ROWstr = (ROWstr + '"%s"' + ',') % (dict[key])

# 判断表是否存在，存在执行try，不存在执行except新建表，再insert
    try:
        find_table = ("SELECT * FROM %s" % (tablename))
        add_info = ("INSERT INTO ()%s VALUES (%s)" % (tablename, ROWstr[:-1]))
        if db_utils.query(find_table) is not None:
            db_utils.no_query(add_info)
            return "add wechat info successfully"
        else:
            print( "not find table %s" % tablename)
            create_tables.create_database()
            return "created table %s" %tablename
    except Exception as e:
        return "connection mysql failed"




