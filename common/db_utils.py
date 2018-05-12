import mysql.connector


def get_connection():
    return mysql.connector.connect(host='localhost', port=3306, user='root', passwd='ace123', db='aceyouth')


def insert(input_sql):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(input_sql)
        cursor.execute(input_sql)
        conn.commit()
    except (RuntimeError):
        print(RuntimeError)
        raise RuntimeError
    finally:
        cursor.close()
        conn.close()


def query(input_sql):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(input_sql)
        cursor.execute(input_sql)
        result = cursor.fetchall()
        print('query result is :', result)
        return result
    except RuntimeError:
        print(RuntimeError)
        raise RuntimeError
    finally:
        cursor.close()
        conn.close()
