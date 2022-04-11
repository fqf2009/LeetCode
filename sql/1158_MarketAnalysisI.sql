-- Postgres, Oracle
select u.user_id buyer_id,
       to_char(join_date, 'yyyy-mm-dd') join_date,
       coalesce(orders_in_2019, 0) orders_in_2019
  from Users u
  left join (
            select buyer_id,
                   count(*) orders_in_2019
              from Orders o
             where extract(year from order_date) = 2019
             group by buyer_id
             ) o
    on u.user_id = o.buyer_id
    ;

-- MySQL
select u.user_id buyer_id,
       join_date,
       coalesce(orders_in_2019, 0) orders_in_2019
  from Users u
  left join (
            select buyer_id,
                   count(*) orders_in_2019
              from Orders o
             where year(order_date) = 2019
             group by buyer_id
             ) o
    on u.user_id = o.buyer_id
    ;
