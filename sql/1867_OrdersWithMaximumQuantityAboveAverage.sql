-- Postgres, Oracle, MySQL, SQL Server
select order_id
  from (
        select order_id,
               sum(quantity) / count(*) avg_qyt,
               max(quantity)    max_qty,
               max(sum(quantity) / count(*)) over () max_avg_qty
          from OrdersDetails o
         group by order_id
       ) o
 where max_qty > max_avg_qty
 ;
