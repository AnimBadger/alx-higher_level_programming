-- convert whole database to UTF-8

USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mm4 COLLATE utf8mm4_unicode_ci;