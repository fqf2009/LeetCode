/*
drop table if exists employee;
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int);
Truncate table Employee;
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4');
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', null);
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', null);
*/

-- Write an SQL query to find the employees who earn more than their managers.

-- Oracle, PostgreSQL, MySQL
select name Employee
  from employee e 
 where exists (
        select null 
          from employee mgr 
         where e.managerid = mgr.id and 
               e.salary > mgr.salary
       );


select e.name Employee
  from employee e
  join employee mgr
    on e.managerid = mgr.id
 where e.salary > mgr.salary
 ;
