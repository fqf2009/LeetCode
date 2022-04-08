/*
drop table if exists point2d;
Create Table If Not Exists Point2D (x int not null, y int not null);
Truncate table Point2D;
insert into Point2D (x, y) values ('-1', '-1');
insert into Point2D (x, y) values ('0', '0');
insert into Point2D (x, y) values ('-1', '-2');
*/

-- The distance between two points p1(x1, y1) and p2(x2, y2) is 
--    sqrt((x2 - x1)^2 + (y2 - y1)^2).
-- Write an SQL query to report the shortest distance between any two
-- points from the Point2D table. Round the distance to two decimal points.

-- Postgres
select round(sqrt(power(p1.x - p2.x, 2) + power(p1.y - p2.y, 2))::numeric, 2) shortest
  from point2d p1
 cross join point2d p2
 where p1.x <> p2.x or
       p1.y <> p2.y
 order by 1
 limit 1
 ;

-- MySQL
select round(sqrt(power(p1.x - p2.x, 2) + power(p1.y - p2.y, 2)), 2) shortest
  from point2d p1
 cross join point2d p2
 where p1.x <> p2.x or
       p1.y <> p2.y
 order by 1
 limit 1
 ;
 
-- Oracle 
select shortest
  from (
        select round(sqrt(power(p1.x - p2.x, 2) + power(p1.y - p2.y, 2)), 2) shortest
          from point2d p1
         cross join point2d p2
         where p1.x <> p2.x or
               p1.y <> p2.y
         order by 1
       ) p
 where rownum = 1
 ;
 
-- Oracle 
select round(sqrt(power(p1.x - p2.x, 2) + power(p1.y - p2.y, 2)), 2) shortest
  from point2d p1
 cross join point2d p2
 where p1.x <> p2.x or
       p1.y <> p2.y
 order by 1
 fetch first 1 rows only
;
