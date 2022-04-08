-- Postgres, Oracle, MySQL, SQLServer
select s.company_id,
       employee_id,
       employee_name,
       round(salary * (1 - tax_rate), 0) salary
  from Salaries s
  join (
        select company_id,
               case when max_salary > 10000 then 0.49
                    when max_salary >= 1000 then 0.24
                    else 0.0
                end tax_rate
          from (
                select company_id,
                       max(salary) max_salary
                  from salaries
                 group by company_id
               ) s
       ) t
    on s.company_id = t.company_id
    ;
