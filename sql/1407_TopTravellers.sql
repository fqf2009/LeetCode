-- Postgres, Oracle, MySQL, SQLServer
select name,
       coalesce(travelled_distance, 0) travelled_distance
  from users u
  left join (
        select user_id,
               sum(distance) travelled_distance 
          from Rides
         group by user_id
       ) r
    on u.id = r.user_id
 order by travelled_distance desc,
          name
    ;
