import mysql.connector
from mysql.connector import Error
from utils.db_manager import _conn_messages as info

def connect_to_db(host, db, user, password):
    try:
        sql_use_querry = "select database();" 
        conn = mysql.connector.connect(
            host=host,
            database=db,
            user=user,
            password=password
        )
        if conn.is_connected():
            db_ver = conn.get_server_info()
            print(info.serv_ver_info, db_ver)
            
            cursor = conn.cursor()
            cursor.execute(sql_use_querry)

            record = cursor.fetchone()
            print(info.conn_success_info, record)

    except Error as e:
        print(conn_error_info, e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print(info.conn_close_info)