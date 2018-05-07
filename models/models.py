from flask_restplus import fields

# user operation model, follow, like etc
operation_model = {
    'user_id': fields.String(description="user_id"),
    'username': fields.String(description='username'),
    'group_id': fields.String(description="group_id"),
    'group_name': fields.String(description='group name'),
    'type': fields.String(description="1 = follow, 2 = like", required=True),
    'type_name': fields.String(description='follow or like ...')
}

# user model, used to save all user information
user_model = {
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
    'self_intro': fields.String(description="introduce yourself")
}

# group model, used to save all group information
group_model = {
    'group_id': fields.String(description='group_id', required=True),
    'group_name': fields.String(description="group's name", required=True),
    'group_topic': fields.String(description='topic in group', required=True),
    'build_time': fields.DateTime(description='When did group build'),
    'event_location': fields.String(description='online, offline or both'),
    'group_QRCode': fields.String(description='the url for group QRCode'),
    'is_verify_need': fields.Boolean(description='Is user need verify to join this group'),
    'join_question': fields.String(description='Ask a question to newcomer'),
    'group_desc': fields.String(description='group information')
}

# user verify model for join a verify needed group
group_user_verify_model = {
    'user_id': fields.String(description='user id'),
    'username': fields.String(description="username", required=True),
    'group_id': fields.String(description='group id'),
    'group_name': fields.String(description='group name'),
    'content': fields.String(description="Why you wanna join", required=True)
}
