-- Postgres, Oracle, MySQL, SQLServer
select product_name, year, price
  from (
        select sale_id, product_name, year, price
          from Sales s
          join Product p
            on s.product_id = p.product_id
         group by sale_id, product_name, year, price
       ) s;
