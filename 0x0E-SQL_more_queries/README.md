# alx-higher_level_programming
![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)
## 0x0E-SQL_more_queries
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…ff2a809cd94ac36348a38cf3e653091dcfa2cc3a68f8d54aa)

### General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a ```PRIMARY KEY```
* What’s a ```FOREIGN KEY```
* How to use ```NOT NULL``` and ```UNIQUE``` constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are ```JOIN``` and ```UNION```
### SQL Introduction
Each file in this repository holds code that illustrates an essential concept of programming, specific to the SQL programming language (Structured Query Language).
eg
### Tasks
Write a script that lists all privileges of the MySQL users ```user_0d_1``` and ```user_0d_2``` your server (in ```localhost)```
```
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'              
guillaume@ubuntu:~/$ 
```

## Author
## [Mugabi Joseph](https://twitter.com/joseph_mugabi)


