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
    'username': fields.String(description="username", required=True),
    'nickname': fields.String(description="nickname", required=True),
    'avatar': fields.String(description="avatar", required=True),
    'gender': fields.String(description="gender", required=True),
    'phone_num': fields.String(description="phone_num", required=True),
    'job': fields.String(description="tell us what do you do"),
    'wechat_id': fields.String(description="wechat account"),
    'wechat_headimg':fields.String(description="wehat headimg"),
    'constellation': fields.String(description="constellation"),
    'pet_plant': fields.String(description="dog cat or?"),
    'hobbies': fields.String(description="what do you like to do?"),
    'fav_event_type': fields.String(description="what event's type do you like?"),
    'self_intro': fields.String(description="introduce yourself")
}


class User(BaseModel):
    # user model, used to save all user information
    user_id = CharField(null=True)
    username = CharField(null=True)
    nickname = CharField(null=True)
    avatar = CharField(null=True)
    gender = CharField(null=True)
    phone_num = CharField(null=True)
    job = CharField(null=True)
    wechat_id = CharField(null=True)
    constellation = CharField(null=True)
    pet_plant = CharField(null=True)
    hobbies = CharField(null=True)
    fav_event_type = CharField(null=True)
    self_intro = CharField(null=True)


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
