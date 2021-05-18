from utils import path_finder as path
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db


def welcome():
    print("--- {}, ver {} ---\n".format(app.name, app.version))

if __name__ == "__main__":
    welcome()

    db.connect_to_db(
        cfg_db.db_host, 
        cfg_db.db_name, 
        cfg_db.db_user, 
        cfg_db.db_pass
    )
