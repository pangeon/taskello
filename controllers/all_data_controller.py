from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_task_full_details(conn):
    records = db.sql_querry(conn, sql_select.all_data_inspect)
    return records

def show_task_assign_for_login_profile(conn, val):
    sql = sql_select.tasks_for_login_user.format(val)
    records = db.sql_querry(conn, sql)
    try:
        return records
    except IndexError as e:
        print("Profile with the given email does not exist.")
        return None