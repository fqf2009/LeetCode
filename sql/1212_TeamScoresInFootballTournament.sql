/*
Drop table If Exists Teams;
Drop table If Exists Matches;
Create table If Not Exists Teams (team_id int, team_name varchar(30));
Create table If Not Exists Matches (match_id int, host_team int, guest_team int, host_goals int, guest_goals int);
Truncate table Teams;
insert into Teams (team_id, team_name) values ('10', 'Leetcode FC');
insert into Teams (team_id, team_name) values ('20', 'NewYork FC');
insert into Teams (team_id, team_name) values ('30', 'Atlanta FC');
insert into Teams (team_id, team_name) values ('40', 'Chicago FC');
insert into Teams (team_id, team_name) values ('50', 'Toronto FC');
Truncate table Matches;
insert into Matches (match_id, host_team, guest_team, host_goals, guest_goals) values ('1', '10', '20', '3', '0');
insert into Matches (match_id, host_team, guest_team, host_goals, guest_goals) values ('2', '30', '10', '2', '2');
insert into Matches (match_id, host_team, guest_team, host_goals, guest_goals) values ('3', '10', '50', '5', '1');
insert into Matches (match_id, host_team, guest_team, host_goals, guest_goals) values ('4', '20', '30', '1', '0');
insert into Matches (match_id, host_team, guest_team, host_goals, guest_goals) values ('5', '50', '30', '1', '0');
*/
-- You would like to compute the scores of all teams after all matches. Points are 
-- awarded as follows:
--    A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
--    A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
--    A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).
-- Write an SQL query that selects the team_id, team_name and num_points of each 
-- team in the tournament after all described matches.
-- Return the result table ordered by num_points in decreasing order. 
-- In case of a tie, order the records by team_id in increasing order.


-- Postgres
select t.team_id,
       t.team_name,
       sum(case when net_goals > 0 then 3
                when net_goals = 0 then 1
                else 0   
            end
           ) num_points
  from (
        select unnest(array[host_team, guest_team]) team_id,
               unnest(array[host_goals - guest_goals, guest_goals - host_goals]) net_goals
          from Matches 
       ) m
 right join Teams t
    on t.team_id = m.team_id
 group by t.team_id,
          t.team_name
 order by 3 desc, 1;


-- Postgres, Oracle, MySQL, SQL Server
select t.team_id,
       t.team_name,
       sum(case when net_goals > 0 then 3
                when net_goals = 0 then 1
                else 0   
            end
           ) num_points
  from (
        select host_team team_id,
               host_goals - guest_goals net_goals
          from Matches 
         union all
        select guest_team team_id,
               guest_goals - host_goals net_goals
          from Matches
       ) m
 right join Teams t
    on t.team_id = m.team_id
 group by t.team_id,
          t.team_name
 order by 3 desc, 1;
