-- Postgres, Oracle
select extra report_reason,
       count(distinct post_id) report_count 
  from Actions
 where action_date = date'2019-07-05' - 1
   and action = 'report'
 group by extra
 ;

-- MySQL
select extra report_reason,
       count(distinct post_id) report_count 
  from Actions
 where datediff(date'2019-07-05', action_date, w2.recordDate) = 1
   and action = 'report'
 group by extra
 ;
