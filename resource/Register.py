from flask_restful import Resource, abort, reqparse
from flask import request
from flask import jsonify
from common import utils


APIS = {
    'sendSMS': {'task': 'get PhoneNumber and send the SMS'},
    'verifySMS': {'task': 'verify the SMS code'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in APIS:
        abort(404, message="API {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class SendSMS(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return APIS[todo_id]

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



