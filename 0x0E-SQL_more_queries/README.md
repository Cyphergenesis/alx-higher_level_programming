# 0x0E. SQL - More queries


### Resources
***Read or watch:***
* How To Create a New User and Grant Permissions in MySQL
* How To Use MySQL GRANT Statement To Grant Privileges To a User
* MySQL constraints
* SQL technique: subqueries
* Basic query operation: the join


### Requirements
***General***
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)

### Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```
