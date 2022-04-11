/*
Drop table If Exists Customers;
Drop table If Exists Orders;
Create table If Not Exists Customers (customer_id int, customer_name varchar(30));
Create table If Not Exists Orders (order_id int, customer_id int, product_name varchar(30));
Truncate table Customers;
insert into Customers (customer_id, customer_name) values ('1', 'Daniel');
insert into Customers (customer_id, customer_name) values ('2', 'Diana');
insert into Customers (customer_id, customer_name) values ('3', 'Elizabeth');
insert into Customers (customer_id, customer_name) values ('4', 'Jhon');
Truncate table Orders;
insert into Orders (order_id, customer_id, product_name) values ('10', '1', 'A');
insert into Orders (order_id, customer_id, product_name) values ('20', '1', 'B');
insert into Orders (order_id, customer_id, product_name) values ('30', '1', 'D');
insert into Orders (order_id, customer_id, product_name) values ('40', '1', 'C');
insert into Orders (order_id, customer_id, product_name) values ('50', '2', 'A');
insert into Orders (order_id, customer_id, product_name) values ('60', '3', 'A');
insert into Orders (order_id, customer_id, product_name) values ('70', '3', 'B');
insert into Orders (order_id, customer_id, product_name) values ('80', '3', 'D');
insert into Orders (order_id, customer_id, product_name) values ('90', '4', 'C');
*/

-- Write an SQL query to report the customer_id and customer_name of customers who
-- bought products Both "A" and "B" but did not buy the product "C" since we want 
-- to recommend them to purchase this product.
-- Return the result table ordered by customer_id.


-- Postgres
select c.customer_id,
       customer_name
  from orders o
  join Customers c
    on c.customer_id = o.customer_id
 group by c.customer_id,
          customer_name
having array_agg(product_name::text) @> array['A', 'B']
   and not array_agg(product_name::text) @> array['C']
   ;

-- Postgres
select c.customer_id,
       customer_name
  from orders o
  join Customers c
    on c.customer_id = o.customer_id
 where o.product_name in ('A', 'B', 'C')
 group by c.customer_id,
          customer_name
having string_agg(product_name, ',' order by product_name) = 'A,B'
;

-- MySQL
select c.customer_id,
       customer_name
  from orders o
  join Customers c
    on c.customer_id = o.customer_id
 where o.product_name in ('A', 'B', 'C')
 group by c.customer_id,
          customer_name
having group_concat(distinct product_name order by product_name separator ',') = 'A,B'
 order by o.customer_id;
;

-- Postgres
-- MySQL does not support INTERSECT and EXCEPT, can use IN, NOT IN to simulate
select c.customer_id,
       customer_name
  from customers c
  join (
        select customer_id
          from orders
         where product_name = 'A'
        intersect
        select customer_id
          from orders
         where product_name = 'B'
        except
        select customer_id
          from orders
         where product_name = 'C'
       ) o
    on c.customer_id = o.customer_id
 order by 1
 ;

-- Oracle - use MINUS as EXCEPT
select c.customer_id,
       customer_name
  from customers c
  join (
        select customer_id
          from orders
         where product_name = 'A'
        intersect
        select customer_id
          from orders
         where product_name = 'B'
         minus
        select customer_id
          from orders
         where product_name = 'C'
       ) o
    on c.customer_id = o.customer_id
 order by 1
 ;

-- All DBs
with a as (
    select distinct customer_id
      from orders
     where product_name = 'A'
),
b as (
    select distinct customer_id
      from orders
     where product_name = 'B'
),
c as (
    select distinct customer_id
      from orders
     where product_name = 'C'
)
select c.customer_id,
       customer_name
  from Customers c
  join a
    on a.customer_id = c.customer_id
  join b
    on b.customer_id = a.customer_id 
 where c.customer_id not in (
            select customer_id
              from c
       )
 order by 1
 ;


-- either A or B, but not C - not meet the requirement
select distinct o.customer_id,
       customer_name
  from orders o
  join Customers c
    on c.customer_id = o.customer_id 
 where product_name in ('A', 'B')
   and not exists (
            select null
              from orders o1
             where o1.customer_id = o.customer_id
               and o1.product_name = 'C'
       )
 order by o.customer_id;
