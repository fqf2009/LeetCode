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
