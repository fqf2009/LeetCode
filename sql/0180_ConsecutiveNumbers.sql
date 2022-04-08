/*
drop table if exists logs
Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');
*/

-- Write an SQL query to find all numbers that appear at least three times consecutively.
-- Return the result table in any order.

-- Oracle, PostgreSQL, MySQL
select distinct num ConsecutiveNums
  from (
        select num,
               lag(num, 1) over (order by id) prev1_num,
               lag(num, 2) over (order by id) prev2_num
          from logs l
       ) l
 where num = prev1_num and 
       num = prev2_num
  ;
  