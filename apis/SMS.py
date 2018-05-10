from flask_restplus import Resource, abort, reqparse, Namespace
from common import utils

api = Namespace('SMS', description="send and verify sms")
APIS = {
    'SMS': {'task': 'get PhoneNumber and send the SMS, verify SMS'},
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

@api.route('/<phone_num>')
class SendSMSCode(Resource):
    def put(self, phone_num):
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_num):
            flag, message = utils.send_message(phone_num)
            if flag:
                return {
                "code": 200,
                "msg": message
                }
            else:
                return {
                "code":400,
                "msg": message
            }
        return{
            "code":401,
            "msg":"invalid phone num"
        }


@api.route('/<phone_num>, <verify_code>')
class VerifySMS(Resource):
    def post(self, phone_num, verify_code):
        if phone_num is not None and verify_code is not None :
            if utils.verify(phone_num, verify_code):
                return {
                    "code": 200,
                    "msg" :  "verify successfully"}
            else:
                return {
                    "code":400,
                    "msg" : "verify failed"
                }
        else:
            return {
                "code":401,
                "msg": "phone or SMS code is NULL"
            }
