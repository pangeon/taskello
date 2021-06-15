from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_all_profiles(conn):
    profiles = db.sql_querry(conn, sql_select.all_profiles)
    return profiles

def login_profile(conn, val):
    sql = "SELECT * FROM profiles WHERE email = %s AND password = %s"
    profile = db.sql_querry(conn, sql, val)
    try: 
        return profile[0]
    except IndexError as e:
        print("Profile with the given email and password does not exist.")
        return None


def get_profile_email(conn, val):
    sql = "SELECT * FROM profiles WHERE email = '{}'".format(val)
    profile = db.sql_single_querry(conn, sql)
    try: 
        return profile
    except IndexError as e:
        print("Profile with the given email does not exist.")
        return None


def get_profile_id(conn, val):
    sql = "SELECT id FROM profiles WHERE email = '{}'".format(val)
    profile_id = db.sql_single_querry(conn, sql)
    try: 
        return profile_id[0]
    except IndexError as e:
        print("Profile with the given email does not exist.")
        return None


def insert_profile(conn, val):
    sql = "INSERT INTO profiles (name, surname, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def create_profile_to_registry(conn, val):
    sql = "INSERT INTO profiles (email, password) VALUES (%s, %s)"
    db.sql_execute(conn, sql, val)


def update_profile_name_and_surname(conn, val):
    sql = "UPDATE profiles SET name = %s, surname = %s WHERE email = %s"
    db.sql_execute(conn, sql, val)


def update_profile_password(conn, val):
    sql = "UPDATE profiles SET password = %s WHERE email = %s"
    db.sql_execute(conn, sql, val)


def grant_profile_active_status(conn, val):
    sql = "UPDATE profiles SET is_active = 1 WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_profile_for_email(conn, val):
    sql = "DELETE FROM profiles WHERE email = '{}'".format(val)
    db.sql_drop(conn, sql)
