-- Postgres, Oracle
select to_char(trans_date, 'yyyy-mm') month,
       country,
       count(*) trans_count,
       sum(case when state = 'approved' then 1 
                else 0 
           end) approved_count,
       sum(amount) trans_total_amount,
       sum(case when state = 'approved' then amount 
                else 0 
           end)  approved_total_amount
  from Transactions 
 group by to_char(trans_date, 'yyyy-mm'), 
          country
          ;

-- MySQL
select date_format(trans_date, '%Y-%m') month,
       country,
       count(*) trans_count,
       sum(case when state = 'approved' then 1 
                else 0 
           end) approved_count,
       sum(amount) trans_total_amount,
       sum(case when state = 'approved' then amount 
                else 0 
           end)  approved_total_amount
  from Transactions 
 group by 1, 
          country
          ;
