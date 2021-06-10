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

## Profiles
def all_profiles():
    return profile_man.show_all_profiles(conn)


def login(val):
    return profile_man.login_profile(conn, val)


def is_email_exist(e_mail):
    profile_list = profile_man.show_all_profiles(conn)
    profiles_emails = []
    for unpack_item in profile_list:
        (id, name, surname, email, password, active) = unpack_item
        profiles_emails.append(email)

    if e_mail in profiles_emails:
        return True
    else:
        return False


def email(val):
    return profile_man.get_profile_email(conn, val)


def registry(val):
    return profile_man.create_profile_to_registry(conn, val)


def profile_id(val):
    return profile_man.get_profile_id(conn, val)


def edit_profile_data(val):
    return profile_man.update_profile_name_and_surname(conn, val)


def edit_profile_pass(val):
    return profile_man.update_profile_password(conn, val)


def remove(val):
    return profile_man.delete_profile_for_email(conn, val)
## Profiles


## Types
def all_types():
    return type_man.show_all_types(conn)


def show_type(val):
    return type_man.show_type_for_id(conn, val)


def insert_type(val):
    return type_man.insert_type(conn, val)


def edit_type(val):
    return type_man.update_type_properties(conn, val)


def delete_type(val):
    return type_man.delete_type_for_id(conn, val)
## Types


## Tasks
def all_tasks():
    return task_man.show_all_tasks(conn)


def show_task(val):
    return task_man.show_task_for_id(conn, val)


def insert_task(val):
    return task_man.insert_task_with_id(conn, val)


def task_priority(val):
    return task_man.update_task_priority(conn, val)


def all_tasks_details():
    return all_data_man.show_task_full_details(conn)


def delete_task(val):
    return task_man.delete_task_for_id(conn, val)


def user_tasks(val):
    return all_data_man.show_task_assign_for_login_profile(conn, val)


def assign_task(val):
    return ass_task_man.insert_assign_task(conn, val)
## Tasks