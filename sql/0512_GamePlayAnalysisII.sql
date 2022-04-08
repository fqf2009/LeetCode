/*
drop table if exists activity;
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
*/

-- Write an SQL query to report the device that is first logged in for each player.
-- Return the result table in any order.

-- Oracle, Postgres, MySQL works
-- T-SQL time exceeded
select player_id,
       device_id
  from (
        select player_id,
               device_id,
               row_number() over (partition by player_id order by event_date) rn
          from activity a
       ) a
 where rn = 1
 ;

 -- Oracle, Postgres, MySQL works, T-SQL failed
 select player_id,
        device_id
   from activity a
  where (player_id, event_date) in (
        select player_id,
               min(event_date) first_login
          from activity a
         group by a.player_id
        ) 
   ;

 -- All databases works
 select a.player_id,
        device_id
   from activity a
   join (
        select player_id,
               min(event_date) first_login
          from activity a
         group by a.player_id
        ) b
     on a.player_id = b.player_id and
        a.event_date = b.first_login
;
