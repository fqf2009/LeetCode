/*
drop table if exists salary;
drop table if exists Employee;
Create table If Not Exists Salary (id int, employee_id int, amount int, pay_date date);
Create table If Not Exists Employee (employee_id int, department_id int);
Truncate table Salary;
insert into Salary (id, employee_id, amount, pay_date) values ('1', '1', '9000', '2017/03/31');
insert into Salary (id, employee_id, amount, pay_date) values ('2', '2', '6000', '2017/03/31');
insert into Salary (id, employee_id, amount, pay_date) values ('3', '3', '10000', '2017/03/31');
insert into Salary (id, employee_id, amount, pay_date) values ('4', '1', '7000', '2017/02/28');
insert into Salary (id, employee_id, amount, pay_date) values ('5', '2', '6000', '2017/02/28');
insert into Salary (id, employee_id, amount, pay_date) values ('6', '3', '8000', '2017/02/28');
Truncate table Employee;
insert into Employee (employee_id, department_id) values ('1', '1');
insert into Employee (employee_id, department_id) values ('2', '2');
insert into Employee (employee_id, department_id) values ('3', '2');
*/

-- Write an SQL query to report the comparison result (higher/lower/same) of the 
-- average salary of employees in a department to the company's average salary.
-- Return the result table in any order.

-- Postgres, Oracle
select pay_month,
       department_id,
       case when dept_avg > company_avg then 'higher'
            when dept_avg = company_avg then 'same'
            else 'lower'
        end comparison
  from (
        select to_char(pay_date, 'yyyy-mm') pay_month, 
               department_id,
               avg(amount) dept_avg,
               sum(sum(amount)) over (partition by to_char(pay_date, 'yyyy-mm')) / 
               sum(count(*)) over (partition by to_char(pay_date, 'yyyy-mm')) company_avg
          from employee e
          join salary s
            on e.employee_id = s.employee_id
         group by to_char(pay_date, 'yyyy-mm'), department_id
        ) c
 ;
 
-- MySQL
select pay_month,
       department_id,
       case when dept_avg > company_avg then 'higher'
            when dept_avg = company_avg then 'same'
            else 'lower'
        end comparison
  from (
        select date_format(pay_date, '%Y-%m') pay_month, 
               department_id,
               avg(amount) dept_avg,
               sum(sum(amount)) over (partition by date_format(pay_date, '%Y-%m')) / 
               sum(count(*)) over (partition by date_format(pay_date, '%Y-%m')) company_avg
          from employee e
          join salary s
            on e.employee_id = s.employee_id
         group by date_format(pay_date, '%Y-%m'), department_id
        ) c
 ;
