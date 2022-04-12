/*
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int)
Create table If Not Exists Product (product_id int, product_name varchar(10))
Truncate table Sales
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000')
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000')
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000')
Truncate table Product
insert into Product (product_id, product_name) values ('100', 'Nokia')
insert into Product (product_id, product_name) values ('200', 'Apple')
insert into Product (product_id, product_name) values ('300', 'Samsung')
*/

-- Write an SQL query that reports the product_name, year, and price for each sale_id
-- in the Sales table.
-- Return the resulting table in any order.


-- Postgres, Oracle, MySQL, SQLServer
select product_name, year, price
  from (
        select sale_id, product_name, year, price
          from Sales s
          join Product p
            on s.product_id = p.product_id
         group by sale_id, product_name, year, price
       ) s;
