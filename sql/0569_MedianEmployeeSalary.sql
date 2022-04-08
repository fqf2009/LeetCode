/*
Drop table if exists Employee;
Create table If Not Exists Employee (id int, company varchar(255), salary int);
Truncate table Employee;
insert into Employee (id, company, salary) values ('1', 'A', '2341');
insert into Employee (id, company, salary) values ('2', 'A', '341');
insert into Employee (id, company, salary) values ('3', 'A', '15');
insert into Employee (id, company, salary) values ('4', 'A', '15314');
insert into Employee (id, company, salary) values ('5', 'A', '451');
insert into Employee (id, company, salary) values ('6', 'A', '513');
insert into Employee (id, company, salary) values ('7', 'B', '15');
insert into Employee (id, company, salary) values ('8', 'B', '13');
insert into Employee (id, company, salary) values ('9', 'B', '1154');
insert into Employee (id, company, salary) values ('10', 'B', '1345');
insert into Employee (id, company, salary) values ('11', 'B', '1221');
insert into Employee (id, company, salary) values ('12', 'B', '234');
insert into Employee (id, company, salary) values ('13', 'C', '2345');
insert into Employee (id, company, salary) values ('14', 'C', '2645');
insert into Employee (id, company, salary) values ('15', 'C', '2645');
insert into Employee (id, company, salary) values ('16', 'C', '2652');
insert into Employee (id, company, salary) values ('17', 'C', '65');
*/

--Write an SQL query to find the median salary of each company.
--Return the result table in any order.

-- Postgres
select id,
       company,
       salary 
  from (
        select id,
               company,
               salary,
               row_number() over (partition by company order by salary) rn,
               count(*) over (partition by company) cnt
          from employee e
         order by 2, 3
       ) s
 where rn = (cnt+1)/2 or rn = (cnt+2)/2
 ;

-- Oracle
select id,
       company,
       salary 
  from (
        select id,
               company,
               salary,
               row_number() over (partition by company order by salary) rn,
               count(*) over (partition by company) cnt
          from employee e
         order by 2, 3
       ) s
 where rn = trunc((cnt+1)/2) or rn = trunc((cnt+2)/2)
 ;
 
-- MySQL
select id,
       company,
       salary 
  from (
        select id,
               company,
               salary,
               row_number() over (partition by company order by salary) rn,
               count(*) over (partition by company) cnt
          from employee e
         order by 2, 3
       ) s
 where rn = truncate((cnt+1)/2, 0) or rn = truncate((cnt+2)/2, 0)
 ;
 