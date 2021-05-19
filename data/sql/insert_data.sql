-- Profiles --
INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Kamil", "Cecherz", "pangeon@tlen.pl", "123pass", True);

INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Adam", "Wolniewicz", "wolnygosc@interia.pl", "passpass", False);

INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Weronika", "Bławut", "wera_bla@op.pl", "Kocurek16", True);

INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Agnieszka", "Lasota", "agnieszka.lasota1@gmail.com", "Laseczka", False);

INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Radosław", "Ignasiak", "radekignasiak13@gmail.com", "radini+ola", True);

INSERT INTO Profiles (name, surname, email, password, is_active)
VALUES ("Adam", "Kos", "kos.adam@wp.pl", "BralemHere10", True);

-- Types --
INSERT INTO Types (specification, responsibilities, color)
VALUES ("IT online support", "answers to customers' question and help solve problems", "yellow");

INSERT INTO Types (specification, responsibilities, color)
VALUES ("Server maintenance", "proactive infrastructure monitoring and prevention of potential problems", "red");

INSERT INTO Types (specification, responsibilities, color)
VALUES ("Database managment", "installation, configuration, database tuning using configuration management tools", "blue");

INSERT INTO Types (specification, responsibilities, color)
VALUES ("Backend dev", "Analysis, design and implementation of software on the server side", "green");

INSERT INTO Types (specification, responsibilities, color)
VALUES ("Graphic design", "Provide graphic design technical support using advanced computer applications.", "pink");

-- Tasks --
INSERT INTO Tasks (type_id, name, description, attachment_link, priority)
VALUES(5, "New logo", "Create new black and white logo for company", NULL, 3);

INSERT INTO Tasks (type_id, name, description, attachment_link, priority)
VALUES(5, "New banner for coxi.io", "Create better baner for webpage resolution 1280x400", "https://gieldykryptowalut.pl/coxi-io-opinie/", 1);

INSERT INTO Tasks (type_id, name, description, attachment_link, priority)
VALUES(4, "Repair payment gate", "Repair bugs for pay.coxi.io", "https://pay.coxi.io/payg/", 1);

INSERT INTO Tasks (type_id, name, description, attachment_link, priority)
VALUES(3, "Backend", "Create serwer full backend and copy data to SSD 1TB", NULL, 2);

INSERT INTO Tasks (type_id, name, description, attachment_link, priority)
VALUES(2, "Drop database from old serwer #44", "Erase all data", NULL, 3);

-- Assigned tasks --
INSERT INTO Assigned_tasks (profile_id, task_id, progress_details)
VALUES(1, 1, "to do - 0% progress");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details, expired_date)
VALUES(1, 2, "in progress - 70% progress", "2021-05-18 16:20:00");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details, expired_date)
VALUES(2, 2, "in progress - 50% progress only your part", "2021-05-18 16:20:00");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details, expired_date)
VALUES(3, 5, "end - ready to test", "2021-05-22 13:00:00");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details)
VALUES(4, 3, "to do - 0% progress", "2021-05-22 13:00:00");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details)
VALUES(4, 4, "to do - 0% progress");

INSERT INTO Assigned_tasks (profile_id, task_id, progress_details)
VALUES(5, 5, "depracated");

