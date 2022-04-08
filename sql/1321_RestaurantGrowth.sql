/*
Drop table If Exists Customer;
Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int);
Truncate table Customer;
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100');
insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120');
insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140');
insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150');
insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80');
insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150');
*/
-- You are the restaurant owner and you want to analyze a possible expansion 
-- (there will be at least one customer every day).
-- Write an SQL query to compute the moving average of how much the customer 
-- paid in a seven days window (i.e., current day + 6 days before). 
-- average_amount should be rounded to two decimal places.
-- Return result table ordered by visited_on in ascending order.

-- Postgres
select visited_on,
       amount,
       average_amount
  from (
        select visited_on,
               sum(sum(amount)) over (order by visited_on 
                    rows between 6 preceding and current row) amount,
               min(visited_on) over () earliest_visit,
               round(avg(sum(amount)) over (order by visited_on
                    rows between 6 preceding and current row), 2) average_amount
          from Customer
         group by visited_on
       ) c
 where visited_on >= earliest_visit + 6
 order by visited_on
 ;

-- Oracle
select to_char(visited_on, 'yyyy-mm-dd') visited_on,
       amount,
       average_amount
  from (
        select visited_on,
               sum(sum(amount)) over (order by visited_on 
                    rows between 6 preceding and current row) amount,
               min(visited_on) over () earliest_visit,
               round(avg(sum(amount)) over (order by visited_on
                    rows between 6 preceding and current row), 2) average_amount
          from Customer
         group by visited_on
       ) c
 where visited_on >= earliest_visit + 6
 order by visited_on
 ;
 
-- MySQL
select visited_on,
       amount,
       average_amount
  from (
        select visited_on,
               sum(sum(amount)) over (order by visited_on 
                    rows between 6 preceding and current row) amount,
               min(visited_on) over () earliest_visit,
               round(avg(sum(amount)) over (order by visited_on
                    rows between 6 preceding and current row), 2) average_amount
          from Customer
         group by visited_on
       ) c
  where visited_on >= date_add(earliest_visit, interval '6' day)
 order by visited_on
 ;
