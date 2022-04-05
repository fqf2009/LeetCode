-- Postgres, Oracle, MySQL
select p.product_name,
       o.unit
  from (
        select o.product_id,
               sum(unit) unit
          from orders o
         where order_date between date'2020-02-01' and date'2020-02-29'
         group by o.product_id
        having sum(unit) >= 100
       ) o
  join Products p
    on o.product_id = p.product_id
 ;
