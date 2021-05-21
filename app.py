from controllers import profiles_controller as profile_man
from controllers import types_controller as type_man

from data import _db_config as cfg_db
from utils.db_manager import mysql_connector as db
from markupsafe import escape

from utils import str_utils
from flask import Flask, request
from flask import render_template

app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')

conn = db.define_db(
        cfg_db.db_host, 
        cfg_db.db_name, 
        cfg_db.db_user, 
        cfg_db.db_pass
)
start_html = "<!DOCTYPE html><html><head><title>Profiles</title><link rel=\"stylesheet\" type=\"text/css\" href=\"/css/main.css\" /></head><body>"
end_html = "</body></html>"

profiles_records = profile_man.show_all_profiles(conn)

@app.route('/')
def index():
    return app.send_static_file("index.html")


## Profiles ##
@app.route("/profiles")
def show_all_profiles():
    body = ""

    for i in range(len(profiles_records)):
        record = "<tr><td>" + str_utils.tup_to_str(profiles_records[i]) + "</td></tr>"
        body += record
    
    table_html_records = "<table table style=\"width:100%\">" + body + "</table>"
    web_page = start_html + table_html_records + end_html

    return web_page


@app.route("/profile/<id>")
def show_profile(id):
    body = ""
    try:
        record = "<tr><td>" + str_utils.tup_to_str(profiles_records[int(escape(id))]) + "</td></tr>"
        body += record
        
        table_html_records = "<table table style=\"width:100%\">" + body + "</table>"
        web_page = start_html + table_html_records + end_html

        return web_page
    except IndexError as e:
        body = "<h1>Profile with indicated number doesn't exist<h1>"
        return start_html + body + end_html 
## Profiles ##


## Types ##
@app.route("/types")
def show_all_types():    
    types = list(type_man.show_all_types(conn))
    #out = [item for t in types for item in t]
    
    out = map(list, zip(*types))
    print(out)
    return render_template('types.html', title='Types of Tasks', types=out)
## Types ##