/*
Drop table If Exists Customers;
Drop table If Exists Product;
Drop table If Exists Orders;
Create table If Not Exists Customers (customer_id int, name varchar(30), country varchar(30));
Create table If Not Exists Product (product_id int, description varchar(30), price int);
Create table If Not Exists Orders (order_id int, customer_id int, product_id int, order_date date, quantity int);
Truncate table Customers;
insert into Customers (customer_id, name, country) values ('1', 'Winston', 'USA');
insert into Customers (customer_id, name, country) values ('2', 'Jonathan', 'Peru');
insert into Customers (customer_id, name, country) values ('3', 'Moustafa', 'Egypt');
Truncate table Product;
insert into Product (product_id, description, price) values ('10', 'LC Phone', '300');
insert into Product (product_id, description, price) values ('20', 'LC T-Shirt', '10');
insert into Product (product_id, description, price) values ('30', 'LC Book', '45');
insert into Product (product_id, description, price) values ('40', 'LC Keychain', '2');
Truncate table Orders;
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('1', '1', '10', '2020-06-10', '1');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('2', '1', '20', '2020-07-01', '1');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('3', '1', '30', '2020-07-08', '2');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('4', '2', '10', '2020-06-15', '2');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('5', '2', '40', '2020-07-01', '10');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('6', '3', '20', '2020-06-24', '2');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('7', '3', '30', '2020-06-25', '2');
insert into Orders (order_id, customer_id, product_id, order_date, quantity) values ('9', '3', '30', '2020-05-08', '3');
*/
-- Write an SQL query to report the customer_id and customer_name of customers 
-- who have spent at least $100 in each month of June and July 2020.
-- Return the result table in any order.

-- Postgres
select c.customer_id,
       c.name
  from customers c
  join (
        select customer_id
          from (
                select customer_id
                  from Orders o
                  join product p
                    on o.product_id = p.product_id
                 where order_date between date'2020-06-01' and date'2020-07-31'
                 group by customer_id,
                          date_trunc('month', order_date)
                having sum(price*quantity) >= 100
                ) o
          group by customer_id
         having count(*) > 1
       ) o
    on o.customer_id = c.customer_id
    ;


-- MySQL
select c.customer_id,
       c.name
  from customers c
  join (
        select customer_id
          from (
                select customer_id
                  from Orders o
                  join product p
                    on o.product_id = p.product_id
                 where order_date between date'2020-06-01' and date'2020-07-31'
                 group by customer_id,
                          extract(year_month from order_date)
                 having sum(price*quantity) >= 100
                ) o
          group by customer_id
         having count(*) > 1
       ) o
    on o.customer_id = c.customer_id
    ;


-- Oracle
select c.customer_id,
       c.name
  from customers c
  join (
        select customer_id
          from (
                select customer_id
                  from Orders o
                  join product p
                    on o.product_id = p.product_id
                 where order_date between date'2020-06-01' and date'2020-07-31'
                 group by customer_id,
                          trunc(order_date, 'mm')
                having sum(price*quantity) >= 100
                ) o
          group by customer_id
         having count(*) > 1
       ) o
    on o.customer_id = c.customer_id
    ;

-- Reducde one level of nesting
select c.customer_id,
       name
  from Customers c
  join (
        select extract(year_month from order_date),
               customer_id,
               sum(price*quantity) amount
          from orders o
          join product p
            on p.product_id = o.product_id
         where order_date between date'2020-06-01' and date'2020-07-31'
         group by extract(year_month from order_date),
                  customer_id
        having sum(price*quantity) >= 100
       ) o
    on c.customer_id = o.customer_id
 group by customer_id
having count(*) = 2
;
