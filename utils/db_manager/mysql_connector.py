import mysql.connector
from mysql.connector import Error
from utils.db_manager import _conn_messages as info


def define_db(host, db, user, password):
    try:
        conn = mysql.connector.connect(
                host=host,
                database=db,
                user=user,
                password=password
            )
        return conn
    except Error as e:
        print("define_db: ", info.conn_error_info, e)


def close_conn(conn):
    if conn.is_connected():
        conn.close()
        print("close_conn: ", id(conn), info.conn_close_info)

def sql_querry(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        return records
    except Error as e:
        print("sql_querry: ", info.conn_error_info, e)


def sql_insert(conn, sql, val):
    try:
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as e:
        print("sql_insert: ", info.error_insert_info, e)


def connection_info(conn):
    try:
        sql_use_querry = "select database();"
        if conn.is_connected():
            db_ver = conn.get_server_info()
            print("connection_info: ", info.serv_ver_info, db_ver)
            
            record = sql_querry(conn, sql_use_querry)
            print("connection_info: ", info.conn_success_info, record)
    except Error as e:
        print(info.conn_error_info, e)
        