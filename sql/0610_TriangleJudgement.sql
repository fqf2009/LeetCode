/*
drop table if exists triangle;
Create table If Not Exists Triangle (x int, y int, z int);
Truncate table Triangle;
insert into Triangle (x, y, z) values ('13', '15', '30');
insert into Triangle (x, y, z) values ('10', '20', '15');
*/

-- Write an SQL query to report for every three line segments whether they can form a triangle.
-- Return the result table in any order.

-- Postgres, Oracle, MySQL
-- Note: "sum(x, y, z) - 2*max(x, y, z)" is incorrect, because sum() and max()
--        are aggregate function in sql, greatest() and least() are not
select x, y, z,
       case when x + y + z - 2*greatest(x, y, z) > 0 then 'Yes'
            else 'No'
        end triangle
  from Triangle
  ;
  