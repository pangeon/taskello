from utils.db_manager import mysql_connector as db
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
    if(create == "YES"):

        ## Profiles ##
        db.sql_create(conn, struct_db.sql_create_profiles)
        profile_list = [
            ("Kamil", "Cecherz", "pangeon@tlen.pl", "pbkdf2:sha256:260000$FhV9g1w7lWbjwUfe$36a06c967419dd9c11fb697bd0a76e929c287e36339ebd31c218447c7e427270", True), 
            # 123pass
            ("Adam", "Wolniewicz", "wolnygosc@interia.pl", "pbkdf2:sha256:260000$4uhKKcC4XS2cSRP2$ffb9af0cff0d246385e6b3d3ebe3f27c6ff228fa9ed9f2ca503b2709e8d306b2", False),
            # passpass
            ("Weronika", "Bławut", "wera_bla@op.pl", "pbkdf2:sha256:260000$Olsa92xHWfgocr1p$b3b306ece5ac578a7ee5898c5f514cbedcccacbe9f6e9b5e1f24457a428f2cd2", True),
            # Kocurek16
            ("Agnieszka", "Lasota", "agnieszka.lasota1@gmail.com", "pbkdf2:sha256:260000$PSFZD6hqWy9jea0C$f1ef422229d9bbb56d0244cfda02fb42197a3145985b3c93ffe644f8a711b552", False),
            # Laseczka
            ("Radosław", "Ignasiak", "radekignasiak13@gmail.com", "pbkdf2:sha256:260000$emI9LuGeCyHJqtDd$809812fd9ff5182a88dcfc2b10853417205af72f350c03ff59a5fab22a46a191", True),
            # radini+ola
            ("Adam", "Kos", "kos.adam@wp.pl", "pbkdf2:sha256:260000$28wfkTWZcVwhZrQE$13760edd4e91020fd09f3fd641452dfccbd1c7d34ddcdf9a725a8711c3ea5018", True)
            # BralemHere10
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
            (1, 1, "TO DO", '2021-01-17T20:00'),
            (1, 2, "TO DO", '2021-09-11T18:00'),
            (4, 3, "DONE", '2020-06-04T10:00'),
            (4, 4, "DOING", '2021-10-05T10:00'),
            (5, 5, "DONE", '2020-01-11T15:00')
        ]
        for record in assigned_tasks_list: ass_task_man.insert_assign_task(conn, record)
        ## Assigned tasks ##
    
    else:
        db.sql_drop(conn, struct_db.sql_drop_tables)

