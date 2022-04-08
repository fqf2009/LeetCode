/*
drop table if exists Student;
Create table If Not Exists Student (name varchar(50), continent varchar(7));
Truncate table Student;
insert into Student (name, continent) values ('Jane', 'America');
insert into Student (name, continent) values ('Pascal', 'Europe');
insert into Student (name, continent) values ('Xi', 'Asia');
insert into Student (name, continent) values ('Jack', 'America');
-- Test case 2: only two continents
Truncate table Student;
insert into Student (name, continent) values ('Parto', 'Europe');
insert into Student (name, continent) values ('Tzvetan', 'America');
*/

-- A school has students from Asia, Europe, and America.

-- Write an SQL query to pivot the continent column in the Student table so that 
-- each name is sorted alphabetically and displayed underneath its corresponding 
-- continent. The output headers should be America, Asia, and Europe, respectively.

-- The test cases are generated so that the student number from America is not 
-- less than either Asia or Europe.

-- Postgres, Oracle
-- full join works even if student number from America is less than from other continents
select a.name America, 
       b.name Asia, 
       c.name Europe
  from (
        select name,
               row_number() over(order by  name) rn1
          from student
         where continent = 'America'
       ) a
  full join (     
       select name,
               row_number() over(order by  name) rn2
          from student
         where continent = 'Asia'
       ) b
    on a.rn1 = b.rn2
  full join (     
        select name,
               row_number() over(order by  name) rn3
          from student
         where continent = 'Europe'
       ) c
    on coalesce(a.rn1, b.rn2) = c.rn3   -- 
 order by 1
;

-- MySQL do not support full outer join
select a.name America, 
       b.name Asia, 
       c.name Europe
  from (
        select name,
               row_number() over(order by  name) rn1
          from student
         where continent = 'America'
       ) a
  left join (     
       select name,
               row_number() over(order by  name) rn2
          from student
         where continent = 'Asia'
       ) b
    on a.rn1 = b.rn2
  left join (     
        select name,
               row_number() over(order by  name) rn3
          from student
         where continent = 'Europe'
       ) c
    on coalesce(a.rn1, b.rn2) = c.rn3
 order by 1
;

-- To emulate full join in MySQL
/*
SELECT * FROM t1
  LEFT JOIN t2 ON t1.id = t2.id
 UNION
SELECT * FROM t1
 RIGHT JOIN t2 ON t1.id = t2.id
*/
