from flask import Flask, Response
from flask_restplus import fields, Resource, reqparse
from wechatpy import WeChatClient

from apis import api
from wechatpy.utils import check_signature
from flask import request

from common import wechat
from resource import settings

app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
app.config['RESTPLUS_VALIDATE'] = True
app.config['BUNDLE_ERRORS'] = True
appid = app.config.get('APPID')
appsecret = app.config.get('APPSECRET')
menu_data = app.config.get('MENU_DATA')

@api.route('/Template')
class Template(Resource):
    template_model = api.model('TempModel',
                               {
                                   'username': fields.String,
                                   'password': fields.String
                               })

    @api.marshal_list_with(template_model)
    @api.doc(params={"username": "username", "password": "password"})
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="input your username")
        parser.add_argument('password', type=str, required=True, help="input your password")
        args = parser.parse_args()
        return args


@api.route('/wechat/settings')
class SetWechatServer(Resource):
    app.config.from_object(settings.wechatConstant)

    def get(self):
        token = app.config.get("TOKEN")
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
        client = WeChatClient(appid, appsecret)
#设置公众号菜单
        client.menu.create(menu_data)
#获取用户信息
        wechat.GetWechatInfo.get(self,appid,appsecret)





api.init_app(app)
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
