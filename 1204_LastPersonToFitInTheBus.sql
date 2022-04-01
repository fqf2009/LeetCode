-- Postgres, MySQL
-- MySQL:       LIMIT [offset,] limit
-- Postgres:    LIMIT limit OFFSET offset
select person_name
  from (
        select person_name,
               turn,
               sum(weight) over (order by turn) total_weight
          from Queue
       ) q
 where total_weight <= 1000
 order by turn desc
 limit 1
 ;

-- Oracle
-- from 12c, [offset m rows] [fetch next n rows only]
select person_name
  from (
        select person_name
          from (
                select person_name,
                       turn,
                       sum(weight) over (order by turn) total_weight
                  from Queue
               ) q
         where total_weight <= 1000
         order by turn desc
        ) q
 where rownum = 1
 ;

-- SQL Server
 select person_name
  from (
        select person_name,
               turn,
               sum(weight) over (order by turn) total_weight
          from Queue
       ) q
 where total_weight <= 1000
 order by turn desc
 offset 0 rows              -- cannot be omitted
 fetch next 1 rows only
 ;
