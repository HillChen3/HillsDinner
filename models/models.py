from flask_restplus import fields
from peewee import *
from playhouse.migrate import *
import datetime

db = MySQLDatabase('aceyouth', user='root', password='ace123', host='127.0.0.1', port=3306)


class BaseModel(Model):
    class Meta:
        database = db


# user model, used to save all user information
user_model = {
    'id': fields.String(description="user_id", required=True),
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
    'id': fields.String(description='group_id', required=True),
    'group_wallpaper': fields.String(description="wall paper url"),
    'group_name': fields.String(description="group's name", required=True),
    'group_topic': fields.String(description='topic in group', required=True),
    'build_time': fields.String(description='When did group build'),
    'event_location': fields.String(description='online, offline or both'),
    'group_QRCode': fields.String(description='the url for group QRCode'),
    'group_tag': fields.String(description="What your group main goal"),
    'is_verify_need': fields.Boolean(description='Is user need verify to join this group'),
    'join_question': fields.String(description='Ask a question to newcomer'),
    'group_intro': fields.String(description='short desc for group'),
    'group_desc': fields.String(description='group information'),
    'owner': fields.String(description='who build this group')
}


class Group(BaseModel):
    # user model, used to save all user information
    group_wallpaper = CharField(null=True)
    group_name = CharField(null=True)
    group_topic = CharField(null=True)
    build_time = DateTimeField(default=datetime.datetime.today())
    event_location = CharField(null=True)
    group_QRCode = CharField(null=True)
    group_tag = CharField(null=True)
    is_verify_need = BooleanField(default=False)
    join_question = CharField(null=True)
    group_intro = CharField(null=True)
    group_desc = CharField(null=True)
    owner = ForeignKeyField(User, backref='groups')


class GroupUserRelation(BaseModel):
    user = ForeignKeyField(User, backref='group_relation')
    group = ForeignKeyField(Group, backref='group_relation')
    action = IntegerField(default=0)  # 1 join, 2 follow, 3 like 4 favorite
    action_time = DateTimeField(default=datetime.datetime.today())


# user operation model, follow, like etc
operation_model = {
    'user_id': fields.String(description="user_id", required=True),
    'type': fields.String(description="1 join, 2 follow, 3 like 4 favorite", required=True)
}

# user verify model for join a verify needed group
group_user_verify_model = {
    'user_id': fields.String(description='user id'),
    'username': fields.String(description="username", required=True),
    'group_id': fields.String(description='group id'),
    'group_name': fields.String(description='group name'),
    'content': fields.String(description="Why you wanna join", required=True)
}

# wechat information model
wechat_user_info_model = {
    'subscribe': fields.String(description='wechat subscribe'),
    'openid': fields.String(description='wechat openid'),
    'nickname': fields.String(description='wechat nickname'),
    'sex': fields.String(description='wechat sex'),
    'language': fields.String(description='wechat language'),
    'city': fields.String(),
    'province': fields.String(),
    'country': fields.String(),
    'headimgurl': fields.String(),
    'subscribe_time': fields.String(),
    'remark': fields.String(),
    'groupid': fields.String(),
    'tagid_list': fields.String(),
    'subscribe_scene': fields.String(),
    'qr_scene': fields.String(),
    'qr_scene_str': fields.String(),
    'user': fields.String(description="which user own this wechat info")
}

# group news model
group_news_model = {
    'id': fields.String(),
    'context': fields.String(),
    'picture_url': fields.String(),
    'create_time': fields.DateTime(),
    'owner': fields.String()
}


class GroupNews(BaseModel):
    context = CharField(null=True)
    picture_url = CharField(null=True)
    create_time = DateTimeField(default=datetime.datetime.today())
    owner = ForeignKeyField(Group, backref='news')


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
    user = ForeignKeyField(User, backref='wechat')


activity_info_model = {
    'activity_poster': fields.String(description="activity's poster"),
    'activity_name': fields.String(description="activity name"),
    'activity_time': fields.String(description="activity holding time"),
    'activity_deadline': fields.String(description="activity deadline"),
    'activity_place': fields.String(description="where will hold this activity"),
    'activity_type': fields.String(description="which type this activity is"),
    'activity_price': fields.String(description="how much should be pay for this activity"),
    'activity_detail': fields.String(),
    'activity_pictures': fields.String(),
    'activity_required_info': fields.String(),
    'group': fields.String(description="which group this activity belongs"),
}


class ActivityInfo(BaseModel):
    activity_poster = CharField(null=True)
    activity_name = CharField(null=True)
    activity_time = CharField(null=True)
    activity_deadline = CharField(null=True)
    activity_place = CharField(null=True)
    activity_type = CharField(null=True)
    activity_price = CharField(null=True)
    activity_detail = CharField(null=True)
    activity_pictures = CharField(null=True)
    activity_required_info = CharField(null=True)
    group = ForeignKeyField(Group, backref='activity')


class ActivityUserRelation(BaseModel):
    activity = ForeignKeyField(ActivityInfo, backref='activity_relation')
    user = ForeignKeyField(User, backref='activity_relation')
    action = IntegerField(default=0)  # 1 join, 2 follow


db.connect()
db.create_tables([User, Group, WechatUserInfo, ActivityInfo, GroupUserRelation, ActivityUserRelation, GroupNews])
