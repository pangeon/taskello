from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def inspect_all_data(conn):
    records = db.sql_querry(conn, sql_select.all_data_inspect)

    for record in records:
        print(record)