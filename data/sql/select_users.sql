SELECT profiles.email, types.specification, tasks.description, assigned_tasks.profile_id 
FROM profiles, types, tasks, assigned_tasks 
WHERE profiles.id = assigned_tasks.profile_id 
AND assigned_tasks.task_id = tasks.id 
AND types.id = tasks.type_id;