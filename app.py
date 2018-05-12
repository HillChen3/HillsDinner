from flask import Flask, Response
from flask_restplus import fields, Resource, reqparse
from wechatpy import WeChatClient

from apis import api
from wechatpy.utils import check_signature
from flask import request

from common import wechat, db_utils
from resource import settings

app = Flask(__name__)
app.config.SWAGGER_UI_JSONEDITOR = True
app.config['RESTPLUS_VALIDATE'] = True
app.config['BUNDLE_ERRORS'] = True

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
        appid = app.config.get('APPID')
        appsecret = app.config.get('APPSECRET')
        menu_data = app.config.get('MENU_DATA')
        client = WeChatClient(appid, appsecret)
        client.menu.create(menu_data)
        openid = request.args.get('openid')
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
        add_user = add_user.format(openid, nickname, sex, city, province, country, headimgurl)
        if user is not None:
            db_utils.no_query(add_user)
            return "add wechat information for user successfully"





api.init_app(app)
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
