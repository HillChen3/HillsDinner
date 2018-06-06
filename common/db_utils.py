import os

from playhouse.shortcuts import model_to_dict, dict_to_model
import mysql.connector
from playhouse.db_url import connect


def get_connection():
    return mysql.connector.connect(host='localhost', user='root', passwd='ace123', db='aceyouth')


def no_query(input_sql):
    exec_sql(input_sql=input_sql, operation_type='no_query')


def query(input_sql):
    return exec_sql(input_sql=input_sql, operation_type='query')


def exec_sql(input_sql, operation_type):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(input_sql)
        cursor.execute(input_sql)
        if operation_type == 'query':
            result = cursor.fetchall()
            print('result is : ', result)
            return result
        elif operation_type == 'no_query':
            conn.commit()
    except RuntimeError:
        print(RuntimeError)
        raise RuntimeError
    finally:
        cursor.close()
        conn.close()


