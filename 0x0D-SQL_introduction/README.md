# 0x0D. SQL - Introduction
+ Weight: 1


## Concepts
***For this project, we expect you to look at these concepts:***
+ Databases

## Resources
***Read or watch:***
+ What is Database & SQL?
+ A Basic MySQL Tutorial
+ Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
+ Basic queries: SQL and RA


### General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL


### Requirements
***General***
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)

#### Comments for your SQL file
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
#### Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```












