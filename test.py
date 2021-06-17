from utils import path_finder as path
from utils import str_utils
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db

from controllers import profiles_controller as profile_man
from controllers import tasks_controller as task_man
from controllers import types_controller as type_man
from controllers import assigned_tasks_controller as ass_task_man
from controllers import all_data_controller as all_data_man
from utils.security import hash_password

from utils.security.hash_password import HashPassword

import itertools

def welcome():
    print("--- {}, ver {} ---\n".format(app.name, app.version))

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)

if __name__ == "__main__":
    # profile_pass = profile_man.get_profile_password(conn, "crazy@vp.pl")
    # print(profile_pass)

    # profile = profile_man.login_profile(conn, val = (
    #     "roman@tlen.pl",
    #     profile_pass
    # ))
    # print(profile)
    password = input("Enter password: ") 
    hash = HashPassword(password)
    hash.generate()
    print(hash.hash)
    # hash.hash = profile_pass
    # print(hash.hash)

    # print(hash.check('Alfaromeo88a#'))
