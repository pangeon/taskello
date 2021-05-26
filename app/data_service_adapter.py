from controllers import profiles_controller as profile_man
from controllers import types_controller as type_man
from controllers import tasks_controller as task_man
from controllers import assigned_tasks_controller as ass_task_man
from controllers import all_data_controller as all_data_man

from data import _db_config as cfg_db
from utils.db_manager import mysql_connector as db

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)

def all_profiles():
    return profile_man.show_all_profiles(conn)

def all_types():
    return type_man.show_all_types(conn)

def all_tasks():
    return task_man.show_all_tasks(conn)

def insert_task(val):
    return task_man.insert_task(conn, val)

def all_tasks_details():
    return all_data_man.show_task_full_details(conn)