/*
Drop table if exists weather;
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-05', '30');
*/

-- Write an SQL query to find all dates' Id with higher temperatures compared to
-- its previous dates (yesterday).
-- Return the result table in any order.

-- Correct for Oracle and PostgreSQL, MySql failed on submit (but ok in test run)
select id
  from (
        select id,
               recordDate,
               temperature,
               lag(recordDate) over (order by  recordDate) prev_date,
               lag(temperature) over (order by  recordDate) prev_temp
          from weather
        ) w
 where temperature > prev_temp and 
       recordDate = prev_date + 1
 ;

-- Oracle and PostgreSQL
 select w.id
   from weather w 
   join weather w2
     on w2.recordDate + 1 = w.recordDate
  where w.temperature > w2.temperature
  ;

-- MySQL: datediff(end_date, start_date), get days between
 select w.id
   from weather w 
   join weather w2
     on datediff(w.recordDate, w2.recordDate) = 1
  where w.temperature > w2.temperature
  ;

-- T-SQL does not support date arithmetic
--       datediff({day|month|year|...}, start_date, end_date)
select id
  from (
        select id,
               recordDate,
               temperature,
               lag(recordDate) over (order by  recordDate) prev_date,
               lag(temperature) over (order by  recordDate) prev_temp
          from weather
        ) w
 where temperature > prev_temp and 
       datediff(day, prev_date, recordDate) = 1
 ;
