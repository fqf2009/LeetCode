/*
Drop table If Exists MyNumbers
Create table If Not Exists MyNumbers (num int);
Truncate table MyNumbers;
insert into MyNumbers (num) values ('8');
insert into MyNumbers (num) values ('8');
insert into MyNumbers (num) values ('3');
insert into MyNumbers (num) values ('3');
insert into MyNumbers (num) values ('1');
insert into MyNumbers (num) values ('4');
insert into MyNumbers (num) values ('5');
insert into MyNumbers (num) values ('6');
*/
-- A single number is a number that appeared only once in the MyNumbers table.
-- Write an SQL query to report the largest single number. If there is no 
-- single number, report null.
-- The query result format is in the following example.

-- Postgres
select num
  from MyNumbers
 group by num
having count(*) = 1
 union all
select null
 order by num desc nulls last
 limit 1
;

-- Oracle
select num
  from (
        select num
          from MyNumbers
         group by num
        having count(*) = 1
         union all
        select null
          from dual
         order by num desc nulls last
       )
 where rownum = 1
;

-- MySQL does not support nulls last
-- In MySQL, null is always small than non-null value
select num
  from MyNumbers
 group by num
having count(*) = 1
 union all
select null
 order by num desc 
 limit 1
;
