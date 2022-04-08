-- Postgres, MySQL, SQL Server
select a.sale_date, 
       a.sold_num - o.sold_num diff
  from (
        select sale_date, sold_num
          from sales
         where fruit = 'apples'
       ) a
  join (
        select sale_date, sold_num
          from sales
         where fruit = 'oranges'
       ) o
    on a.sale_date = o.sale_date
 order by a.sale_date
 ;

-- Oracle
select to_char(a.sale_date, 'yyyy-mm-dd') sale_date,
       a.sold_num - o.sold_num diff
  from (
        select sale_date, sold_num
          from sales
         where fruit = 'apples'
       ) a
  join (
        select sale_date, sold_num
          from sales
         where fruit = 'oranges'
       ) o
    on a.sale_date = o.sale_date
 order by a.sale_date
 ;
