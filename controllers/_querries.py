all_profiles = "SELECT * FROM profiles"
all_tasks = "SELECT * FROM tasks"
all_types = "SELECT DISTINCT * FROM types"
all_assigned_tasks = "SELECT * FROM assigned_tasks"

all_data_inspect = '''
SELECT assigned_tasks.id, profiles.email, types.specification, tasks.description, tasks.attachment_link, tasks.priority, assigned_tasks.progress_details, assigned_tasks.activation_date, assigned_tasks.expired_date  
FROM profiles, types, tasks, assigned_tasks 
WHERE profiles.id = assigned_tasks.profile_id 
AND assigned_tasks.task_id = tasks.id 
AND types.id = tasks.type_id;
'''
