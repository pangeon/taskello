-- Profiles --
CREATE TABLE `dian_db`.`profiles` ( 
    `id` INT NOT NULL AUTO_INCREMENT, 
    `name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL , 
    `surname` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL , 
    `email` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL , 
    `password` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL , 
    `is_active` BOOLEAN NULL DEFAULT NULL , 
    PRIMARY KEY (`id`), 
    UNIQUE (`email`)
) ENGINE = InnoDB; 


-- Types --
CREATE TABLE `dian_db`.`types` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `specification` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL , 
    `responsibilities` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL , 
    `color` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL , 
    PRIMARY KEY (`id`),
    UNIQUE (`specification`)
) ENGINE = InnoDB; 


-- Tasks --
CREATE TABLE `dian_db`.`tasks` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `type_id` INT NOT NULL , 
    `name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL , 
    `description` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL , 
    `attachment_link` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL , 
    `priority` SMALLINT DEFAULT NULL , 
    PRIMARY KEY (`id`) ,
    FOREIGN KEY (`type_id`) REFERENCES Types(`id`) ,
    UNIQUE (`name`)
) ENGINE = InnoDB; 


-- Assigned tasks --
CREATE TABLE `dian_db`.`assigned_tasks` ( 
    `id` INT NOT NULL AUTO_INCREMENT , 
    `profile_id` INT NOT NULL , 
    `task_id` INT NOT NULL UNIQUE,
    `progress_details` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL ,
    `activation_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , 
    `expired_date` TIMESTAMP NULL DEFAULT NULL , 
    FOREIGN KEY (`profile_id`) REFERENCES Profiles(`id`) ,
    FOREIGN KEY (`task_id`) REFERENCES Tasks(`id`) ,
    PRIMARY KEY (`id`),
    UNIQUE (`task_id`)
) ENGINE = InnoDB;