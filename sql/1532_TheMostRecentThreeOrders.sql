-- Postgres, MySQL, SQL Server
select c.name customer_name,
       c.customer_id,
       order_id,
       order_date
  from customers c
  join (
        select customer_id,
               order_id,
               order_date,
               row_number() over (partition by customer_id
                                  order by order_date desc) rn
          from orders o
       ) o
    on c.customer_id = o.customer_id
 where rn <= 3
 order by c.name,
          c.customer_id,
          order_date desc
 ;
  
-- Oracle
select c.name customer_name,
       c.customer_id,
       order_id,
       to_char(order_date, 'yyyy-mm-dd') order_date
  from customers c
  join (
        select customer_id,
               order_id,
               order_date,
               row_number() over (partition by customer_id
                                  order by order_date desc) rn
          from orders o
       ) o
    on c.customer_id = o.customer_id
 where rn <= 3
 order by c.name,
          c.customer_id,
          order_date desc
 ;
  