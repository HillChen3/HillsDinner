from flask_restful import Resource, abort, reqparse
from flask import request
from flask import jsonify
from common import sms

TODOS = {
    'sendSMS': {'task': 'get PhoneNumber and send the SMS'},
    'verifySMS': {'task': 'verify the SMS code'},

}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class SendSMS(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def put(self,):

        phone_number = request.form['phone']
        if phone_number is not None :
            if sms.send_message(phone_number):
                return "send SMS successfully to " + phone_number, 200
            else:
                return "send SMS failed to " + phone_number, 400
        else:
            return "phone is NULL", 401

class VerifySMS(Resource):
    def put(self):
        phone_number = request.form['phone']
        SMS_code = request.form['smscode']
        if phone_number is not None and SMS_code is not None :
            if sms.verify(phone_number,SMS_code):
                return "verify successfully", 200
            else:
                return "verify failed", 400
        else:
            return "phone or SMScode is NULL", 401



