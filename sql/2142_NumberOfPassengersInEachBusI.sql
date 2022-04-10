/*
Drop table If Exists Buses;
Drop table If Exists Passengers;
Create table If Not Exists Buses (bus_id int, arrival_time int);
Create table If Not Exists Passengers (passenger_id int, arrival_time int);
Truncate table Buses;
insert into Buses (bus_id, arrival_time) values ('1', '2');
insert into Buses (bus_id, arrival_time) values ('2', '4');
insert into Buses (bus_id, arrival_time) values ('3', '7');
Truncate table Passengers;
insert into Passengers (passenger_id, arrival_time) values ('11', '1');
insert into Passengers (passenger_id, arrival_time) values ('12', '5');
insert into Passengers (passenger_id, arrival_time) values ('13', '6');
insert into Passengers (passenger_id, arrival_time) values ('14', '7');
*/
-- Buses and passengers arrive at the LeetCode station. If a bus arrives 
-- at the station at time tbus and a passenger arrived at time tpassenger 
-- where tpassenger <= tbus and the passenger did not catch any bus, the 
-- passenger will use that bus.
-- Write an SQL query to report the number of users that used each bus.
-- Return the result table ordered by bus_id in ascending order.

-- Postgres, Oracle, MySQL, SQL Server
select bus_id,
       count(passenger_id) passengers_cnt 
  from (
        select bus_id,
               lag(arrival_time) over (order by arrival_time) prev_arrival,
               arrival_time
          from buses b
       ) b
  left join Passengers p
    on (p.arrival_time > coalesce(b.prev_arrival, -1)) and
       p.arrival_time <= b.arrival_time
 group by bus_id
 order by bus_id
 ;
