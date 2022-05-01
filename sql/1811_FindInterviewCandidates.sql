/*
Drop table If Exists Contests;
Drop table If Exists Users;
Create table If Not Exists Contests (contest_id int, gold_medal int, silver_medal int, bronze_medal int);
Create table If Not Exists Users (user_id int, mail varchar(50), name varchar(30));
Truncate table Contests;
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('190', '1', '5', '2');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('191', '2', '3', '5');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('192', '5', '2', '3');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('193', '1', '3', '5');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('194', '4', '5', '2');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('195', '4', '2', '1');
insert into Contests (contest_id, gold_medal, silver_medal, bronze_medal) values ('196', '1', '5', '2');
Truncate table Users;
insert into Users (user_id, mail, name) values ('1', 'sarah@leetcode.com', 'Sarah');
insert into Users (user_id, mail, name) values ('2', 'bob@leetcode.com', 'Bob');
insert into Users (user_id, mail, name) values ('3', 'alice@leetcode.com', 'Alice');
insert into Users (user_id, mail, name) values ('4', 'hercy@leetcode.com', 'Hercy');
insert into Users (user_id, mail, name) values ('5', 'quarz@leetcode.com', 'Quarz');
*/
-- Write an SQL query to report the name and the mail of all interview candidates. 
-- A user is an interview candidate if at least one of these two conditions is true:
--   The user won any medal in three or more consecutive contests.
--   The user won the gold medal in three or more different contests (not necessarily consecutive).
-- Return the result table in any order.


-- Postgres
select name, 
       mail
  from (
        select gold_medal user_id
          from Contests
         group by gold_medal
        having count(*) >= 3
         union
        select user_id
          from (
                select user_id,
                       contest_id,
                       case when lag(contest_id, 1) over (partition by user_id order by contest_id) = contest_id - 1 and
                                 lag(contest_id, 2) over (partition by user_id order by contest_id) = contest_id - 2
                                 then 'Y'
                            else 'N'
                        end cont_3
                  from (
                        select contest_id,
                               unnest(array[gold_medal, silver_medal, bronze_medal]) user_id
                         from Contests
                       ) c
                 ) c2
         where cont_3 = 'Y'
       ) c
  join users u
    on u.user_id = c.user_id
;

-- ERROR: column "user_id" does not exist
-- However, this does not work, i.e.,, other column in same "select list" 
-- cannot access this new unnested column, but "group by" and "having" can.
select name, 
       mail
  from (
        select gold_medal user_id
          from Contests
         group by gold_medal
        having count(*) >= 3
         union
        select user_id
          from (
                select unnest(array[gold_medal, silver_medal, bronze_medal]) user_id,
                       contest_id,
                       case when lag(contest_id, 1) over (partition by user_id order by contest_id) = contest_id - 1 and
                                 lag(contest_id, 2) over (partition by user_id order by contest_id) = contest_id - 2
                                 then 'Y'
                            else 'N'
                        end cont_3
                  from Contests
                 ) c
         where cont_3 = 'Y'
       ) c
  join users u
    on u.user_id = c.user_id
;

-- Postgres, MySQL, Oracle
select name, 
       mail
  from (
        select gold_medal user_id
          from Contests
         group by gold_medal
        having count(*) >= 3
         union    -- to unique the result set
        select user_id
          from (
                select user_id,
                       case when lag(contest_id, 1) over (partition by user_id order by contest_id) = contest_id - 1 and
                                 lag(contest_id, 2) over (partition by user_id order by contest_id) = contest_id - 2
                                 then 'Y'
                            else 'N'
                        end cont_3
                  from (
                        select contest_id,
                               gold_medal user_id
                          from Contests
                         union all
                        select contest_id,
                               silver_medal user_id
                          from Contests
                         union all
                        select contest_id,
                               bronze_medal user_id
                          from Contests
                         order by user_id, contest_id
                       ) c
                 ) c2
         where cont_3 = 'Y'
       ) c
  join users u
    on u.user_id = c.user_id
;
