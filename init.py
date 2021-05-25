from utils import path_finder as path
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db
from data import _db_struct as struct_db

from controllers import profiles_controller as profile_man
from controllers import tasks_controller as task_man
from controllers import types_controller as type_man
from controllers import assigned_tasks_controller as ass_task_man
from controllers import all_data_controller as all_data_man

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)
create = "YES"

if __name__ == "__main__":
    db.sql_drop(conn, struct_db.sql_drop_tables)
    if(create == "YES"):

        ## Profiles ##
        db.sql_create(conn, struct_db.sql_create_profiles)
        profile_list = [
            ("Kamil", "Cecherz", "pangeon@tlen.pl", "123pass", True),
            ("Adam", "Wolniewicz", "wolnygosc@interia.pl", "passpass", False),
            ("Weronika", "Bławut", "wera_bla@op.pl", "Kocurek16", True),
            ("Agnieszka", "Lasota", "agnieszka.lasota1@gmail.com", "Laseczka", False),
            ("Radosław", "Ignasiak", "radekignasiak13@gmail.com", "radini+ola", True),
            ("Adam", "Kos", "kos.adam@wp.pl", "BralemHere10", True)
        ]
        for record in profile_list: profile_man.insert_profile(conn, record)
        ## Profiles ##


        ## Types ##
        db.sql_create(conn, struct_db.sql_create_types)
        types_list = [
            ("IT online support", "answers to customers' question and help solve problems", "yellow"),
            ("Server maintenance", "proactive infrastructure monitoring and prevention of potential problems", "red"),
            ("Database managment", "installation, configuration, database tuning using configuration management tools", "blue"),
            ("Backend dev", "Analysis, design and implementation of software on the server side", "green"),
            ("Graphic design", "Provide graphic design technical support using advanced computer applications.", "pink")
        ]
        for record in types_list: type_man.insert_type(conn, record)
        ## Types ##


        ## Tasks ##
        db.sql_create(conn, struct_db.sql_create_tasks)
        tasks_list = [
            (5, "New logo", "Create new black and white logo for company", "NULL", 3),
            (5, "New banner for coxi.io", "Create better baner for webpage resolution 1280x400", "https://gieldykryptowalut.pl/coxi-io-opinie/", 1),
            (4, "Repair payment gate", "Repair bugs for pay.coxi.io", "https://pay.coxi.io/payg/", 1),
            (3, "Backend", "Create serwer full backend and copy data to SSD 1TB", "NULL", 2),
            (2, "Drop database from old serwer #44", "Erase all data", "NULL", 3)
        ]
        for record in tasks_list: task_man.insert_task(conn, record)
        ## Tasks ##


        ## Assigned tasks ##
        db.sql_create(conn, struct_db.sql_create_assigned_tasks)
        assigned_tasks_list = [
            (1, 1, "to do - 0% progress"),
            (1, 2, "in progress - 70% progress"),
            (2, 2, "in progress - 50% progress only your part"),
            (3, 5, "end - ready to test"),
            (4, 3, "to do - 0% progress"),
            (4, 4, "to do - 0% progress"),
            (5, 5, "depracated")
        ]
        for record in assigned_tasks_list: ass_task_man.insert_assign_task(conn, record)
        ## Assigned tasks ##

