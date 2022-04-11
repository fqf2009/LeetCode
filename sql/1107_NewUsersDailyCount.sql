
select login_date,
       count(*) user_count
  from (
        select user_id,
               activity_date login_date,
               row_number() over (partition by user_id order by activity_date) rn
          from Traffic
         where activity = 'login'
       ) t
 where rn = 1 and
       login_date between date'2019-06-30' - 90 and date'2019-06-30'
 group by login_date
 ;

-- MySQL
select login_date,
       count(*) user_count
  from (
        select user_id,
               activity_date login_date,
               row_number() over (partition by user_id order by activity_date) rn
          from Traffic
         where activity = 'login'
       ) t
 where rn = 1 and
       login_date between date_add(date'2019-06-30', interval '-90' day) and date'2019-06-30'
 group by login_date
 ;

-- Oracle
select to_char(login_date, 'yyyy-mm-dd') login_date,
       count(*) user_count
  from (
        select user_id,
               activity_date login_date,
               row_number() over (partition by user_id order by activity_date) rn
          from Traffic
         where activity = 'login'
       ) t
 where rn = 1 and
       login_date between date'2019-06-30' - 90 and date'2019-06-30'
 group by login_date
 ;
