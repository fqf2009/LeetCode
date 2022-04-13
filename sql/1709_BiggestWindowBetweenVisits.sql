-- Assume today's date is '2021-1-1'.
-- Write an SQL query that will, for each user_id, find out the largest window 
-- of days between each visit and the one right after it (or today if you are 
-- considering the last visit).
-- Return the result table ordered by user_id.


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
