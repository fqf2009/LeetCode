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
