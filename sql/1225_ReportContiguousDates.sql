/*
Drop table If Exists Failed;
Drop table If Exists Succeeded;
Create table If Not Exists Failed (fail_date date);
Create table If Not Exists Succeeded (success_date date);
Truncate table Failed;
insert into Failed (fail_date) values ('2018-12-28');
insert into Failed (fail_date) values ('2018-12-29');
insert into Failed (fail_date) values ('2019-01-04');
insert into Failed (fail_date) values ('2019-01-05');
Truncate table Succeeded;
insert into Succeeded (success_date) values ('2018-12-30');
insert into Succeeded (success_date) values ('2018-12-31');
insert into Succeeded (success_date) values ('2019-01-01');
insert into Succeeded (success_date) values ('2019-01-02');
insert into Succeeded (success_date) values ('2019-01-03');
insert into Succeeded (success_date) values ('2019-01-06');
*/
-- A system is running one task every day. Every task is independent of the 
-- previous tasks. The tasks can fail or succeed.
-- Write an SQL query to generate a report of period_state for each continuous
-- interval of days in the period from 2019-01-01 to 2019-12-31.
-- period_state is 'failed' if tasks in this interval failed or 'succeeded' 
-- if tasks in this interval succeeded. Interval of days are retrieved as 
-- start_date and end_date.
-- Return the result table ordered by start_date.


-- Postgres, MySQL
select period_state,
       start_date,
       end_date
  from (
        select task_date,
               period_state,
               start_date,
               coalesce(end_date, lead(end_date) over (order by task_date)) end_date
          from (
                select task_date,
                       period_state,
                       case when coalesce(lag(period_state) over (order by task_date), 'unknown') <> period_state then task_date
                            else null
                        end start_date,
                       case when coalesce(lead(period_state) over (order by task_date), 'unknown') <> period_state then task_date
                            else null
                        end end_date
                  from (
                        select success_date task_date,
                               'succeeded' period_state
                          from succeeded
                         where success_date between date'2019-01-01' and date'2019-12-31'
                         union all
                        select fail_date task_date,
                               'failed' period_state
                          from failed
                         where fail_date between date'2019-01-01' and date'2019-12-31'
                       ) t
                ) t1
          where start_date is not null
             or end_date is not null
        ) t2
  where start_date is not null
  order by start_date
;

-- Another approach, by grouping contigious rows into group, i.e.:
--   because row_number() is always contigious among one partition
--   (period_state in this problem), if the dates are contigious, they
--   increase at the same pace as row_number(), otherwise, they change
--   faster than row_number().
-- The diff between works below because successful and failed events are in
--   different tables, otherwise, please add "(partition by period_state order by...)"
-- Postgres, MySQL
select period_state,
       start_date,
       end_date
  from (
        select period_state,
               diff,
               min(task_date) start_date,
               max(task_date) end_date
          from (
                select success_date task_date,
                       'succeeded' period_state,
                       (success_date - date'2000-01-01') - row_number() over (order by success_date) diff
                  from succeeded
                 where extract(year from success_date) = 2019
                 union all
                select fail_date task_date,
                       'failed' period_state,
                       (fail_date - date'2000-01-01') - row_number() over (order by fail_date) diff
                  from failed
                 where extract(year from fail_date) = 2019
               ) t
         group by period_state,
                  diff
       ) t1
 order by start_date
;

-- Oracle
select period_state,
       to_char(start_date, 'yyyy-mm-dd') start_date,
       to_char(end_date, 'yyyy-mm-dd') end_date
  from (
        select task_date,
               period_state,
               start_date,
               coalesce(end_date, lead(end_date) over (order by task_date)) end_date
          from (
                select task_date,
                       period_state,
                       case when coalesce(lag(period_state) over (order by task_date), 'unknown') <> period_state then task_date
                            else null
                        end start_date,
                       case when coalesce(lead(period_state) over (order by task_date), 'unknown') <> period_state then task_date
                            else null
                        end end_date
                  from (
                        select success_date task_date,
                               'succeeded' period_state
                          from succeeded
                         where success_date between date'2019-01-01' and date'2019-12-31'
                         union all
                        select fail_date task_date,
                               'failed' period_state
                          from failed
                         where fail_date between date'2019-01-01' and date'2019-12-31'
                       ) t
                ) t1
          where start_date is not null
             or end_date is not null
        ) t2
  where start_date is not null
  order by start_date
;

-- Oracle
select period_state,
       to_char(start_date, 'yyyy-mm-dd') start_date,
       to_char(end_date, 'yyyy-mm-dd') end_date
  from (
        select period_state,
               diff,
               min(task_date) start_date,
               max(task_date) end_date
          from (
                select success_date task_date,
                       'succeeded' period_state,
                       (success_date - date'2000-01-01') - row_number() over (order by success_date) diff
                  from succeeded
                 where extract(year from success_date) = 2019
                 union all
                select fail_date task_date,
                       'failed' period_state,
                       (fail_date - date'2000-01-01') - row_number() over (order by fail_date) diff
                  from failed
                 where extract(year from fail_date) = 2019
               ) t
         group by period_state,
                  diff
       ) t1
 order by start_date
;
