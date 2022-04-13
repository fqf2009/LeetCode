/*
-- Postgres
Drop table If Exists Calls;
Create table If Not Exists Calls (caller_id int, recipient_id int, call_time timestamp);
Truncate table Calls;
insert into Calls (caller_id, recipient_id, call_time) values ('8',  '4', '2021-08-24 17:46:07');
insert into Calls (caller_id, recipient_id, call_time) values ('4',  '8', '2021-08-24 19:57:13');
insert into Calls (caller_id, recipient_id, call_time) values ('5',  '1', '2021-08-11 05:28:44');
insert into Calls (caller_id, recipient_id, call_time) values ('8',  '3', '2021-08-17 04:04:15');
insert into Calls (caller_id, recipient_id, call_time) values ('11', '3', '2021-08-17 13:07:00');
insert into Calls (caller_id, recipient_id, call_time) values ('8', '11', '2021-08-17 22:22:22');
-- Oracle
Create table Calls (caller_id int, recipient_id int, call_time date);
Truncate table Calls;
insert into Calls (caller_id, recipient_id, call_time) values ('8',  '4', timestamp'2021-08-24 17:46:07');
insert into Calls (caller_id, recipient_id, call_time) values ('4',  '8', timestamp'2021-08-24 19:57:13');
insert into Calls (caller_id, recipient_id, call_time) values ('5',  '1', timestamp'2021-08-11 05:28:44');
insert into Calls (caller_id, recipient_id, call_time) values ('8',  '3', timestamp'2021-08-17 04:04:15');
insert into Calls (caller_id, recipient_id, call_time) values ('11', '3', timestamp'2021-08-17 13:07:00');
insert into Calls (caller_id, recipient_id, call_time) values ('8', '11', timestamp'2021-08-17 22:22:22');
*/
-- Write an SQL query to report the IDs of the users whose first and 
-- last calls on any day were with the same person. Calls are counted 
-- regardless of being the caller or the recipient.
-- Return the result table in any order.


-- Postgres
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, date_trunc('day', call_time) 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, date_trunc('day', call_time) 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select unnest(array[caller_id, recipient_id]) user_id,
                       unnest(array[recipient_id, caller_id]) talk_to_id,
                       unnest(array[call_time, call_time]) call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
;


-- Postgres
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, date_trunc('day', call_time) 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, date_trunc('day', call_time) 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select caller_id user_id, recipient_id talk_to_id, call_time
                  from calls
                 union all
                select recipient_id, caller_id, call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
;

-- Postgres
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, call_time::date
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, call_time::date
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select caller_id user_id, recipient_id talk_to_id, call_time
                  from calls
                 union all
                select recipient_id, caller_id, call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
;

-- Postgres, MySQL, but not for Oracle
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, cast(call_time as date)
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, cast(call_time as date)
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select caller_id user_id, recipient_id talk_to_id, call_time
                  from calls
                 union all
                select recipient_id, caller_id, call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
;

-- MySQL
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, date(call_time)
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, date(call_time)
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select caller_id user_id, recipient_id talk_to_id, call_time
                  from calls
                 union all
                select recipient_id, caller_id, call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
;

-- Oracle
select distinct user_id
  from (
        select user_id,
               first_value(talk_to_id) over (partition by user_id, trunc(call_time, 'dd') 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) first_talk_to,
               last_value(talk_to_id)  over (partition by user_id, trunc(call_time, 'dd') 
                                             order by call_time 
                                             rows between unbounded preceding and 
                                                          unbounded following) last_talk_to
          from (
                select caller_id user_id, recipient_id talk_to_id, call_time
                  from calls
                 union all
                select recipient_id, caller_id, call_time
                  from calls
               ) c
       ) c1
 where first_talk_to = last_talk_to
 ;
