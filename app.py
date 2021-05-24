from controllers import profiles_controller as profile_man
from controllers import types_controller as type_man
from controllers import tasks_controller as task_man
from controllers import all_data_controller as all_data_man

from data import _db_config as cfg_db
from utils.db_manager import mysql_connector as db
from markupsafe import escape

from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)
@app.route('/')
def index():
    return app.send_static_file("index.html")


## Profiles ##
@app.route("/admin/edit/profiles")
def show_all_profiles():
    profiles = list(profile_man.show_all_profiles(conn))
    return render_template('profiles.html', title='Profiles list', profiles=profiles)


@app.route("/user/profile/<id>")
def show_profile(id):
    profiles = list(profile_man.show_all_profiles(conn))
    try:
        profile = profiles[int(escape(id))]
        print(profile)
        return render_template('profile.html', title='Profile account', profile=profile) 
    except IndexError as e:
        return app.send_static_file("errors/error.html")
## Profiles ##


## Types ##
@app.route("/admin/edit/types")
def show_all_types():    
    types = list(type_man.show_all_types(conn))
    return render_template('types.html', title='Types of Tasks', types=types)
## Types ##


## Tasks
@app.route("/user/all/tasks")
def show_all_tasks():
    tasks = list(task_man.show_all_tasks(conn))
    return render_template('tasks.html', title='List of all Tasks', tasks=tasks)
## Tasks


## Assignment tasks and details
@app.route("/user/all/tasks/table")
def show_all_tasks_details():
    task_details = list(all_data_man.show_task_full_details(conn))
    return render_template('tasks_details.html', title='Tasks table', tasks_details=task_details)
## Assignment tasks and details