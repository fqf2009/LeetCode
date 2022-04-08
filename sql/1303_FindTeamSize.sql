-- Postgres, Oracle, MySQL, SQLServer
select employee_id,
       count(*) over (partition by team_id) team_size
  from employee;
