all_profiles = "SELECT * FROM Profiles"
all_tasks = "SELECT * FROM Tasks"
all_types = "SELECT * FROM Types"
all_assigned_tasks = "SELECT * FROM Assigned_tasks"

all_data_inspect = '''
SELECT Profiles.email, Types.specification, Tasks.description, Assigned_tasks.profile_id 
FROM Profiles, Types, Tasks, Assigned_tasks 
WHERE Profiles.id = Assigned_tasks.profile_id 
AND Assigned_tasks.task_id = Tasks.id 
AND Types.id = Tasks.type_id;
'''