-- The cancellation rate is computed by dividing the number of canceled 
-- (by client or driver) requests with unbanned users by the total number 
-- of requests with unbanned users on that day.

-- Write a SQL query to find the cancellation rate of requests with unbanned 
-- users (both client and driver must not be banned) each day between 
-- "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

-- Return the result table in any order.
/*
Drop table if exists Trips;
Drop table if exists Users;
Create table If Not Exists Trips (id int, client_id int, driver_id int, city_id int, status varchar(50), request_at varchar(50));
Create table If Not Exists Users (users_id int, banned varchar(50), role varchar(50));
Truncate table Trips;
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('1', '1', '10', '1', 'completed', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('3', '3', '12', '6', 'completed', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('5', '1', '10', '1', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('6', '2', '11', '6', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('7', '3', '12', '6', 'completed', '2013-10-02');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('8', '2', '12', '12', 'completed', '2013-10-03');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('9', '3', '10', '12', 'completed', '2013-10-03');
insert into Trips (id, client_id, driver_id, city_id, status, request_at) values ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03');
Truncate table Users;
insert into Users (users_id, banned, role) values ('1', 'No', 'client');
insert into Users (users_id, banned, role) values ('2', 'Yes', 'client');
insert into Users (users_id, banned, role) values ('3', 'No', 'client');
insert into Users (users_id, banned, role) values ('4', 'No', 'client');
insert into Users (users_id, banned, role) values ('10', 'No', 'driver');
insert into Users (users_id, banned, role) values ('11', 'No', 'driver');
insert into Users (users_id, banned, role) values ('12', 'No', 'driver');
insert into Users (users_id, banned, role) values ('13', 'No', 'driver');
*/

-- For Oracle and Postgres
-- Note: Postgres does not convert int to float automatically. (Oracle does)
--       It is rediculous that request_at is varchar(50) type.
select t.request_at "Day",
       round(sum(case when status = 'completed' then 0.0 else 1.0 end) / count(*), 2) "Cancellation Rate"
  from trips t 
  join users c
    on t.client_id = c.users_id and c.role = 'client'
  join users d 
    on t.driver_id = d.users_id and d.role = 'driver'
 where c.banned = 'No' and 
       d.banned = 'No' and
       to_date(t.request_at, 'yyyy-mm-dd') between date'2013-10-01' and date'2013-10-03'
 group by t.request_at
 ;

-- MySQL
select t.request_at "Day",
       round(sum(case when status = 'completed' then 0.0 else 1.0 end) / count(*), 2) "Cancellation Rate"
  from trips t 
  join users c
    on t.client_id = c.users_id and c.role = 'client'
  join users d 
    on t.driver_id = d.users_id and d.role = 'driver'
 where c.banned = 'No' and 
       d.banned = 'No' and
       str_to_date(t.request_at, '%Y-%m-%d') between date'2013-10-01' and date'2013-10-03'
 group by t.request_at
 ;

-- T-SQL
select t.request_at "Day",
       round(sum(case when status = 'completed' then 0.0 else 1.0 end) / count(*), 2) "Cancellation Rate"
  from trips t 
  join users c
    on t.client_id = c.users_id and c.role = 'client'
  join users d 
    on t.driver_id = d.users_id and d.role = 'driver'
 where c.banned = 'No' and 
       d.banned = 'No' and
       convert(date, t.request_at, 23) between '2013-10-01' and '2013-10-03'
 group by t.request_at
 ;
