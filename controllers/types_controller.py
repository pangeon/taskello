from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_all_types(conn):
    types = db.sql_querry(conn, sql_select.all_types)

    for type in types:
        print(type)


def insert_type(conn, val):
    sql = "INSERT INTO Types (specification, responsibilities, color) VALUES (%s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_type_specication(conn, val):
    sql = "UPDATE Types SET specification = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_type_responsibilities(conn, val):
    sql = "UPDATE Types SET responsibilities = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_type_color(conn, val):
    sql = "UPDATE Types SET color = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_type_for_id(conn, val):
    sql = "DELETE FROM Types WHERE id = %s"
    db.sql_execute(conn, sql, val)