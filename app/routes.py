from app import app
from app import data_service_adapter as data
from app.forms import LoginForm
from app.forms import RegistrationForm

from flask import request, redirect, flash, session, url_for
from flask import render_template

from markupsafe import escape


@app.route('/')
def index():
    return render_template('main.html')


## Security ##
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        if request.method == 'POST' and 'e_mail' in request.form and 'password' in request.form:
            e_mail = request.form['e_mail']
            password = request.form['password']
            data.registry(
                val = (
                    e_mail,
                    password
                )
            )
        return redirect(url_for('login'))
            
    return render_template('register.html',  title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if request.method == 'POST' and 'e_mail' in request.form and 'password' in request.form:
            e_mail = request.form['e_mail']
            password = request.form['password']
            profile = data.login(
                val = (
                    e_mail,
                    password
                )
            )
            if profile == None:
                return render_template('error.html')
            else:
                session['loggedin'] = True
                session['id'] = profile[0]
                session['username'] = profile[3]
                return render_template('main.html')

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))
## Security ##


## Profiles ##
@app.route("/admin/edit/profiles")
def show_all_profiles():
    profiles = list(data.all_profiles())
    return render_template('profiles.html', title='Profiles list', profiles=profiles)

##! deprecated
@app.route("/user/profile/<id>")
def show_profile(id):
    profiles = list(data.all_profiles())
    try:
        profile = profiles[int(escape(id))]
        return render_template('profile.html', title='Profile account', profile=profile) 
    except IndexError as e:
        return app.send_static_file("errors/error.html")
##! deprecated

@app.route("/account/profile")
def show_login_profile():
    
    try:
        profile = data.email(session.get('username', 'not set'))
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
        return render_template('main.html')
    else:    
        return render_template('add_task.html', title='Add new task')
## Tasks


## Assignment tasks and details
@app.route("/user/all/tasks/table")
def show_all_tasks_details():
    task_details = list(data.all_tasks_details())
    return render_template('tasks_details.html', title='Tasks table', tasks_details=task_details)
## Assignment tasks and details