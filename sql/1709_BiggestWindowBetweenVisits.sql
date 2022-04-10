-- Postgres, Oracle
select user_id,
       max(days) biggest_window
  from (
        select user_id,
               coalesce(lead(visit_date) over (partition by user_id 
                                               order by visit_date), date'2021-01-01')
                    - visit_date days
          from UserVisits
       ) v
 group by user_id
 order by user_id;

-- MySQL
select user_id,
       max(days) biggest_window
  from (
        select user_id,
               datediff(coalesce(lead(visit_date) over 
                                    (partition by user_id order by visit_date),
                                 date'2021-01-01'),
                        visit_date) days
          from UserVisits
       ) v
 group by user_id
 order by user_id;
