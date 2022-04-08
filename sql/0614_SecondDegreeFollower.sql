/*
drop table if exists follow;
Create table If Not Exists Follow (followee varchar(255), follower varchar(255));
Truncate table Follow;
insert into Follow (followee, follower) values ('Alice', 'Bob');
insert into Follow (followee, follower) values ('Bob', 'Cena');
insert into Follow (followee, follower) values ('Bob', 'Donald');
insert into Follow (followee, follower) values ('Donald', 'Edward');
*/

-- A second-degree follower is a user who:
--  - follows at least one user, and
--  - is followed by at least one user.
-- Write an SQL query to report the second-degree users and the number
-- of their followers.
-- Return the result table ordered by follower in alphabetical order.

-- All DB
select follower, num
  from (
        select distinct follower
          from follow
       ) f
  join (
        select followee,
               count(*) num
          from follow
         group by followee
       ) e
    on f.follower = e.followee
 order by follower
 ;
