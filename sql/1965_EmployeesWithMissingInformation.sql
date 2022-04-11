
-- Postgres, SQL Server
select employee_id
  from Employees
except 
select employee_id
  from Salaries
 union all (
select employee_id
  from Salaries
except 
select employee_id
  from Employees
 )
 order by 1
 ;

-- Oracle
select employee_id
  from Employees
 minus 
select employee_id
  from Salaries
 union all (
select employee_id
  from Salaries
 minus 
select employee_id
  from Employees
 )
 order by 1
 ;
 
-- All DBs
select employee_id
  from Employees
 where employee_id not in (
        select employee_id
          from Salaries
       )
 union all (
        select employee_id
          from Salaries
         where employee_id not in (
                select employee_id
                  from Employees
               )
 )
 order by 1
 ;
