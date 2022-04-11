-- Postgres, MySQL, Oracle
select e.employee_id,
       e.name,
       count(*) reports_count,
       round(avg(e1.age), 0) average_age
  from employees e
  join employees e1
    on e.employee_id = e1.reports_to
 group by e.employee_id,
          e.name
 order by e.employee_id
 ;
