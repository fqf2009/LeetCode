-- Postgres, Oracle, MySQL, SQLServer
select project_id
  from (
        select project_id,
               dense_rank() over (order by count(employee_id) desc) rk
          from project p
         group by project_id
       ) p
 where p.rk = 1
;
