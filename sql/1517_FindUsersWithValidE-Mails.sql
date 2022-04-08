/*
drop table If Exists Users;
Create table If Not Exists Users (user_id int, name varchar(30), mail varchar(50));
Truncate table Users;
insert into Users (user_id, name, mail) values ('1', 'Winston', 'winston@leetcode.com');
insert into Users (user_id, name, mail) values ('2', 'Jonathan', 'jonathanisgreat');
insert into Users (user_id, name, mail) values ('3', 'Annabelle', 'bella-@leetcode.com');
insert into Users (user_id, name, mail) values ('4', 'Sally', 'sally.come@leetcode.com');
insert into Users (user_id, name, mail) values ('5', 'Marwan', 'quarz#2020@leetcode.com');
insert into Users (user_id, name, mail) values ('6', 'David', 'david69@gmail.com');
insert into Users (user_id, name, mail) values ('7', 'Shapiro', '.shapo@leetcode.com');
insert into Users (user_id, name, mail) values ('8', 'Winston', 'winston@leetcode?com');
*/
-- Write an SQL query to find the users who have valid emails.
-- A valid e-mail has a prefix name and a domain where:
-- * The prefix name is a string that may contain letters (upper or lower case),
--   digits, underscore '_', period '.', and/or dash '-'. The prefix name must 
--   start with a letter.
-- * The domain is '@leetcode.com'.
-- Return the result table in any order.

-- Postgres
-- text ~ pattern: match POSIX regular expression
-- text ~ pattern: case insensitively match
-- text !~ pattern: not match
-- text !~* pattern: not case insensitively matc
select *
  from users
 where mail ~ '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'
 ;

-- Oracle
-- https://oracle-base.com/articles/misc/regular-expressions-support-in-oracle
select *
  from users
 where regexp_like(mail, '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$')
 ;

-- MySQL - the '\\' must be leet code issue
select *
  from users
 where regexp_like(mail, '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$')
 ;
