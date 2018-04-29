from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'SMS': {'task': 'get PhoneNumber and send the SMS, verify SMS'},
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class SendSMS(Resource):
    def put(self, phone_num):
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_num):
            flag, message = utils.send_message(phone_num)
            return message, 200 if flag else 400
        return "invalid phone num", 401


class VerifySMS(Resource):
    def post(self, phone_num, verify_code):
        if phone_num is not None and verify_code is not None :
            if utils.verify(phone_num, verify_code):
                return "verify successfully", 200
            else:
                return "verify failed", 400
        else:
            return "phone or SMS code is NULL", 401
