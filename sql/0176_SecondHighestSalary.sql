--Write an SQL query to report the second highest salary from the Employee
--table. If there is no second highest salary, the query should report null.

/*
drop table if exists Employee;
Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');
*/

-- Postgres (nulls last is default for ascending)
select salary SecondHighestSalary
  from (
        select salary,
               dense_rank() over (order by salary desc) rk
          from Employee e
       ) s
 where rk = 2
 union all
select null
 order by 1 nulls last
 limit 1
;

-- Oracle (nulls last is default for ascending)
select SecondHighestSalary
  from (
        select salary SecondHighestSalary
          from (
                select salary,
                       dense_rank() over (order by salary desc) rk
                  from Employee e
               ) s
         where rk = 2
         union all
        select null
          from dual
         order by 1 nulls last
     )
 where rownum = 1
;

-- MySQL (NULL values are considered lower in order, than any non-NULL value)
select salary SecondHighestSalary
  from (
        select salary,
               dense_rank() over (order by salary desc) rk
          from Employee e
       ) s
 where rk = 2
 union all
select null
 order by 1 desc
 limit 1
;