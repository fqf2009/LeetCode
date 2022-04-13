/*
Drop table If Exists Customers;
Drop table If Exists Orders;
Create table If Not Exists Customers (customer_id int, name varchar(10));
Create table If Not Exists Orders (order_id int, order_date date, customer_id int, cost int);
Truncate table Customers;
insert into Customers (customer_id, name) values ('1', 'Winston');
insert into Customers (customer_id, name) values ('2', 'Jonathan');
insert into Customers (customer_id, name) values ('3', 'Annabelle');
insert into Customers (customer_id, name) values ('4', 'Marwan');
insert into Customers (customer_id, name) values ('5', 'Khaled');
Truncate table Orders;
insert into Orders (order_id, order_date, customer_id, cost) values ('1', '2020-07-31', '1', '30');
insert into Orders (order_id, order_date, customer_id, cost) values ('2', '2020-7-30', '2', '40');
insert into Orders (order_id, order_date, customer_id, cost) values ('3', '2020-07-31', '3', '70');
insert into Orders (order_id, order_date, customer_id, cost) values ('4', '2020-07-29', '4', '100');
insert into Orders (order_id, order_date, customer_id, cost) values ('5', '2020-06-10', '1', '1010');
insert into Orders (order_id, order_date, customer_id, cost) values ('6', '2020-08-01', '2', '102');
insert into Orders (order_id, order_date, customer_id, cost) values ('7', '2020-08-01', '3', '111');
insert into Orders (order_id, order_date, customer_id, cost) values ('8', '2020-08-03', '1', '99');
insert into Orders (order_id, order_date, customer_id, cost) values ('9', '2020-08-07', '2', '32');
insert into Orders (order_id, order_date, customer_id, cost) values ('10', '2020-07-15', '1', '2');
*/
-- Write an SQL query to find the most recent three orders of each user.
-- If a user ordered less than three orders, return all of their orders.
-- Return the result table ordered by customer_name in ascending order 
-- and in case of a tie by the customer_id in ascending order. If there 
-- is still a tie, order them by order_date in descending order.


-- Postgres, MySQL, SQL Server
select c.name customer_name,
       c.customer_id,
       order_id,
       order_date
  from customers c
  join (
        select customer_id,
               order_id,
               order_date,
               row_number() over (partition by customer_id
                                  order by order_date desc) rn
          from orders o
       ) o
    on c.customer_id = o.customer_id
 where rn <= 3
 order by c.name,
          c.customer_id,
          order_date desc
 ;
  
-- Oracle
select c.name customer_name,
       c.customer_id,
       order_id,
       to_char(order_date, 'yyyy-mm-dd') order_date
  from customers c
  join (
        select customer_id,
               order_id,
               order_date,
               row_number() over (partition by customer_id
                                  order by order_date desc) rn
          from orders o
       ) o
    on c.customer_id = o.customer_id
 where rn <= 3
 order by c.name,
          c.customer_id,
          order_date desc
 ;
  