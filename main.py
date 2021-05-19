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


def insert_profile(conn, val):
    sql = "INSERT INTO Profiles (name, surname, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
    db.sql_insert(conn, sql, val)


def insert_task(conn, val):
    sql = "INSERT INTO Tasks (type_id, name, description, attachment_link, priority) VALUES (%s, %s, %s, %s, %s)"
    db.sql_insert(conn, sql, val)


def insert_type(conn, val):
    sql = "INSERT INTO Types (specification, responsibilities, color) VALUES (%s, %s, %s)"
    db.sql_insert(conn, sql, val)


def insert_assign_task(conn, val):
    sql = "INSERT INTO Assigned_tasks (profile_id, task_id, progress_details) VALUES (%s, %s, %s)"
    db.sql_insert(conn, sql, val) 

if __name__ == "__main__":
    welcome()  
    db.connection_info(conn)
    
    # show_all_profiles(conn)

    # show_all_tasks(conn)
    # show_all_types(conn)
    # show_assigned_tasks(conn)

    # sql = '''
    #     INSERT INTO Profiles (name, surname, email, password, is_active)
    #     VALUES ("Adam", "Kos", "kos.adam@wp.pl", "BralemHere10", True);
    # '''
    # insert_profile(conn, ("Jan", "Mazurek", "mazurek@yahoo.com", "Nic123", False))
    # insert_assign_task(conn, (10, 1, "TO DO"))

    inspect_all_data(conn)


