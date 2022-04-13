/*
Drop table If Exists Teams;
Drop table If Exists Matches;
Create table If Not Exists Teams (team_id int, team_name varchar(20));
Create table If Not Exists Matches (home_team_id int, away_team_id int, home_team_goals int, away_team_goals int);
Truncate table Teams;
insert into Teams (team_id, team_name) values ('1', 'Ajax');
insert into Teams (team_id, team_name) values ('4', 'Dortmund');
insert into Teams (team_id, team_name) values ('6', 'Arsenal');
Truncate table Matches;
insert into Matches (home_team_id, away_team_id, home_team_goals, away_team_goals) values ('1', '4', '0', '1');
insert into Matches (home_team_id, away_team_id, home_team_goals, away_team_goals) values ('1', '6', '3', '3');
insert into Matches (home_team_id, away_team_id, home_team_goals, away_team_goals) values ('4', '1', '5', '2');
insert into Matches (home_team_id, away_team_id, home_team_goals, away_team_goals) values ('6', '1', '0', '0');
*/
-- Write an SQL query to report the statistics of the league. The statistics 
-- should be built using the played matches where the winning team gets three 
-- points and the losing team gets no points. If a match ends with a draw, 
-- both teams get one point.
-- Each row of the result table should contain:
--   team_name -      The name of the team in the Teams table.
--   matches_played - The number of matches played as either a home or away team.
--   points -         The total points the team has so far.
--   goal_for -       The total number of goals scored by the team across all matches.
--   goal_against -   The total number of goals scored by opponent teams against 
--                    this team across all matches.
--   goal_diff -      The result of goal_for - goal_against.
-- Return the result table ordered by points in descending order. If two or 
-- more teams have the same points, order them by goal_diff in descending order.
-- If there is still a tie, order them by team_name in lexicographical order.


-- Postgres
select team_name, 
       count(*) matches_played,
       sum(case when goal_diff > 0 then 3
                when goal_diff = 0 then 1
                else 0
            end) points,
        sum(goal_for) goal_for,
        sum(goal_against) goal_against,
        sum(goal_diff) goal_diff
  from (
        select unnest(array[home_team_id, away_team_id]) id,
               unnest(array[home_team_goals, away_team_goals]) goal_for,
               unnest(array[away_team_goals, home_team_goals]) goal_against,
               unnest(array[home_team_goals - away_team_goals, away_team_goals - home_team_goals]) goal_diff
          from matches
       ) m
  join teams t
    on t.team_id = m.id
 group by t.team_name
 order by points desc,
          goal_diff desc,
          team_name
;


-- Postgres, Oracle, MySQL
select team_name, 
       count(*) matches_played,
       sum(case when goal_diff > 0 then 3
                when goal_diff = 0 then 1
                else 0
            end) points,
        sum(goal_for) goal_for,
        sum(goal_against) goal_against,
        sum(goal_diff) goal_diff
  from (
        select home_team_id id,
               home_team_goals goal_for,
               away_team_goals goal_against,
               home_team_goals - away_team_goals goal_diff
          from matches
         union all
        select away_team_id id,
               away_team_goals goal_for,
               home_team_goals goal_against,
               away_team_goals - home_team_goals goal_diff
          from matches
       ) m
  join teams t
    on t.team_id = m.id
 group by t.team_name
 order by points desc,
          goal_diff desc,
          team_name
;
