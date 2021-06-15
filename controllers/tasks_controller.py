from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db


def show_all_tasks(conn):
    tasks = db.sql_querry(conn, sql_select.all_tasks)
    return tasks

def show_task_for_id(conn, val):
    sql = "SELECT * FROM tasks WHERE id = '{}'".format(val)
    task = db.sql_single_querry(conn, sql)
    return task

def insert_task(conn, val):
    sql = "INSERT INTO tasks (type_id, name, description, attachment_link, priority) VALUES (%s, %s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def insert_task_with_id(conn, val):
    sql = "INSERT INTO tasks (id, type_id, name, description, attachment_link, priority) VALUES (%s, %s, %s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_task_name_and_description(conn, val):
    sql = "UPDATE tasks SET name = %s, description = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_task_attachment_link(conn, val):
    sql = "UPDATE tasks SET attachment_link = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def update_task_priority(conn, val):
    sql = "UPDATE tasks SET priority = %s WHERE id = %s"
    db.sql_execute(conn, sql, val)


def delete_task_for_id(conn, val):
    sql = "DELETE FROM tasks WHERE id = '{}'".format(val)
    db.sql_drop(conn, sql)
