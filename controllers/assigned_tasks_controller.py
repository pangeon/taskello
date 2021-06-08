from controllers import _querries as sql_select
from utils.db_manager import mysql_connector as db

def show_assigned_tasks(conn):
    assigned_tasks = db.sql_querry(conn, sql_select.all_assigned_tasks)
    return assigned_task


def insert_assign_task(conn, val):
    sql = "INSERT INTO assigned_tasks (profile_id, task_id, progress_details, expired_date) VALUES (%s, %s, %s, %s)"
    db.sql_execute(conn, sql, val)


def delete_assigned_task_for_id(conn, val):
    sql = "DELETE FROM assigned_tasks WHERE id = %s"
    db.sql_execute(conn, sql, val) 
