import common.db_utils as db
from mysql.connector import errorcode
import mysql.connector

DB_NAME = 'aceyouth'
conn = db.get_connection()
cursor = conn.cursor()

arr_personaltags = [
    "脑洞暴发户",
    "强迫症患者",
    "多动症儿童",
    "画画儿的",
    "好奇心患者",
    "自由至上",
    "有志有痣",
    "公益力",
    "同理心",
    "社会设计",
    "摄影爱好者",
    "下笔如有神经病"
]
arr_grouptags = [
    "环保",
    "社区",
    "乡村",
    "文化教育",
    "自我认同",
    "生活美学",
    "阅读",
    "音乐",
    "运动"
]

TABLES = {'users': (
    "CREATE TABLE `users` ("
    "  id MEDIUMINT NOT NULL AUTO_INCREMENT,"
    "  username varchar(200),"
    "  nickname varchar(100),"
    "  avatar varchar(500),"
    "  gender int(2),"
    "  phone_num varchar(50),"
    "  job varchar(250),"
    "  wechat_id varchar(100),"
    "  city varchar(20),"
    "  province varchar(20),"
    "  country varchar(20),"
    "  headimgurl varchar(1000),"
    "  constellation varchar(50),"
    "  personal_tag varchar(50),"
    "  hobbies varchar(150),"
    "  fav_event_type varchar(50),"
    "  self_intro varchar(500),"
    "  PRIMARY KEY (id)"
    ") ENGINE=InnoDB"),

    "wechatinfo": (
        "CREATE TABLE `wechatinfo` ("
        "  subscribe varchar(20),"
        "  openid varchar(50),"
        "  nickname varchar(100),"
        "  sex int(2),"
        "  language varchar(10),"
        "  city varchar(20),"
        "  province varchar(20),"
        "  country varchar(20),"
        "  headimgurl varchar(1000),"
        "  subscribe_time varchar(50),"
        "  remark varchar(50),"
        "  groupid varchar(50),"
        "  tagid_list varchar(50),"
        "  subscribe_scene varchar(100),"
        "  qr_scene varchar(10),"
        "  qr_scene_str  varchar(100) "
        ")ENGINE=InnoDB"),

    "personal_tag": (
        "CREATE TABLE `personal_tag` ("
        "  pid MEDIUMINT NOT NULL AUTO_INCREMENT, "
        "  personal_tag varchar(50),"
        "  PRIMARY KEY (pid)"
        ")ENGINE=InnoDB"),

    "group_tag": (
        "CREATE TABLE `group_tag` ("
        "  gid MEDIUMINT NOT NULL AUTO_INCREMENT, "
        "  community_tag varchar(50), "
        "  PRIMARY KEY (gid)"
        ")ENGINE=InnoDB"),

    "personal_tagmap": (
        "CREATE TABLE `personal_tagmap` ("
        "t_pid int(100),"
        "pid int(100)"
        ")ENGINE=InnoDB"),

    "group_tagmap": (
        "CREATE TABLE `group_tagmap` ("
        " t_gid int(100),"
        " gid int(100)"
        ")ENGINE=InnoDB")

}


def create_database(inside_cursor):
    try:
        inside_cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def add_information(inside_cursor):
    try:
        for tag in arr_personaltags:
            inside_cursor.execute(
                "INSERT INTO use (personal_tag)VALUES {}".format(tag)
            )
        for tag in arr_grouptags:
            inside_cursor.execute(
                "INSERT INTO use (group_tag)VALUES {}".format(tag)
            )
    except mysql.connector.Error as err:

        print("Failed add info to database: {}".format(err))
        exit(1)


try:
    conn.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        add_information(cursor)
        conn.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
conn.close()
