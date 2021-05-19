from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_all_tasks(conn):
    tasks = db.sql_querry(conn, sql_select.all_tasks)

    for task in tasks:
        print(task)


def insert_task(conn, val):
    sql = "INSERT INTO Tasks (type_id, name, description, attachment_link, priority) VALUES (%s, %s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_task_name_and_description(conn, val):
    sql = "UPDATE Tasks SET name = %s, description = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_task_attachment_link(conn, val):
    sql = "UPDATE Tasks SET attachment_link = %s, WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_task_priority(conn, val):
    sql = "UPDATE Tasks SET priority = %s, WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_task_for_id(conn, val):
    sql = "DELETE FROM Tasks WHERE id = %s"
    db.sql_execute(conn, sql, val)