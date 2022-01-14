/*
Drop table If Exists Numbers;
Create table If Not Exists Numbers (num int, frequency int);
Truncate table Numbers;
insert into Numbers (num, frequency) values ('0', '7');
insert into Numbers (num, frequency) values ('1', '1');
insert into Numbers (num, frequency) values ('2', '3');
insert into Numbers (num, frequency) values ('3', '1');
*/

-- The median is the value separating the higher half from the lower half of a data sample.
-- Write an SQL query to report the median of all the numbers in the database after
-- decompressing the Numbers table. Round the median to one decimal point.

-- Postgres
select avg(num) median
  from (
        select num,
               frequency,
               sum(frequency) over (order by num) csum,
               -- sum(frequency) over () total,
               (sum(frequency) over () + 1) / 2 mid1,
               (sum(frequency) over () + 2) / 2 mid2
          from numbers
          -- order by num
       ) n
 where (mid1 between csum - frequency + 1 and csum) or
       (mid2 between csum - frequency + 1 and csum)
 ;
 
-- Oracle, Postgres
select avg(num) median
  from (
        select num,
               frequency,
               sum(frequency) over (order by num) csum,
               trunc((sum(frequency) over () + 1) / 2) mid1,
               trunc((sum(frequency) over () + 2) / 2) mid2
          from numbers
       ) n
 where (mid1 between csum - frequency + 1 and csum) or
       (mid2 between csum - frequency + 1 and csum)
 ;
 
-- MySQL
 select avg(num) median
  from (
        select num,
               frequency,
               sum(frequency) over (order by num) csum,
               truncate((sum(frequency) over () + 1) / 2, 0) mid1,
               truncate((sum(frequency) over () + 2) / 2, 0) mid2
          from numbers
       ) n
 where (mid1 between csum - frequency + 1 and csum) or
       (mid2 between csum - frequency + 1 and csum)
 ;
