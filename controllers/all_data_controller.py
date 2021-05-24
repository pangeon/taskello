from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_task_full_details(conn):
    records = db.sql_querry(conn, sql_select.all_data_inspect)
    return records