from flask_restplus import fields
from peewee import *
from playhouse.migrate import *

db = MySQLDatabase('aceyouth', user='root', password='ace123', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


# user model, used to save all user information
user_model = {
    'user_id': fields.String(description="user_id", required=True),
    'nickname': fields.String(description="nickname", required=True),
    'phone_num': fields.String(description="phone_num", required=True),
    'gender': fields.String(description="gender", required=True),
    'job': fields.String(description="tell us what do you do"),
    'personal_tag': fields.String(description="what's your personal tags?"),
    'fav_event_type': fields.String(description="what event's type do you like?"),
    'self_intro': fields.String(description="introduce yourself"),
    'register_time': fields.String(description="user register time"),
    'status': fields.Boolean(description="true means user can use normally, false means cannot use", default=True),
    'last_login_time': fields.String(description="the time of the user last login")

}


class User(BaseModel):
    # user model, used to save all user information
    user_id = CharField(null=True)
    nickname = CharField(null=True)
    phone_num = CharField(null=True)
    gender = CharField(null=True)
    job = CharField(null=True)
    personal_tag = CharField(null=True)
    fav_event_type = CharField(null=True)
    self_intro = CharField(null=True)
    register_time = CharField(null=True)
    status = BooleanField(default=True)
    last_login_time = CharField(null=False)


# group model, used to save all group information
group_model = {
    'group_id': fields.String(description='group_id', required=True),
    'group_name': fields.String(description="group's name", required=True),
    'group_topic': fields.String(description='topic in group', required=True),
    'build_time': fields.String(description='When did group build'),
    'event_location': fields.String(description='online, offline or both'),
    'group_QRCode': fields.String(description='the url for group QRCode'),
    'is_verify_need': fields.Boolean(description='Is user need verify to join this group'),
    'join_question': fields.String(description='Ask a question to newcomer'),
    'group_desc': fields.String(description='group information'),
    'owner_id': fields.String(description='who build this group')
}


class Group(BaseModel):
    # user model, used to save all user information
    group_id = CharField(null=True)
    group_name = CharField(null=True)
    group_topic = CharField(null=True)
    build_time = CharField(null=True)
    event_location = CharField(null=True)
    group_QRCode = CharField(null=True)
    is_verify_need = BooleanField(default=False)
    join_question = CharField(null=True)
    group_desc = CharField(null=True)
    owner_id = ForeignKeyField(User, backref='group_owner')


db.connect()
db.create_tables([User, Group])

# user operation model, follow, like etc
operation_model = {
    'user_id': fields.String(description="user_id"),
    'username': fields.String(description='username'),
    'group_id': fields.String(description="group_id"),
    'group_name': fields.String(description='group name'),
    'type': fields.String(description="1 = follow, 2 = like", required=True),
    'type_name': fields.String(description='follow or like ...')
}

# user verify model for join a verify needed group
group_user_verify_model = {
    'user_id': fields.String(description='user id'),
    'username': fields.String(description="username", required=True),
    'group_id': fields.String(description='group id'),
    'group_name': fields.String(description='group name'),
    'content': fields.String(description="Why you wanna join", required=True)
}

#wechat information model
wechat_user_info_model = {
    'subscribe': fields.String(),
    'openid': fields.String(),
    'nickname': fields.String(),
    'sex': fields.String(),
    'language': fields.String(),
    'city': fields.String(),
    'province':fields.String(),
    'country': fields.String(),
    'headimgurl': fields.String(),
    'subscribe_time': fields.String(),
    'remark': fields.String(),
    'groupid': fields.String(),
    'tagid_list': fields.String(),
    'subscribe_scene': fields.String(),
    'qr_scene': fields.String(),
    'qr_scene_str': fields.String(),
}

class WechatUserInfo(BaseModel):
    subscribe = CharField(null=True)
    openid = CharField(null=True)
    nickname = CharField(null=True)
    sex = CharField(null=True)
    language = CharField(null=True)
    city = CharField(null=True)
    province = CharField(null=True)
    country = CharField(null=True)
    headimgurl = CharField(null=True)
    subscribe_time = CharField(null=True)
    remark = CharField(null=True)
    groupid = CharField(null=True)
    tagid_list = CharField(null=True)
    subscribe_scene = CharField(null=True)
    qr_scene = CharField(null=True)
    qr_scene_str = CharField(null=True)
