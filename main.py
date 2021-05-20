import sys
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
def collection_options():
    print(
        " 0. Exit\n"
        " 1. Connection info\n",
        "2. Profiles\n",
        "3. Types\n",
        "4. Tasks\n",
        "5. Assigned Tasks\n",
    )

def crud_options():
    print(
        " 1. Show all\n",
        "2. Add new\n",
        "3. Edit\n",
        "4. Delete\n"
    )

def profile_update_options():
    print(
        " 1. Update name and surname\n",
        "2. Update password\n",
        "3. Grant active\n",
    )

def type_update_options():
    print(
        " 1. Update specication\n",
        "2. Update responsibilities\n",
        "3. Update color\n",
    )

def task_update_options():
    print(
        " 1. Update name and description\n",
        "2. Update attachment link\n",
        "3. Update priority\n",
    )

if __name__ == "__main__":
    welcome()  
    collection_options()
    
    operation = int(input("Enter collection name from list above: "))

    if operation == 1:
        db.connection_info(conn)

    
    ## Profiles ##   
    elif operation == 2:
        crud_options()
        choice = int(input("Enter name of operation for Profiles: "))

        if choice == 1:
            profile_man.show_all_profiles(conn)

        elif choice == 2:
            # example: Exaple data: Jan, Serce, janek_serce@yahoo.com, 45JanToJa, False
            new_record = input("Add new record pattern: name, surmame, email, password, is_active: ")
            profile_man.insert_profile(conn, tuple(new_record.split(",")))
        elif choice == 3:
            profile_update_options()
            update_option = int(input("Choose update option: "))
            
            ## Update ##
            if update_option == 1:
                changed_record = input("You change data: enter name, surname, id: ")
                profile_man.update_profile_name_and_surname(conn, tuple(changed_record.split(",")))
            elif update_option == 2:
                changed_record = input("You change data: password, id: ")
                profile_man.update_profile_password(conn, tuple(changed_record.split(",")))
            elif update_option == 3:
                id = input("Choose profile id: ")
                profile_man.grant_profile_active_status(conn, tuple(id, ))
            else:
                raise Exception("Unsupported operation")
            ## Update ##

        elif choice == 4:
            id = input("Enter user id: ")
            profile_man.delete_profile_for_id(conn, tuple(id, ))
        else:
            raise Exception("Unsupported operation")
    ## Profiles ##

    
    ## Types ##
    elif operation == 3:
        crud_options()
        choice = int(input("Enter name of operation for Types: "))

        if choice == 1:
            type_man.show_all_types(conn)

        elif choice == 2:
            # example: advance IT support, help solve hard problems, grey
            new_record = input("Add new record pattern: specification, responsibilities, color: ")
            type_man.insert_type(conn, tuple(new_record.split(",")))
        elif choice == 3:
            type_update_options()
            update_option = int(input("Choose update option: "))
            
            ## Update ##
            if update_option == 1:
                changed_record = input("You change data: enter specification, id: ")
                type_man.update_type_specication(conn, tuple(changed_record.split(",")))
            elif update_option == 2:
                changed_record = input("You change data: enter responsibilities, id: ")
                type_man.update_type_responsibilities(conn, tuple(changed_record.split(",")))
            elif update_option == 3:
                changed_record = input("You change data: enter color, id: ")
                type_man.update_type_color(conn, tuple(changed_record.split(",")))
            else:
                raise Exception("Unsupported operation")
            ## Update ##
        elif choice == 4:
            id = input("Enter type id: ")
            type_man.delete_type_for_id(conn, tuple(id, ))
        else:
            raise Exception("Unsupported operation")
    ## Types ##

    
    ## Tasks ##
    elif operation == 4:
        crud_options()
        choice = int(input("Enter name of operation for Tasks: "))

        if choice == 1:
            task_man.show_all_tasks(conn)
        elif choice == 2:
            # example: 2, Create new database on serwer #50", "copy and paste data", "NULL", 2
            new_record = input("Add new record pattern: type_id, name, description, attachment_link, priority: ")
            task_man.insert_task(conn, tuple(new_record.split(",")))
        elif choice == 3:
            task_update_options()
            update_option = int(input("Choose update option: "))
            
            ## Update ##
            if update_option == 1:
                changed_record = input("You change data: enter name, description, id: ")
                task_man.update_task_name_and_description(conn, tuple(new_record.split(",")))
            elif update_option == 2:
                changed_record = input("You change data: enter attachment link, id: ")
                task_man.update_task_attachment_link(conn, tuple(new_record.split(",")))
            elif update_option == 3:
                changed_record = input("You change data: enter priority, id: ")
                task_man.update_task_priority(conn, tuple(new_record.split(",")))
            else:
                raise Exception("Unsupported operation")
            ## Update ##
        elif choice == 4:
            id = input("Enter task id: ")
            task_man.delete_task_for_id(conn, tuple(id, ))
        else:
            raise Exception("Unsupported operation")
    ## Tasks ##

    
    ## Assigned tasks ##
    elif operation == 5:
        crud_options()
        choice = int(input("Enter name of operation for Assigned Tasks: "))

        if choice == 1:
            ass_task_man.show_assigned_tasks(conn)
        elif choice == 2:
            # example: 5, 3, "to do - 0% progress"
            new_record = input("Add new record pattern: profile_id, task_id, progress_details: ")
            ass_task_man.insert_assign_task(conn, tuple(new_record.split(",")))
        elif choice == 3:
            print("This haven't any update method.")
        elif choice == 4:
            id = input("Enter task id: ")
            ass_task_man.delete_assigned_task_for_id(conn, tuple(id, ))
        else:
            raise Exception("Unsupported operation")
    ## Assigned tasks ##

    elif operation == 0:
        sys.exit("You closed programme.")
    else:
        raise Exception("Unsupported operation")

    db.close_conn(conn)
    
    
    


