from app import app
from app import data_service_adapter as data

from flask import request, redirect
from flask import render_template
from markupsafe import escape


@app.route('/')
def index():
    return app.send_static_file("index.html")


## Profiles ##
@app.route("/admin/edit/profiles")
def show_all_profiles():
    profiles = list(data.all_profiles())
    return render_template('profiles.html', title='Profiles list', profiles=profiles)


@app.route("/user/profile/<id>")
def show_profile(id):
    profiles = list(data.all_profiles())
    try:
        profile = profiles[int(escape(id))]
        return render_template('profile.html', title='Profile account', profile=profile) 
    except IndexError as e:
        return app.send_static_file("errors/error.html")
## Profiles ##


## Types ##
@app.route("/admin/edit/types")
def show_all_types():    
    types = list(data.all_types())
    return render_template('types.html', title='Types of Tasks', types=types)
## Types ##


## Tasks
@app.route("/user/all/tasks")
def show_all_tasks():
    tasks = list(data.all_tasks())
    return render_template('tasks.html', title='Your task list', tasks=tasks)


@app.route("/user/edit/add_task", methods=['POST', 'GET'])
def add_task():
    if request.method == "POST":
        task_type_id = request.form['task_type_id']
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        task_attachment_link = request.form['task_attachment_link']
        task_priority = request.form['task_priority']

        data.insert_task(
            val = (
                task_type_id, 
                task_name, 
                task_description,
                task_attachment_link,
                task_priority
            )
        )
        return redirect('/')
    else:    
        return render_template('add_task.html')
## Tasks


## Assignment tasks and details
@app.route("/user/all/tasks/table")
def show_all_tasks_details():
    task_details = list(data.all_tasks_details())
    return render_template('tasks_details.html', title='Tasks table', tasks_details=task_details)
## Assignment tasks and details