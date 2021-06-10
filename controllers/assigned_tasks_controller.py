from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db


def show_assigned_tasks(conn):
    assigned_task = db.sql_querry(conn, sql_select.all_assigned_tasks)
    return assigned_task


def show_ass_task_for_task_id(conn, val):
    sql = "SELECT * FROM assigned_tasks WHERE task_id = '{}'".format(val)
    ass_task = db.sql_single_querry(conn, sql)
    return ass_task


def insert_assign_task(conn, val):
    sql = "INSERT INTO assigned_tasks (profile_id, task_id, progress_details, expired_date) VALUES (%s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def update_ass_task_progress(conn, val):
    sql = "UPDATE assigned_tasks SET progress_details = %s WHERE task_id = %s"
    db.sql_execute(conn, sql, val)


def delete_assigned_task_for_id(conn, val):
    sql = "DELETE FROM assigned_tasks WHERE id = %s"
    db.sql_execute(conn, sql, val) 
