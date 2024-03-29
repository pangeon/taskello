from app import app
from app import data_service_adapter as data
from app.forms import LoginForm, PL_LoginForm, PL_RegistrationForm
from app.forms import RegistrationForm

from flask import request, redirect, session, url_for
from flask import render_template

from random import randint as gen

from utils.security.hash_password import HashPassword

lang = "PL"

@app.route('/')
def index():
    return render_template('main.html', lang=lang)


################################# UTILS ##############################################
######################################################################################

def __id_generator():
    return gen(0, 10000)


def __profile_id():
    e_mail = session.get('username', None)
    profile_id = data.profile_id(val = (
        e_mail
    ))
    return profile_id


def __session_invalidate():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)


def __task_dashboard_for_user(login_user_name):
    return render_template(
        'task/tasks.html', 
        title='Your task list', 
        tasks=list(data.user_tasks(login_user_name)),
        lang=lang
    ) 

def __generate_hash_password(password):
    hash_password = HashPassword(password)
    hash_password.generate()
    
    return hash_password.hash

def __template_error(info_for_user):
    return render_template(
        'error.html', 
        msg = info_for_user
    )

#################################### SECURITY ########################################
######################################################################################

@app.route('/register', methods=['GET', 'POST'])
def register():
    if lang == "ENG":
        form = RegistrationForm()
    elif lang == "PL":
        form = PL_RegistrationForm()
    else:
        raise Exception("Language is not support")
    

    if form.validate_on_submit():
        if request.method == 'POST' and 'e_mail' in request.form and 'password' in request.form:
            e_mail = request.form['e_mail']
            password = request.form['password']

            if not data.is_email_exist(e_mail):
                data.registry(
                    val = (
                        e_mail,
                        __generate_hash_password(password)
                    )
                )
            else:
                if lang == "ENG":
                    return __template_error("A profile with the indicated e-mail already exists.")
                elif lang == "PL":
                    return __template_error("Profil o wskazanym adresie e-mail już istnieje.")
                else:
                    raise Exception("Language is not support")

        return redirect(url_for('login'))
    return render_template(
        'profile/register.html', 
        title = 'Register', 
        form = form,
        lang = lang
    )

######################################################################################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if lang == "ENG":
        form = LoginForm()
    elif lang == "PL":
        form = PL_LoginForm()
    else:
        raise Exception("Language is not support")
    
    if form.validate_on_submit():
        if request.method == 'POST' and 'e_mail' in request.form and 'password' in request.form:
            e_mail = request.form['e_mail']
            password = request.form['password']

            hash_password = HashPassword()
            hash_password.hash = data.profile_pass(e_mail)
            
            if hash_password.check(password):
                profile = data.login(
                    val = (
                        e_mail,
                        data.profile_pass(e_mail)
                    )
                )
            else:
                profile = None

            if profile == None:
                if lang == "ENG":
                    return __template_error("Password and login do not match.")
                elif lang == "PL":
                    return __template_error("Hasło i login nie pasują do siebie")
                else:
                    raise Exception("Language is not support")
            else:
                session['loggedin'] = True
                session['id'] = profile[0]
                session['username'] = profile[3]
                return render_template('main.html', lang=lang)
    return render_template(
        'profile/login.html', 
        title = 'Sign In', 
        form = form,
        lang=lang
    )

######################################################################################

@app.route('/logout')
def logout():
    __session_invalidate()
    return redirect(url_for('login'))


###################################### PROFILES ######################################
######################################################################################

##! test only
@app.route("/admin/edit/profiles")
def show_all_profiles():
    return render_template(
        'profile/profiles.html', 
        title = 'Profiles list', 
        profiles = list(data.all_profiles()),
        lang = lang
    )
##! test only

######################################################################################

@app.route("/user/show/profile")
def show_login_profile():
    try:
        if session.get('username', None):
            return render_template(
                'profile/profile.html', 
                title = 'Profile account', 
                profile = data.email(session.get('username', None)),
                lang = lang
            )
        else:
            return redirect(url_for('login'))
    except IndexError as e:
        return app.send_static_file("errors/error.html")

######################################################################################

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
        return redirect(url_for('show_login_profile'))
    else:
        if session.get('username', None):
            return render_template(
                'profile/edit_profile_data.html', 
                title = 'Edit Profile data',
                lang = lang
            )
        else:
            return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/profile/pass", methods = ['POST', 'GET'])
def edit_profile_password():
    if request.method == "POST":
        pass_1 = request.form['profile_password']
        pass_2 = request.form['profile_password_repeat']
        e_mail = session.get('username', 'not set')
        if pass_1 == pass_2:
            data.edit_profile_pass(
                val = (
                    __generate_hash_password(pass_1),
                    e_mail
                )
            )
        else:
            msg = "Passwords do not match"
            return render_template(
                'profile/edit_profile_pass.html', 
                title = 'Edit Profile password', 
                msg = msg
            )
        return redirect(url_for('show_login_profile'))
    else:
        if session.get('username', None):
            return render_template(
                'profile/edit_profile_pass.html', 
                title = 'Edit Profile password',
                lang = lang
            )
        else:
            return redirect(url_for('login'))

######################################################################################

@app.route("/user/remove/profile")
def remove_profile():
    e_mail = session.get('username', 'not set')
    data.remove(
        val = (
            e_mail
        )
    )
    __session_invalidate()
    return redirect('/')


###################################### TYPES #########################################
######################################################################################

