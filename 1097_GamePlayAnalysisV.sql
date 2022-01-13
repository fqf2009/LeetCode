/*
drop table if exists activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-01', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
*/

-- The install date of a player is the first login day of that player.
-- We define day one retention of some date x to be the number of players whose 
-- install date is x and they logged back in on the day right after x, divided
-- by the number of players whose install date is x, rounded to 2 decimal places.

-- Write an SQL query to report for each install date, the number of players that
-- installed the game on that day, and the day one retention.
-- Return the result table in any order.


-- Postgres - need explicitly convert int to numeric
select event_date install_dt,
       sum(installed) installs,
       round(sum(retention)::numeric / sum(installed)::numeric, 2) Day1_retention
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
 where installed > 0
 group by event_date
  ;

-- Oracle - date to remove time component
select to_char(event_date, 'yyyy-mm-dd') install_dt,
       sum(installed) installs,
       round(sum(retention) / sum(installed), 2) Day1_retention
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
 where installed > 0
 group by event_date
  ;

-- MySQL - does not support date arithmetic
select event_date install_dt,
       sum(installed) installs,
       round(sum(retention) / sum(installed), 2) Day1_retention
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
 where installed > 0
 group by event_date
  ;
  
