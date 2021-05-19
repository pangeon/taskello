from utils import path_finder as path
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db
from data import _querries as sql_select


def welcome():
    print("--- {}, ver {} ---\n".format(app.name, app.version))

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)


def show_all_profiles(conn):
    profiles = db.sql_querry(conn, sql_select.all_profiles)

    for profile in profiles:
        print(profile)


def show_all_tasks(conn):
    tasks = db.sql_querry(conn, sql_select.all_tasks)

    for task in tasks:
        print(task)


def show_all_types(conn):
    types = db.sql_querry(conn, sql_select.all_types)

    for type in types:
        print(type)


def show_assigned_tasks(conn):
    assigned_tasks = db.sql_querry(conn, sql_select.all_assigned_tasks)

    for assigned_task in assigned_tasks:
        print(assigned_tasks)


def inspect_all_data(conn):
    records = db.sql_querry(conn, sql_select.all_data_inspect)

    for record in records:
        print(record)


if __name__ == "__main__":
    welcome()  
    db.connection_info(conn)
    
    show_all_profiles(conn)
    show_all_tasks(conn)
    show_all_types(conn)
    show_assigned_tasks(conn)

    inspect_all_data(conn)


