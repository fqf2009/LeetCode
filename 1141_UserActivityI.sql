-- Postgres
select activity_date day,
       count(distinct user_id) active_users
  from activity
 where activity_date between date'2019-07-27' - 29 and date'2019-07-27'
 group  by activity_date
;

-- Postgres, Oracle
select to_char(activity_date, 'yyyy-mm-dd') day,
       count(distinct user_id) active_users
  from activity
 where activity_date between date'2019-07-27' - 29 and date'2019-07-27'
 group  by activity_date
;

-- MySQL
select activity_date day,
       count(distinct user_id) active_users
  from activity
 where activity_date between date_add(date'2019-07-27', interval '-29' day)
                         and date'2019-07-27'
 group  by activity_date
;
