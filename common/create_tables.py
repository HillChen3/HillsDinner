import common.db_utils as db
from mysql.connector import errorcode
import mysql.connector

DB_NAME = 'aceyouth'
conn = db.get_connection()
cursor = conn.cursor()

TABLES = {'users': (
    "CREATE TABLE `users` ("
    "  id MEDIUMINT NOT NULL AUTO_INCREMENT,"
    "  username varchar(200),"
    "  nickname varchar(100),"
    "  avatar varchar(500),"
    "  gender enum(0, 1, 2),"
    "  phone_num varchar(50),"
    "  job varchar(250),"
    "  wechat_id varchar(100),"
    "  constellation varchar(50),"
    "  pet_plant varchar(50),"
    "  hobbies varchar(150),"
    "  fav_event_type varchar(50),"
    "  self_intro varchar(500),"
    "  PRIMARY KEY (id)"
    ") ENGINE=InnoDB")}


def create_database(inside_cursor):
    try:
        inside_cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    conn.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
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