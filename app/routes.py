from app import app
from app import data_service_adapter as data
from app.forms import LoginForm
from app.forms import RegistrationForm

from flask import request, redirect, flash, session, url_for
from flask import render_template

from markupsafe import escape

from random import randint as gen



@app.route('/')
def index():
    return render_template('main.html')


## Utils
def __id_generator():
    return gen(0, 10000)

def __profile_id():
    e_mail = session.get('username', 'not set')
    profile_id = data.profile_id(val = (
        e_mail
    ))
    return profile_id
## Utils


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
            
    return render_template('profile/register.html',  title='Register', form=form)


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

    return render_template('profile/login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    return redirect(url_for('login'))
## Security ##


## Profiles ##
##! test only
@app.route("/admin/edit/profiles")
def show_all_profiles():
    profiles = list(data.all_profiles())
    return render_template('profile/profiles.html', title='Profiles list', profiles=profiles)
##! test only


##! deprecated
@app.route("/user/profile/<id>")
def show_profile(id):
    profiles = list(data.all_profiles())
    try:
        profile = profiles[int(escape(id))]
        return render_template('profile/profile.html', title='Profile account', profile=profile) 
    except IndexError as e:
        return app.send_static_file("errors/error.html")
##! deprecated


@app.route("/user/show/profile")
def show_login_profile():
    try:
        profile = data.email(session.get('username', 'not set'))
        return render_template('profile/profile.html', title='Profile account', profile=profile) 
    except IndexError as e:
        return app.send_static_file("errors/error.html")


@app.route("/user/edit/profile/name_surname", methods=['POST', 'GET'])
def edit_profile():
    if request.method == "POST":
        name = request.form['profile_name']
        surname = request.form['profile_surname']
        e_mail = session.get('username', 'not set')

        data.edit_profile_data(
            val = (
                name,
                surname,
                e_mail
            )
        )
        return redirect('/')
    else:
        return render_template('profile/edit_profile_data.html', title='Edit Profile data')


@app.route("/user/edit/profile/pass", methods=['POST', 'GET'])
def edit_profile_password():
    if request.method == "POST":
        pass_1 = request.form['profile_password']
        pass_2 = request.form['profile_password_repeat']
        e_mail = session.get('username', 'not set')
        if pass_1 == pass_2:
            data.edit_profile_pass(
                val = (
                    pass_1,
                    e_mail
                )
            )
        else:
            msg = "Passwords do not match"
            return render_template('profile/edit_profile_pass.html', title='Edit Profile password', msg=msg)
        return redirect('/')
    else:
        return render_template('profile/edit_profile_pass.html', title='Edit Profile password')


@app.route("/user/remove/profile")
def remove_profile():
    e_mail = session.get('username', 'not set')
    data.remove(
        val = (
            e_mail
        )
    )
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/')
## Profiles ##


## Types ##
##! test only
@app.route("/admin/edit/types")
def show_all_types():    
    types = list(data.all_types())
    return render_template('category/types.html', title='Types of Tasks', types=types)
##! test only

@app.route("/user/edit/add_category", methods=['POST', 'GET'])
def add_category():
    if request.method == "POST":
        specification = request.form['type_specification']
        responsibilities = request.form['type_responsibilities']
        color = request.form['type_color']

        data.insert_type( 
            val = (
                specification,
                responsibilities,
                color
            )
        )
        return redirect('/')
    else:
        return render_template('category/add_type.html', title='Add new category')
## Types ##


## Tasks
@app.route("/user/show/tasks")
def show_profile_tasks():
    e_mail = session.get('username', 'not set')
    tasks = list(data.user_tasks(
        val = (
            e_mail
        )
    ))
    return render_template('task/tasks.html', title='Your task list', tasks=tasks)


@app.route("/user/edit/add_task", methods=['POST', 'GET'])
def add_task():
    if request.method == "POST":
        task_id = __id_generator()
        task_type_id = request.form['task_type_id']
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        task_attachment_link = request.form['task_attachment_link']
        task_priority = request.form['task_priority']

        data.insert_task(
            val = (
                task_id,
                task_type_id, 
                task_name, 
                task_description,
                task_attachment_link,
                task_priority
            )
        )
        data.assign_task(val = (
            __profile_id(),
            task_id,
            "TO DO"
        ))
        return redirect("/")
    else:
        task_type_list = data.all_types()
        return render_template('task/add_task.html', title='Add new task', task_type_list=task_type_list)
## Tasks




## Assignment tasks and details
@app.route("/show/all_tasks")
def show_all_tasks_details():
    task_details = list(data.all_tasks_details())
    return render_template('task/tasks_details.html', title='Tasks table', tasks_details=task_details)
## Assignment tasks and details