-- Postgres, Oracle, MySQL, SQL Server
select employee_id, 
       department_id
  from (
        select employee_id, 
               department_id,
               count(*) over (partition by employee_id) dept_cnt
          from Employee e
       ) e
 where dept_cnt = 1
 union -- not use 'union all' because some employee with 'Y', but only have one dept
select employee_id, department_id 
  from Employee e
 where primary_flag = 'Y';
