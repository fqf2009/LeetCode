/*
drop table if exists activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
*/

-- Write an SQL query to report for each player and date, how many games played so far 
-- by the player. That is, the total number of games played by the player until that date.
-- Return the result table in any order.

-- Postgres, MySQL works
-- T-SQL tests ok, but run time exception upon submit to leetcode
select player_id,
       event_date,
       sum(games_played) over (
                partition by player_id
                order by event_date
                rows between unbounded preceding and current row
           ) games_played_so_far
  from activity;
  
-- Oracle date type has time component
select player_id,
       to_char(event_date, 'yyyy-mm-dd') event_date,
       sum(games_played) over (
                partition by player_id
                order by event_date
                rows between unbounded preceding and current row
           ) games_played_so_far
  from activity;
