/*
Drop table If Exists Subscriptions;
Drop table If Exists Streams;
Create table If Not Exists Subscriptions (account_id int, start_date date, end_date date);
Create table If Not Exists Streams (session_id int, account_id int, stream_date date);
Truncate table Subscriptions;
insert into Subscriptions (account_id, start_date, end_date) values ('9', '2020-02-18', '2021-10-30');
insert into Subscriptions (account_id, start_date, end_date) values ('3', '2021-09-21', '2021-11-13');
insert into Subscriptions (account_id, start_date, end_date) values ('11', '2020-02-28', '2020-08-18');
insert into Subscriptions (account_id, start_date, end_date) values ('13', '2021-04-20', '2021-09-22');
insert into Subscriptions (account_id, start_date, end_date) values ('4', '2020-10-26', '2021-05-08');
insert into Subscriptions (account_id, start_date, end_date) values ('5', '2020-09-11', '2021-01-17');
Truncate table Streams;
insert into Streams (session_id, account_id, stream_date) values ('14', '9', '2020-05-16');
insert into Streams (session_id, account_id, stream_date) values ('16', '3', '2021-10-27');
insert into Streams (session_id, account_id, stream_date) values ('18', '11', '2020-04-29');
insert into Streams (session_id, account_id, stream_date) values ('17', '13', '2021-08-08');
insert into Streams (session_id, account_id, stream_date) values ('19', '4', '2020-12-31');
insert into Streams (session_id, account_id, stream_date) values ('13', '5', '2021-01-05');
*/
-- Write an SQL query to report the number of accounts that bought a 
-- subscription in 2021 but did not have any stream session.

-- Postgres, Oracle, MySQL 
select count(*) accounts_count
  from Subscriptions s
 where start_date <= date'2021-12-31' and end_date >= date'2021-01-01'
   and not exists (
        select null
          from Streams s1
         where extract(year from s1.stream_date) = 2021
           and s1.account_id = s.account_id
       )
       ;

-- Postgres
select count(*) accounts_count
  from (
        select account_id
          from Subscriptions s
         where start_date <= date'2021-12-31' and end_date >= date'2021-01-01'
        except
        select account_id 
          from streams
         where stream_date between date'2021-01-01' and date'2021-12-31'
       ) a
       ;

-- Oracle
select count(*) accounts_count
  from (
        select account_id
          from Subscriptions s
         where start_date <= date'2021-12-31' and end_date >= date'2021-01-01'
         minus
        select account_id 
          from streams
         where stream_date between date'2021-01-01' and date'2021-12-31'
       ) a
       ;