@app.route("/user/show/types")
def show_all_types():
    if session.get('username', None):    
        return render_template(
            'category/types.html', 
            title = 'Types of Tasks', 
            types = list(data.all_types()),
            lang = lang
        )
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/add_type", methods=['POST', 'GET'])
def add_category():
    if request.method == "POST":
        data.insert_type( 
            val = (
                request.form['type_specification'],
                request.form['type_responsibilities'],
                request.form['type_color']
            )
        )
        return redirect(url_for('show_all_types'))
    else:
        return render_template(
            'category/add_type.html', 
            title='Add new category',
            lang = lang
        )

######################################################################################

@app.route("/user/edit/type/<int:type_id>", methods=['POST', 'GET'])
def edit_type(type_id):
    if session.get('username', None):
        if request.method == "POST":
            data.edit_type(
                val = (
                    request.form['type_specification'],
                    request.form['type_responsibilities'],
                    request.form['type_color'],
                    type_id
                )
            )
            return redirect(url_for('show_all_types'))
        else:
            return render_template(
                'category/edit_type.html', 
                title = 'Edit category', 
                type_item = list(data.show_type(type_id)),
                lang = lang
            )
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/remove/type/<int:type_id>")
def remove_type(type_id):
    if session.get('username', None):
        data.delete_type(type_id)
        return redirect(url_for('show_all_types'))
    else:
        return redirect(url_for('login'))


##################################### TASKS ##########################################
######################################################################################

@app.route("/user/show/tasks")
def show_profile_tasks():
    e_mail = session.get('username', None)
    if session.get('username', None): 
        return __task_dashboard_for_user(e_mail)
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/add_task", methods=['POST', 'GET'])
def add_task():
    if request.method == "POST":
        task_id = __id_generator()
        
        data.insert_task(
            val = (
                task_id,
                request.form['task_type_id'],
                request.form['task_name'],
                request.form['task_description'],
                request.form['task_attachment_link'],
                request.form['task_priority']
            )
        )
        print(request.form['task_expired_date'] + "T" + request.form['task_expired_time'])
        data.assign_task(
            val = (
                __profile_id(),
                task_id,
                request.form['task_progress_status'],
                request.form['task_expired_date'] + "T" + request.form['task_expired_time']
            )
        )
        return redirect("/")
    else:
        if session.get('username', None): 
            return render_template(
                'task/add_task.html', 
                title='Add new task', 
                task_type_list=data.all_types(),
                lang = lang
            )
        else:
            return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/task/progress/<int:task_id>")
def set_progress_done(task_id):
    e_mail = session.get('username', None)
    if e_mail:
        progress_details_to_change = data.show_ass_task(task_id)[3]
        progress_details_to_change = "DONE"

        data.task_progress_details(val = (
            progress_details_to_change,
            task_id
        ))
        return __task_dashboard_for_user(e_mail)
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/task/priority/<int:task_id>/<int:operation>")
def change_task_priority(task_id, operation):
    
    e_mail = session.get('username', None)

    if e_mail:
        task_priority_to_change = data.show_task(task_id)[5]
        if task_priority_to_change > 1 and operation == 0: 
            task_priority_to_change -= 1
        if task_priority_to_change < 6 and operation == 1: 
            task_priority_to_change += 1

        data.task_priority(val = (
            task_priority_to_change,
            task_id
        ))
        return __task_dashboard_for_user(e_mail)
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/task/name_description/<int:task_id>", methods=['POST', 'GET'])
def change_task_name_and_description(task_id):

    e_mail = session.get('username', None)

    if e_mail:
        
        if request.method == "POST":
            data.task_name_and_description(
                val = (
                    request.form['task_name'],
                    request.form['task_description'],
                    task_id
                )
            )
            return __task_dashboard_for_user(e_mail)
        else:
            tasks_properties = [
                data.show_task(task_id)[2],
                data.show_task(task_id)[3]
            ]
            return render_template(
                'task/edit_task.html',
                title="Edit task properties",
                tasks_properties = tasks_properties,
                lang = lang
            )
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/task/attachment-link/<int:task_id>", methods=['POST', 'GET'])
def change_attachment_link(task_id):

    e_mail = session.get('username', None)

    if e_mail:
        if request.method == "POST":
            data.task_attachment_link(
                val = (
                    request.form['task_attachment_link'],
                    task_id
                )
            )
            return __task_dashboard_for_user(e_mail)
        else:
            return render_template(
                'task/edit_task_link.html',
                title="Edit task link",
                task_attachment_link = data.show_task(task_id)[4],
                lang = lang
            )
    else:
        return redirect(url_for('login'))

######################################################################################

@app.route("/user/edit/task/expired-time/<int:task_id>", methods=['POST', 'GET'])
def change_expired_time(task_id):

    e_mail = session.get('username', None)

    if e_mail:
        if request.method == "POST":
            data.task_expired_time(
                val = (
                    request.form['task_expired_date'] + "T" + request.form['task_expired_time'],
                    task_id
                )
            )
            return __task_dashboard_for_user(e_mail)
        else:

            return render_template(
                'task/edit_task_expired_date.html',
                title="Edit task time",
                task_expired_time = data.show_task(task_id)[5],
                lang = lang
            )
    else:
        return redirect(url_for('login'))

######################################################################################


@app.route("/user/remove/task/<int:task_id>")
def remove_task(task_id):
    e_mail = session.get('username', None)

    if e_mail:
        data.delete_task(task_id)
        return __task_dashboard_for_user(e_mail)
    else:
        return redirect(url_for('login'))


######################## ASSIGNMENT TASKS AND DETAILS ################################
######################################################################################

@app.route("/show/all_tasks")
def show_all_tasks_details():
    return render_template(
        'task/tasks_details.html', 
        title='Tasks table', 
        tasks_details=list(data.all_tasks_details()),
        lang = lang
    )

######################################################################################
