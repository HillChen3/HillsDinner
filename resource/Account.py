from flask_restplus import Resource, abort, reqparse
from flask import request
from common import utils

in_progress = "Interface is still in progress"

APIS = {
    'sendSMS': {'task': 'get PhoneNumber and send the SMS'},
    'verifySMS': {'task': 'verify the SMS code'},
    'register': {'task': 'register new account'},
    'login': {'task': 'login in and get token'}
}


def abort_if_todo_doesnt_exist(api_id):
    if api_id not in APIS:
        abort(404, message="API {} doesn't exist".format(api_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class SendSMS(Resource):
    def get(self, api_id):
        abort_if_todo_doesnt_exist(api_id)
        return APIS[api_id]

    def put(self,):
        phone_number = request.form['phone']
        # 需要检查电话号码格式
        if utils.check_phone_num(phone_number):
            flag, message = utils.send_message(phone_number)
            return message, 200 if flag else 400
        return "invalid phone num", 401


class VerifySMS(Resource):
    def put(self):
        phone_number = request.form['phone']
        SMS_code = request.form['smscode']
        if phone_number is not None and SMS_code is not None :
            if utils.verify(phone_number, SMS_code):
                return "verify successfully", 200
            else:
                return "verify failed", 400
        else:
            return "phone or SMS code is NULL", 401


class Register(Resource):
    def post(self):
        return in_progress, 200


class Login(Register):
    def get(self):
        return in_progress, 200