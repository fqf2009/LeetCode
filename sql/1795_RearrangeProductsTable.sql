/*
Drop table If Exists Products;
Create table If Not Exists Products (product_id int, store1 int, store2 int, store3 int);
Truncate table Products;
insert into Products (product_id, store1, store2, store3) values ('0', '95', '100', '105');
insert into Products (product_id, store1, store2, store3) values ('1', '70', NULL, '80');
*/
-- Write an SQL query to rearrange the Products table so that each row has 
-- (product_id, store, price). If a product is not available in a store, 
-- do not include a row with that product_id and store combination in the 
-- result table.
-- Return the result table in any order.

-- Postgres
select product_id,
       store,
       price
  from (
        select product_id,
               unnest(array['store1', 'store2', 'store3']) as store,
               unnest(array[store1, store2, store3]) as price
          from products
       ) p
 where price is not null
;

-- Postgres, Oracle, MySQL, SQLServer
-- Scan table multiple times
select product_id,
       'store1' store,
       store1 price
  from Products
 where store1 is not null
 union all
select product_id,
       'store2' store,
       store2 price
  from Products
 where store2 is not null
 union all
select product_id,
       'store3' store,
       store3 price
  from Products
 where store3 is not null
 ;

 -- Oracle
 -- Note exclude nulls is the default, use include nulls to get null
 select product_id,
        store,
        price
   from Products
unpivot exclude nulls (price for store in (
            store1 as 'store1', store2 as 'store2', store3 as 'store3')
        )
;

-- SQL Server
-- no column1 as 'value1', but unpivot(...) as ... is necessary
 select product_id,
        store,
        price
   from Products
unpivot (price for store in (store1, store2, store3)) as upvt
;
