/*
Drop table If Exists Buses;
Drop table If Exists Passengers;
Create table If Not Exists Buses (bus_id int, arrival_time int, capacity int);
Create table If Not Exists Passengers (passenger_id int, arrival_time int);
Truncate table Buses;
insert into Buses (bus_id, arrival_time, capacity) values ('1', '2', '1');
insert into Buses (bus_id, arrival_time, capacity) values ('2', '4', '10');
insert into Buses (bus_id, arrival_time, capacity) values ('3', '7', '2');
Truncate table Passengers;
insert into Passengers (passenger_id, arrival_time) values ('11', '1');
insert into Passengers (passenger_id, arrival_time) values ('12', '1');
insert into Passengers (passenger_id, arrival_time) values ('13', '5');
insert into Passengers (passenger_id, arrival_time) values ('14', '6');
insert into Passengers (passenger_id, arrival_time) values ('15', '7');
*/
-- Buses and passengers arrive at the LeetCode station. If a bus arrives at 
-- the station at a time tbus and a passenger arrived at a time tpassenger
-- where tpassenger <= tbus and the passenger did not catch any bus, the
-- passenger will use that bus. In addition, each bus has a capacity. If at
-- the moment the bus arrives at the station there are more passengers waiting
-- than its capacity capacity, only capacity passengers will use the bus.
--
-- Write an SQL query to report the number of users that used each bus.
-- Return the result table ordered by bus_id in ascending order.


-- Postgres, MySQL
with recursive   -- !!! Note this is prior to all CTE, not just before b2
b1 as (
    select bus_id,
           capacity,
           count(passenger_id) passengers_cnt,
           row_number() over (order by b.arrival_time) rn
      from (
            select bus_id,
                   arrival_time,
                   coalesce(lag(arrival_time) over (order by arrival_time), -1) prev_arrival,
                   capacity
              from buses b
           ) b
      left join Passengers p
        on p.arrival_time > b.prev_arrival and
           p.arrival_time <= b.arrival_time
     group by bus_id,
              capacity,
              b.arrival_time
),
b2 as (     -- column list is optional
    select bus_id,
           rn,
           least(capacity, passengers_cnt) passengers_cnt,
           greatest(passengers_cnt - capacity, 0) leftover
      from b1
     where rn = 1
     union all
    select b1.bus_id,
           b1.rn,
           least(b1.capacity, b1.passengers_cnt + b2.leftover) passengers_cnt,
           greatest(b1.passengers_cnt + b2.leftover - b1.capacity, 0) leftover
      from b1
      join b2
        on b1.rn = b2.rn + 1
)
select bus_id,
       passengers_cnt
  from b2
 order by bus_id
;

-- Oracle
with b1 as (
    select bus_id,
           capacity,
           count(passenger_id) passengers_cnt,
           row_number() over (order by b.arrival_time) rn
      from (
            select bus_id,
                   arrival_time,
                   coalesce(lag(arrival_time) over (order by arrival_time), -1) prev_arrival,
                   capacity
              from buses b
           ) b
      left join Passengers p
        on p.arrival_time > b.prev_arrival and
           p.arrival_time <= b.arrival_time
     group by bus_id,
              capacity,
              b.arrival_time
),
b2 (bus_id, rn, passengers_cnt, leftover) as (   -- !!! No recursive, but column list is needed
    select bus_id,
           rn,
           least(capacity, passengers_cnt) passengers_cnt,
           greatest(passengers_cnt - capacity, 0) leftover
      from b1
     where rn = 1
     union all
    select b1.bus_id,
           b1.rn,
           least(b1.capacity, b1.passengers_cnt + b2.leftover) passengers_cnt,
           greatest(b1.passengers_cnt + b2.leftover - b1.capacity, 0) leftover
      from b1
      join b2
        on b1.rn = b2.rn + 1
)
select bus_id,
       passengers_cnt
  from b2
 order by bus_id
;
