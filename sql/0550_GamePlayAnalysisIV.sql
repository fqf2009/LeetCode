/*
drop table if exists activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
*/

-- Write an SQL query to report the fraction of players that logged in again on the day 
-- after the day they first logged in, rounded to 2 decimal places. In other words, you 
-- need to count the number of players that logged in for at least two consecutive days 
-- starting from their first login date, then divide that number by total number of players.


-- Solution 1 - use analytic function
-- Postgres - need explicitly convert int to numeric
select round(sum(retention)::numeric / sum(installed)::numeric, 2) fraction
  from (
        select event_date,
               case when event_date = first_value(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end installed,
               case when event_date + 1 = lead(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end retention
          from activity a
       ) r
 where installed = 1    -- Only count those first logged in ids
  ;

-- Oracle
select round(sum(retention) / sum(installed), 2) fraction
  from (
        select event_date,
               case when event_date = first_value(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end installed,
               case when event_date + 1 = lead(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end retention
          from activity a
       ) r
 where installed = 1
  ;


-- MySQL - does not support date arithmetic
select round(sum(retention) / sum(installed), 2) fraction
  from (
        select event_date,
               case when event_date = first_value(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end installed,
               case when date_add(event_date, interval 1 day) = lead(event_date) over (
                                partition by player_id order by event_date) then 1
                    else 0
                end retention
          from activity a
       ) r
 where installed = 1
  ;


-- Solution 2 - use group by

-- Postgres - must explicitly convert int to numeric
 select round(second_login_count::numeric / total_count::numeric, 2) fraction
   from (
         select count(distinct player_id) total_count
           from activity
        ) a
  cross join (    -- single row cross join
             select count(*) second_login_count
               from activity
              where (player_id, event_date) in (
                         select player_id,
                                min(event_date) + 1 second_login
                           from activity
                          group by player_id
                     )
            ) b
 ;
 
 -- Oracle
 select round(second_login_count / total_count, 2) fraction
   from (
         select count(distinct player_id) total_count
           from activity
        ) a
  cross join (
             select count(*) second_login_count
               from activity
              where (player_id, event_date) in (
                         select player_id,
                                min(event_date) + 1 second_login
                           from activity
                          group by player_id
                     )
            ) b
 ;

 -- MySQL - No date arithmetic, use date_add
  select round(second_login_count/ total_count, 2) fraction
   from (
         select count(distinct player_id) total_count
           from activity
        ) a
  cross join (
             select count(*) second_login_count
               from activity
              where (player_id, event_date) in (
                         select player_id,
                                date_add(min(event_date), interval 1 day) second_login
                           from activity
                          group by player_id
                     )
            ) b
 ;
