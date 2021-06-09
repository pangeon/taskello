from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_all_types(conn):
    types = db.sql_querry(conn, sql_select.all_types)
    return types


def insert_type(conn, val):
    sql = "INSERT INTO types (specification, responsibilities, color) VALUES (%s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_type_specication(conn, val):
    sql = "UPDATE types SET specification = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_type_responsibilities(conn, val):
    sql = "UPDATE types SET responsibilities = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_type_color(conn, val):
    sql = "UPDATE types SET color = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_type_for_id(conn, val):
    sql = "DELETE FROM types WHERE id = '{}'".format(val)
    db.sql_execute(conn, sql, val)
