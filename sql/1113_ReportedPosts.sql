-- Postgres, Oracle, MySQL
select extra report_reason,
       count(distinct post_id) report_count 
  from Actions
 where action_date = date'2019-07-05' - 1
   and action = 'report'
 group by extra
 ;
