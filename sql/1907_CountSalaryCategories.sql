-- Postgres, MySQL
select c.category,
       coalesce(accounts_count, 0) accounts_count
  from (
        select 'Low Salary' category
         union all
        select 'Average Salary'
         union all
        select 'High Salary'
       ) c
  left join (
        select category,
               count(*) accounts_count
          from (
                select case when income < 20000 then 'Low Salary'
                            when income between 20000 and 50000 then 'Average Salary'
                            else 'High Salary'
                        end category
                  from Accounts 
               ) a
         group by category
       ) a


-- Oracle
select c.category,
       coalesce(accounts_count, 0) accounts_count
  from (
        select 'Low Salary' category
          from dual
         union all
        select 'Average Salary'
          from dual
         union all
        select 'High Salary'
          from dual
       ) c
  left join (
        select category,
               count(*) accounts_count
          from (
                select case when income < 20000 then 'Low Salary'
                            when income between 20000 and 50000 then 'Average Salary'
                            else 'High Salary'
                        end category
                  from Accounts 
               ) a
         group by category
       ) a
    on a.category = c.category
    ;
