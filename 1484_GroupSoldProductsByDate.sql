/*
Drop table If Exists Activities;
Create table If Not Exists Activities (sell_date date, product varchar(20));
Truncate table Activities;
insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');
*/
-- Write an SQL query to find for each date the number of different 
-- products sold and their names.
-- The sold products names for each date should be sorted lexicographically.
-- Return the result table ordered by sell_date.

-- Postgres
select sell_date,
       count(distinct product) num_sold,
       string_agg(distinct product, ',' order by product) products
  from Activities
 group by sell_date
 order by sell_date
 ;

-- MySQL
select sell_date,
       count(distinct product) num_sold,
       group_concat(distinct product order by product separator ',') products
  from Activities
 group by sell_date
 order by sell_date
 ;

-- Oracle
select to_char(sell_date, 'yyyy-mm-dd') sell_date,
       count(distinct product) num_sold,
       listagg(product, ',') within group (order by product) products
  from (
        select distinct sell_date,
               product
          from Activities
       ) p
 group by sell_date
 order by sell_date
 ;

-- SQL Server
select sell_date,
       count(distinct product) num_sold,
       string_agg(product, ',') within group (order by product) products
  from (
        select distinct sell_date,
               product
          from Activities
       ) p
 group by sell_date
 order by sell_date
 ;
