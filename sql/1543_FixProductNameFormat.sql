-- Postgres, Oracle
select lower(trim(product_name)) product_name,
       to_char(sale_date, 'yyyy-mm') sale_date,
       count(*) total
  from sales
 group by lower(trim(product_name)),
          to_char(sale_date, 'yyyy-mm')
 order by 1, 2
          ;

-- Postgres
select lower(trim(product_name)) product_name,
       to_char(sale_date, 'yyyy-mm') sale_date,
       count(*) total
  from sales
 group by 1, 2
 order by 1, 2
          ;

-- MySQL
select lower(trim(product_name)) product_name,
       date_format(sale_date, '%Y-%m') sale_date,
       count(*) total
  from sales
 group by 1, 2
 order by 1, 2
          ;
