-- Postgres, Oracle, MySQL, SQLServer
select id,
       name
  from students s
 where not exists (
            select null
              from departments d
             where d.id = s.department_id
       )
       ;
