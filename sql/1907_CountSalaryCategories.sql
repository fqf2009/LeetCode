/*
Drop table If Exists Accounts;
Create table If Not Exists Accounts (account_id int, income int);
Truncate table Accounts;
insert into Accounts (account_id, income) values ('3', '108939');
insert into Accounts (account_id, income) values ('2', '12747');
insert into Accounts (account_id, income) values ('8', '87709');
insert into Accounts (account_id, income) values ('6', '91796');
*/
-- Write an SQL query to report the number of bank accounts of each 
-- salary category. The salary categories are:
--    "Low Salary": All the salaries strictly less than $20000.
--    "Average Salary": All the salaries in the inclusive range [$20000, $50000].
--    "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no 
-- accounts in a category, then report 0.
-- Return the result table in any order.


-- Postgres
select c.category,
       coalesce(accounts_count, 0) accounts_count
  from (
        select unnest(array['Low Salary', 'Average Salary', 'High Salary']) category
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
    on a.category = c.category
    ;


-- Oracle
select c.category,
       coalesce(accounts_count, 0) accounts_count
  from (
        select 'Low Salary' category
          from dual           -- difference
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
