/*
drop table if exists RequestAccepted;
Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null);
Truncate table RequestAccepted;
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '2', '2016/06/03');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('1', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('2', '3', '2016/06/08');
insert into RequestAccepted (requester_id, accepter_id, accept_date) values ('3', '4', '2016/06/09');
*/

-- Write an SQL query to find the people who have the most friends and the most friends number.
-- The test cases are generated so that only one person has the most friends.

-- Postgres, MySQL
select id,
       count(*) num
  from (
        select requester_id id
          from RequestAccepted
         union all
        select accepter_id  id
          from RequestAccepted
       ) r
 group by id
 order by num desc
 limit 1
 ;

-- Postgres
select id,
       count(*) num
  from (
        select unnest(array[requester_id, accepter_id]) id
          from RequestAccepted
       ) r
 group by id
 order by num desc
 limit 1
 ;

-- Postgres, even simpler
select unnest(array[requester_id, accepter_id]) id,
       count(*) num
  from RequestAccepted
 group by id
 order by num desc
 limit 1
 ;

 -- Oracle
 select id,
       num
  from (
        select id,
               count(*) num
          from (
                select requester_id id
                  from RequestAccepted
                 union all
                select accepter_id  id
                  from RequestAccepted
               ) r
         group by id
         order by 2 desc
       )
 where rownum = 1
 ;
 

 -- If there are duplicates
 select id1 id,
        count(*) num
  from (
        select requester_id id1,
               accepter_id  id2
          from RequestAccepted
         union
        select accepter_id id1,
               accepter_id id2
          from RequestAccepted
       ) r
 group by id1
 order by num desc
 limit 1
 ;
