/*
drop table if exists FriendRequest;
drop table if exists RequestAccepted;
Create table If Not Exists FriendRequest (sender_id int, send_to_id int, request_date date);
Create table If Not Exists RequestAccepted (requester_id int, accepter_id int, accept_date date);
Truncate table FriendRequest;
insert into FriendRequest (sender_id, send_to_id, request_date) values ('1', '2', '2016/06/01');
insert into FriendRequest (sender_id, send_to_id, request_date) values ('1', '3', '2016/06/01');
insert into FriendRequest (sender_id, send_to_id, request_date) values ('1', '4', '2016/06/01');
insert into FriendRequest (sender_id, send_to_id, request_date) values ('2', '3', '2016/06/02');
insert into FriendRequest (sender_id, send_to_id, request_date) values ('3', '4', '2016/06/09');
Truncate table RequestAccepted;
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/10');
*/

-- Write an SQL query to find the overall acceptance rate of requests, which is the number
-- of acceptance divided by the number of requests. Return the answer rounded to 2 decimals places.

-- Note that:

-- - The accepted requests are not necessarily from the table friend_request. In this case, 
--   Count the total accepted requests (no matter whether they are in the original requests), 
--   and divide it by the number of requests to get the acceptance rate.
-- - It is possible that a sender sends multiple requests to the same receiver, and a request 
--   could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances 
--   are only counted once.
-- - If there are no requests at all, you should return 0.00 as the accept_rate.

-- Postgres can count(distinct composit_type), which Oracle cannot
select case when req = 0 then 0.0
            else round(acp::numeric / req, 2) 
        end accept_rate
  from (
         select count(distinct (sender_id, send_to_id)) req 
           from friendRequest
       ) r
 cross join (
         select count(distinct (requester_id, accepter_id)) acp 
           from RequestAccepted
       ) a
 ;

-- MySQL also can count(distinct composit_type)
select round(case when request_count = 0 then 0.0
                  else accept_count / request_count
             end, 2) accept_rate
  from (
        select count(distinct requester_id, accepter_id) accept_count
          from RequestAccepted
       ) a
  join (
        select count(distinct sender_id, send_to_id) request_count
          from FriendRequest 
       ) r
;

-- Oracle can nest aggregate function (not for postgres)
-- It make sense, think about second count as:
-- count without group by: select count(*) from t;
select case when req = 0 then 0
            else round(acp / req, 2)
        end accept_rate
  from (
         select count(count(*)) req
           from friendRequest
          group by sender_id, send_to_id
       ) r
 cross join (
         select count(count(*)) acp
           from RequestAccepted
          group by requester_id, accepter_id
       ) a
 ;


-- Oracle, MySQL, Postgres (with type conversion acp::numeric)
select case when req = 0 then 0.0
            else round(acp / req, 2)
        end accept_rate
  from (
         select count(*) req
           from (select distinct sender_id, send_to_id 
                   from friendRequest
                ) r
       ) r
 cross join (
         select count(*) acp
           from (select distinct requester_id, accepter_id
                   from RequestAccepted
                ) a
       ) a
 ;
