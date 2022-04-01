-- Postgres, Oracle, MySQL, SQLServer
select project_id,
       employee_id
  from (
        select p.project_id,
               p.employee_id,
               dense_rank() over (partition by project_id order by experience_years desc) rk
          from project p
          join employee e
            on p.employee_id = e.employee_id
       ) p
 where rk = 1
 ;
