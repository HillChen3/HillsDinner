import hashlib
from flask_restplus import Resource, abort, reqparse
from flask import request, app


TOKEN = '123456'

in_progress = "Interface is still in progress"

APIS = {
    'SMS': {'task': 'get PhoneNumber and send the SMS, verify SMS'},
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

class SetWechat(Resource):
    def get(self):
        #这里改写你在微信公众平台里输入的token
        token = TOKEN
        #获取输入参数
        data = request.args
        signature = data.get('signature','')
        print(signature)
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        #字典排序
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0] + list[1] + list[2]
        #sha1加密算法
        hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        print(hascode)
        #如果是来自微信的请求，则回复echostr
        if hascode == signature:

            return echostr
            print("hascode == signature")
        #else:
        #    return "set wechat failed"

