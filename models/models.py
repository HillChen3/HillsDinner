from flask_restplus import fields, Namespace

api = Namespace('models', description='models')

operation_model = api.model('OperationModel', {
    'group_id': fields.String(description="group_id", required=True),
    'type': fields.String(description="1 = follow, 2 = like", required=True)
})

user_model = api.model('UserModel', {
    'user_id': fields.String(description="user_id", required=True),
    'username': fields.String(description="username", required=True),
    'nickname': fields.String(description="nickname", required=True),
    'avatar': fields.String(description="avatar", required=True),
    'gender': fields.String(description="gender", required=True),
    'phone_num': fields.String(description="phone_num", required=True),
    'job': fields.String(description="tell us what do you do"),
    'wechat_id': fields.String(description="wechat account"),
    'constellation': fields.String(description="constellation"),
    'pet_plant': fields.String(description="dog cat or?"),
    'hobbies': fields.String(description="what do you like to do?"),
    'fav_event_type': fields.String(description="what event's type do you like?"),
    'self_intro': fields.String(description="introduce yourself"),
})