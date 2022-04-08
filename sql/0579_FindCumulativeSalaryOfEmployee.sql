/*
Drop table if exists Employee;
Create table If Not Exists Employee (id int, month int, salary int);
Truncate table Employee;
insert into Employee (id, month, salary) values ('1', '1', '20');
insert into Employee (id, month, salary) values ('2', '1', '20');
insert into Employee (id, month, salary) values ('1', '2', '30');
insert into Employee (id, month, salary) values ('2', '2', '30');
insert into Employee (id, month, salary) values ('3', '2', '40');
insert into Employee (id, month, salary) values ('1', '3', '40');
insert into Employee (id, month, salary) values ('3', '3', '60');
insert into Employee (id, month, salary) values ('1', '4', '60');
insert into Employee (id, month, salary) values ('3', '4', '70');
insert into Employee (id, month, salary) values ('1', '7', '90');
insert into Employee (id, month, salary) values ('1', '8', '90');
*/

-- Write an SQL query to calculate the cumulative salary summary for every 
-- employee in a single unified table.

-- The cumulative salary summary for an employee can be calculated as follows:
--  - For each month that the employee worked, sum up the salaries in that month 
--    and the previous two months. This is their 3-month sum for that month. If 
--    an employee did not work for the company in previous months, their effective
--    salary for those months is 0.
--  - Do not include the 3-month sum for the most recent month that the employee 
--    worked for in the summary. !!!
--  - Do not include the 3-month sum for any month the employee did not work.

-- Return the result table ordered by id in ascending order. In case of a tie,
-- order it by month in descending order.

-- Oracle, Postgres, MySQL
select  id,
        month,
        salary + (case when prev1_month = month - 1 then prev1_salary else 0 end)
               + (case when prev2_month = month - 2 then prev2_salary else 0 end) as salary
  from (
        select  id,
                month,
                salary,
                lag(month, 1) over (partition by id order by month) prev1_month,
                lag(month, 2) over (partition by id order by month) prev2_month,
                lag(salary, 1) over (partition by id order by month) prev1_salary,
                lag(salary, 2) over (partition by id order by month) prev2_salary,
                row_number() over (partition by id order by month desc) rn
           from Employee
  ) s
 where rn <> 1
 order by id, month desc
 ;
