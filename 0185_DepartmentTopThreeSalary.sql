/*
Drop table if exists Employee;
Drop table if exists Department;
Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
Create table If Not Exists Department (id int, name varchar(255));
Truncate table Employee;
insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');
Truncate table Department;
insert into Department (id, name) values ('1', 'IT');
insert into Department (id, name) values ('2', 'Sales');
*/

-- Write an SQL query to find employees who have the highest salary in each of the departments.
-- Return the result table in any order.

-- Oracle, Postgres, MySQL, T-SQL
select d.name Department,
       e.name Employee,
       e.Salary
  from (
        select e.name,
               e.salary,
               e.departmentId,
               dense_rank() over (partition by e.departmentId order by e.salary desc) rk
        from employee e
        ) e
  join department d
    on d.id = e.departmentId
 where rk <= 3
 ;
