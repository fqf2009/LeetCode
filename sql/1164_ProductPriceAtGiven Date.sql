/*
Drop table If Exists Products;
Create table If Not Exists Products (product_id int, new_price int, change_date date);
Truncate table Products;
insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');
*/
-- Write an SQL query to find the prices of all products on 2019-08-16. 
-- Assume the price of all products before any change is 10.
-- Return the result table in any order.


-- Postgres, Oracle, MySQL
select p.product_id,
       coalesce(n.price, 10) price
  from (
        select distinct product_id
          from products
       ) p
  left join (
            select distinct product_id,
                   last_value(new_price) over (
                       partition by product_id 
                       order by change_date
                       rows between unbounded preceding
                                and unbounded following) price
              from Products
             where change_date <= date'2019-08-16'
       ) n
    on p.product_id = n.product_id
    ;

-- Postgres, Oracle, MySQL
select p.product_id,
       coalesce(n.price, 10) price
  from (
        select distinct product_id
          from products
       ) p
  left join (
            select product_id,
                   new_price price,
                   row_number() over (partition by product_id 
                                      order by change_date desc) rn
              from Products
             where change_date <= date'2019-08-16'
       ) n
    on p.product_id = n.product_id and rn = 1   -- join condition, not filter condition
    ;

-- SQL Server
select p.product_id,
       coalesce(n.price, 10) price
  from (
        select distinct product_id
          from products
       ) p
  left join (
            select distinct product_id,
                   last_value(new_price) over (
                       partition by product_id 
                       order by change_date
                       rows between unbounded preceding
                                and unbounded following) price
              from Products
             where change_date <= cast('2019-08-16' as date)
       ) n
    on p.product_id = n.product_id
    ;
