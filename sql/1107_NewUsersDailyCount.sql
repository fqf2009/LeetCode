/*
Drop table If Exists Traffic;
Create table If Not Exists Traffic (user_id int, activity varchar(30), activity_date date);
Truncate table Traffic;
insert into Traffic (user_id, activity, activity_date) values ('1', 'login', '2019-05-01');
insert into Traffic (user_id, activity, activity_date) values ('1', 'homepage', '2019-05-01');
insert into Traffic (user_id, activity, activity_date) values ('1', 'logout', '2019-05-01');
insert into Traffic (user_id, activity, activity_date) values ('2', 'login', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('2', 'logout', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('3', 'login', '2019-01-01');
insert into Traffic (user_id, activity, activity_date) values ('3', 'jobs', '2019-01-01');
insert into Traffic (user_id, activity, activity_date) values ('3', 'logout', '2019-01-01');
insert into Traffic (user_id, activity, activity_date) values ('4', 'login', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('4', 'groups', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('4', 'logout', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('5', 'login', '2019-03-01');
insert into Traffic (user_id, activity, activity_date) values ('5', 'logout', '2019-03-01');
insert into Traffic (user_id, activity, activity_date) values ('5', 'login', '2019-06-21');
insert into Traffic (user_id, activity, activity_date) values ('5', 'logout', '2019-06-21');
*/
-- Write an SQL query to reports for every date within at most 90 days 
-- from today, the number of users that logged in for the first time on
-- that date. Assume today is 2019-06-30.

-- Return the result table in any order.


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
