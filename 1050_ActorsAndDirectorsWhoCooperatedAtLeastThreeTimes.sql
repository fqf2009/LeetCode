-- Postgres, Oracle, MySQL, SQLServer
select actor_id, director_id
  from ActorDirector ad
 group by actor_id, director_id
having count(*) >= 3;
