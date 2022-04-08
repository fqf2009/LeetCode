/*
Drop table If Exists Employees;
Create table If Not Exists Employees (employee_id int, employee_name varchar(30), manager_id int);
Truncate table Employees;
insert into Employees (employee_id, employee_name, manager_id) values ('1', 'Boss', '1');
insert into Employees (employee_id, employee_name, manager_id) values ('3', 'Alice', '3');
insert into Employees (employee_id, employee_name, manager_id) values ('2', 'Bob', '1');
insert into Employees (employee_id, employee_name, manager_id) values ('4', 'Daniel', '2');
insert into Employees (employee_id, employee_name, manager_id) values ('7', 'Luis', '4');
insert into Employees (employee_id, employee_name, manager_id) values ('8', 'John', '3');
insert into Employees (employee_id, employee_name, manager_id) values ('9', 'Angela', '8');
insert into Employees (employee_id, employee_name, manager_id) values ('77', 'Robert', '1');
*/
-- Write an SQL query to find employee_id of all employees that directly or 
-- indirectly report their work to the head of the company.
-- The indirect relation between managers will not exceed three managers as 
-- the company is small.
-- Return the result table in any order.


-- !!! Note the tricky part in this problem: if an employee does not
--     have manager, its manager_id is the same as its employee_id,
--     instead of null.
--     Therefore need to add an extra predicate, e.g.:
--         ( e.employee_id <> 1, or, e.employee_id <> e.manager_id )
--     to prevent the rows already in CTE to added again, and loop forever.
-- Postgres, MySQL
with recursive t(employee_id) as(
    select employee_id
      from employees e
     where e.employee_id = 1
     union all
    select e.employee_id
      from employees e
      join t
        on e.manager_id = t.employee_id
     where e.employee_id <> e.manager_id -- exclude the head to avoid endless loop
)
select employee_id
  from t
 where employee_id <> 1
;

-- Oracle, SQL Server
with t(employee_id) as (
    select employee_id
      from employees e
     where e.employee_id = 1
     union all
    select e.employee_id
      from employees e
      join t
        on e.manager_id = t.employee_id
     where e.employee_id <> e.manager_id -- exclude the head to avoid endless loop
)
select employee_id
  from t
 where employee_id <> 1
;
