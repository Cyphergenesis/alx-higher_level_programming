--Converts the entire database htbn_0c_0 to UTF8.
USE `htbn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
