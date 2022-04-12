/*
drop table if exists person;
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');
*/

-- Write an SQL query to delete all the duplicate emails, keeping 
-- only one unique email with the smallest id.

-- Oracle, Postgres, MySql
delete from Person
 where id in (
     select id
       from (
            select id,
                   min(id) over (partition by email) min_id
            from Person
       ) p
       where id <> min_id
 )
 ;

-- Oracle, Postgres
delete from Person
 where id not in (
          select min(id) id
            from Person
           group by email
       )
 ;

-- MySQL - One more level of nesting
-- You can't specify target table 'Person' for update in FROM clause
delete from Person
 where id not in (
       select id from (
              select min(id) id
                from Person
               group by email
           ) p
       )
 ;
