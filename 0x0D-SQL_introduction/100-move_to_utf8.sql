-- converts `hbtn_0c_0` database to UTF-8 in MySQL sevrer.
USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
