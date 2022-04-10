-- Postgres, Oracle, MySQL 
select count(*) accounts_count
  from Subscriptions s
 where start_date <= date'2021-12-31' and end_date >= date'2021-01-01'
   and not exists (
        select null
          from Streams s1
         where extract(year from s1.stream_date) = 2021
           and s1.account_id = s.account_id
       )
       ;
