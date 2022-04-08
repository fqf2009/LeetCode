/*
drop table If Exists actions;
drop table If Exists Removals;
Create table If Not Exists Actions (user_id int, post_id int, action_date date, action varchar(10), extra varchar(10));
create table if not exists Removals (post_id int, remove_date date);
Truncate table Actions;
insert into Actions (user_id, post_id, action_date, action, extra) values ('1', '1', '2019-07-01', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('1', '1', '2019-07-01', 'like', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('1', '1', '2019-07-01', 'share', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('2', '2', '2019-07-04', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('2', '2', '2019-07-04', 'report', 'spam');
insert into Actions (user_id, post_id, action_date, action, extra) values ('3', '4', '2019-07-04', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('3', '4', '2019-07-04', 'report', 'spam');
insert into Actions (user_id, post_id, action_date, action, extra) values ('4', '3', '2019-07-02', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('4', '3', '2019-07-02', 'report', 'spam');
insert into Actions (user_id, post_id, action_date, action, extra) values ('5', '2', '2019-07-03', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('5', '2', '2019-07-03', 'report', 'racism');
insert into Actions (user_id, post_id, action_date, action, extra) values ('5', '5', '2019-07-03', 'view', 'None');
insert into Actions (user_id, post_id, action_date, action, extra) values ('5', '5', '2019-07-03', 'report', 'racism');
Truncate table Removals;
insert into Removals (post_id, remove_date) values ('2', '2019-07-20');
insert into Removals (post_id, remove_date) values ('3', '2019-07-18');
*/
-- Write an SQL query to find the average daily percentage of posts that got 
-- removed after being reported as spam, rounded to 2 decimal places.


-- Postgres
select round(avg(daily_pct), 2) average_daily_percent
  from (
        select action_date,
               (count(r.post_id))::numeric / count(*) * 100 daily_pct  -- !!!
          from (
                select distinct
                       post_id,
                       action_date
                  from actions
                 where action = 'report'
                   and extra = 'spam'
               ) s
          left join Removals r
            on r.post_id = s.post_id
         group by action_date
       ) p
 ;

-- MySQL, Oracle
select round(avg(daily_pct), 2) average_daily_percent
  from (
        select action_date,
               (count(r.post_id)) / count(*) * 100 daily_pct
          from (
                select distinct
                       post_id,
                       action_date
                  from actions
                 where action = 'report'
                   and extra = 'spam'
               ) s
          left join Removals r
            on r.post_id = s.post_id
         group by action_date
       ) p
 ;

-- SQL Server
select round(avg(daily_pct), 2) average_daily_percent
  from (
        select action_date,
               count(r.post_id)*100.0 / count(*) daily_pct
          from (
                select distinct
                       post_id,
                       action_date
                  from actions
                 where action = 'report'
                   and extra = 'spam'
               ) s
          left join Removals r
            on r.post_id = s.post_id
         group by action_date
       ) p
 ;
