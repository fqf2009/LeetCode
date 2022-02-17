/*
Drop table If Exists Customer;
Drop table If Exists  Product;
Create table Customer (customer_id int, product_key int);
Create table Product (product_key int);
Truncate table Customer;
insert into Customer (customer_id, product_key) values ('1', '5');
insert into Customer (customer_id, product_key) values ('2', '6');
insert into Customer (customer_id, product_key) values ('3', '5');
insert into Customer (customer_id, product_key) values ('3', '6');
insert into Customer (customer_id, product_key) values ('1', '6');
Truncate table Product;
insert into Product (product_key) values ('5');
insert into Product (product_key) values ('6');
*/
-- Write an SQL query to report the customer ids from the Customer
-- table that bought all the products in the Product table.
-- Return the result table in any order.
-- The query result format is in the following example.

-- postgres, oracle, mysql
select customer_id 
  from customer c
 group by customer_id
having count(distinct product_key) = (select count(*) from Product)
;
