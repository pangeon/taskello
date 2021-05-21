from controllers import profiles_controller as profile_man
from data import _db_config as cfg_db
from utils.db_manager import mysql_connector as db

from utils import str_utils

from flask import Flask
app = Flask(__name__)

@app.route("/profiles")
def show_all_profiles():
    conn = db.define_db(
        cfg_db.db_host, 
        cfg_db.db_name, 
        cfg_db.db_user, 
        cfg_db.db_pass
    )

    profiles_records = profile_man.show_all_profiles(conn)
    start_html = "<!DOCTYPE html><html><head><title>Profiles</title></head><body>"
    body = ""

    for i in range(len(profiles_records)):
        record = "<tr><td>" + str_utils.tup_to_str(profiles_records[i]) + "</td></tr>"
        body += record
    
    table_html_records = "<table table style=\"width:100%\">" + body + "</table>"
    end_html = "</body></html>"
    web_page = start_html + table_html_records + end_html

    return web_page