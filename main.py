from utils import path_finder as path
from utils.db_manager import mysql_connector as db
from data import _variables as app
from data import _db_config as cfg_db

from controllers import profiles_controller as profile_man
from controllers import tasks_controller as task_man
from controllers import types_controller as type_man
from controllers import assigned_tasks_controller as ass_task_man
from controllers import all_data_controller as all_data_man


def welcome():
    print("--- {}, ver {} ---\n".format(app.name, app.version))

conn = db.define_db(
    cfg_db.db_host, 
    cfg_db.db_name, 
    cfg_db.db_user, 
    cfg_db.db_pass
)

if __name__ == "__main__":
    welcome()  
    db.connection_info(conn)
    #profile_man.show_all_profiles(conn)
    all_data_man.inspect_all_data(conn)

    db.close_conn(conn)
    
    # show_all_profiles(conn)

    # show_all_tasks(conn)
    # show_all_types(conn)
    # show_assigned_tasks(conn)

    # sql = '''
    #     INSERT INTO Profiles (name, surname, email, password, is_active)
    #     VALUES ("Adam", "Kos", "kos.adam@wp.pl", "BralemHere10", True);
    # '''
    # profile.insert_profile(conn, ("Sebastian", "Zupa", "zupa@netflix.com", "#daszek", True))
    # insert_assign_task(conn, (10, 1, "TO DO"))
    # profile.update_profile_name_and_surname(conn, ("Sebastian", "Supa", 11))
    # profile.delete_profile_for_id(conn, (11, ))

    # inspect_all_data(conn)
    


