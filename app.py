import hashlib
import time

import xml.etree.ElementTree as ET
from flask import *
from flask.ext.restful import Api
from resource import Register
app = Flask(__name__)
api = Api(app)
api.add_resource(Register.SendSMS, '/register/sendSMS')
api.add_resource(Register.VerifySMS, '/register/verifySMS')

@app.route('/',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        token='hill2018' #微信配置所需的token
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find('ToUserName').text
        fromu = xml_rec.find('FromUserName').text
        content = xml_rec.find('Content').text
        xml_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
        response = make_response(xml_rep % (fromu,tou,str(int(time.time())), content))
        response.content_type='application/xml'
        return response
    return 'Hello weixin!'
if __name__ == '__main__':
    app.run(debug=True)
