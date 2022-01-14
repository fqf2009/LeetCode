/*
drop table if exists Employee;
Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
Truncate table Employee;
insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', null);
insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
*/

-- Write an SQL query to report the managers with at least five direct reports.
-- Return the result table in any order.

-- Oracle, Postgres, MySQL
select name
  from (
        select m.id,
               m.name
          from employee e 
          join employee m
            on e.managerid = m.id
         group by m.id,
                  m.name
        having count(*) >= 5
       ) e
    ;
