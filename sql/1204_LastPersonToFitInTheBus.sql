/*
Drop table If Exists Queue;;
Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int);
Truncate table Queue;
insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1');
insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5');
insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2');
insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3');
insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6');
insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4');
*/
-- There is a queue of people waiting to board a bus. However, the bus has a 
-- weight limit of 1000 kilograms, so there may be some people who cannot board.

-- Write an SQL query to find the person_name of the last person that can fit on
-- the bus without exceeding the weight limit. The test cases are generated such 
-- that the first person does not exceed the weight limit.

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
