-- Profiles --
INSERT INTO `profiles` (`id`, `name`, `surname`, `email`, `password`, `is_active`) VALUES
(1, 'Kamil', 'Cecherz', 'pangeon@tlen.pl', 'pbkdf2:sha256:260000$FhV9g1w7lWbjwUfe$36a06c967419dd9c11fb697bd0a76e929c287e36339ebd31c218447c7e427270', 1),
(2, 'Adam', 'Wolniewicz', 'wolnygosc@interia.pl', 'pbkdf2:sha256:260000$4uhKKcC4XS2cSRP2$ffb9af0cff0d246385e6b3d3ebe3f27c6ff228fa9ed9f2ca503b2709e8d306b2', 0),
(3, 'Weronika', 'Bławut', 'wera_bla@op.pl', 'pbkdf2:sha256:260000$Olsa92xHWfgocr1p$b3b306ece5ac578a7ee5898c5f514cbedcccacbe9f6e9b5e1f24457a428f2cd2', 1),
(4, 'Agnieszka', 'Lasota', 'agnieszka.lasota1@gmail.com', 'pbkdf2:sha256:260000$PSFZD6hqWy9jea0C$f1ef422229d9bbb56d0244cfda02fb42197a3145985b3c93ffe644f8a711b552', 0),
(5, 'Radosław', 'Ignasiak', 'radekignasiak13@gmail.com', 'pbkdf2:sha256:260000$emI9LuGeCyHJqtDd$809812fd9ff5182a88dcfc2b10853417205af72f350c03ff59a5fab22a46a191', 1),
(6, 'Adam', 'Kos', 'kos.adam@wp.pl', 'pbkdf2:sha256:260000$28wfkTWZcVwhZrQE$13760edd4e91020fd09f3fd641452dfccbd1c7d34ddcdf9a725a8711c3ea5018', 1);

-- Types --
INSERT INTO `types` (`id`, `specification`, `responsibilities`, `color`) VALUES
(1, 'IT online support', 'answers to customers question and help solve problems', 'yellow'),
(2, 'Server maintenance', 'proactive infrastructure monitoring and prevention of potential problems', 'red'),
(3, 'Database managment', 'installation, configuration, database tuning using configuration management tools', 'blue'),
(4, 'Backend dev', 'Analysis, design and implementation of software on the server side', 'green'),
(5, 'Graphic design', 'Provide graphic design technical support using advanced computer applications.', 'pink');

-- Tasks --
INSERT INTO `tasks` (`id`, `type_id`, `name`, `description`, `attachment_link`, `priority`) VALUES
(1, 5, 'New logo', 'Create new black and white logo for company', 'NULL', 3),
(2, 5, 'New banner for coxi.io', 'Create better baner for webpage resolution 1280x400', 'https://gieldykryptowalut.pl/coxi-io-opinie/', 1),
(3, 4, 'Repair payment gate', 'Repair bugs for pay.coxi.io', 'https://pay.coxi.io/payg/', 1),
(4, 3, 'Backend', 'Create serwer full backend and copy data to SSD 1TB', 'NULL', 2),
(5, 2, 'Drop database from old serwer #44', 'Erase all data', 'NULL', 3);

-- Assigned tasks --
INSERT INTO `assigned_tasks` (`id`, `profile_id`, `task_id`, `progress_details`, `activation_date`, `expired_date`) VALUES
(1, 1, 1, 'TO DO', '2022-12-06 19:59:40', '2021-01-17 19:00:00'),
(2, 1, 2, 'TO DO', '2022-12-06 19:59:40', '2021-09-11 16:00:00'),
(3, 4, 3, 'DONE', '2022-12-06 19:59:40', '2020-06-04 08:00:00'),
(4, 4, 4, 'DOING', '2022-12-06 19:59:40', '2021-10-05 08:00:00'),
(5, 5, 5, 'DONE', '2022-12-06 19:59:40', '2020-01-11 14:00:00');


