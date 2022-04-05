/*
Drop table If Exists Logs;
Create table If Not Exists Logs (log_id int);
Truncate table Logs;
insert into Logs (log_id) values ('1');
insert into Logs (log_id) values ('2');
insert into Logs (log_id) values ('3');
insert into Logs (log_id) values ('7');
insert into Logs (log_id) values ('8');
insert into Logs (log_id) values ('10');
*/
-- Write an SQL query to find the start and end number of continuous 
-- ranges in the table Logs.
-- Return the result table ordered by start_id.

-- Postgres, Oracle, MySQL, SQLServer
select min(log_id) start_id,
       max(log_id) end_id
  from (
        select log_id,
               log_id - row_number() over (order by log_id) group_no
          from logs
       ) g
 group by group_no
 order by 1
;
