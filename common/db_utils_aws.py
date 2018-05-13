import mysql.connector


def get_connection():
    # return mysql.connector.connect(host='172.31.27.37', port=3306, user='root', passwd='ace123', db='aceyouth')
    return mysql.connector.connect(host='172.17.0.5', port=3306, user='root', passwd='ace123', db='aceyouth')


def no_query(input_sql):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print(input_sql)
        cursor.execute(input_sql)
        conn.commit()
    except RuntimeError:
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
        print('result is : ', result)
        return result
    except RuntimeError:
        print(RuntimeError)
        raise RuntimeError
    finally:
        cursor.close()
        conn.close()


def set_response_data(model, values):
    result = []
    for value in values:
        tmp = make_dict_by_model(model=model, value=value)
        print('tmp is : ', tmp)
        result.append(tmp)
    return result


def make_dict_by_model(model, value):
    if value:
        return dict(zip(model.keys(), value))
    else:
        return None
