from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_all_profiles(conn):
    profiles = db.sql_querry(conn, sql_select.all_profiles)
    return profiles


def insert_profile(conn, val):
    sql = "INSERT INTO Profiles (name, surname, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_profile_name_and_surname(conn, val):
    sql = "UPDATE Profiles SET name = %s, surname = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_profile_password(conn, val):
    sql = "UPDATE Profiles SET password = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def grant_profile_active_status(conn, val):
    sql = "UPDATE Profiles SET is_active = 1 WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_profile_for_id(conn, val):
    sql = "DELETE FROM Profiles WHERE id = %s"
    db.sql_execute(conn, sql, val)