/*
Drop table If Exists Players;
Drop table If Exists Matches;
Create table If Not Exists Players (player_id int, group_id int);
Create table If Not Exists Matches (match_id int, first_player int, second_player int, first_score int, second_score int);
Truncate table Players;
insert into Players (player_id, group_id) values ('10', '2');
insert into Players (player_id, group_id) values ('15', '1');
insert into Players (player_id, group_id) values ('20', '3');
insert into Players (player_id, group_id) values ('25', '1');
insert into Players (player_id, group_id) values ('30', '1');
insert into Players (player_id, group_id) values ('35', '2');
insert into Players (player_id, group_id) values ('40', '3');
insert into Players (player_id, group_id) values ('45', '1');
insert into Players (player_id, group_id) values ('50', '2');
Truncate table Matches;
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('1', '15', '45', '3', '0');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('2', '30', '25', '1', '2');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('3', '30', '15', '2', '0');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('4', '40', '20', '5', '2');
insert into Matches (match_id, first_player, second_player, first_score, second_score) values ('5', '35', '50', '1', '1');
*/
-- The winner in each group is the player who scored the maximum total points within
-- the group. In the case of a tie, the lowest player_id wins.
-- Write an SQL query to find the winner in each group.
-- Return the result table in any order.

-- Postgres, Oracle, MySQL, SQLServer
select group_id,
       player_id
  from (
        select p.group_id,
               p.player_id,
               rank() over (partition by group_id order by sum(score) desc, p.player_id) rk
          from (
                select first_player player_id,
                       first_score score
                  from Matches
                 union all
                select second_player, 
                       second_score
                  from Matches
               ) m
          join Players p
            on m.player_id = p.player_id
         group by p.group_id,
                  p.player_id
       ) s
 where rk = 1
 ;
