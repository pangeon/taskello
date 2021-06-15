from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db


def show_all_types(conn):
    types = db.sql_querry(conn, sql_select.all_types)
    return types


def show_type_for_id(conn, val):
    sql = "SELECT * FROM types WHERE id = '{}'".format(val)
    type = db.sql_single_querry(conn, sql)
    return type


def insert_type(conn, val):
    sql = "INSERT INTO types (specification, responsibilities, color) VALUES (%s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_type_properties(conn, val):
    sql = "UPDATE types SET specification = %s, responsibilities = %s, color = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_type_for_id(conn, val):
    sql = "DELETE FROM types WHERE id = '{}'".format(val)
    db.sql_drop(conn, sql, multi=False)