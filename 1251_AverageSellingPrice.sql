-- Postgres
select p.product_id,
       round(sum(p.price*s.units)::numeric / sum(s.units), 2) average_price
  from UnitsSold s
  join prices p
    on p.product_id = s.product_id
   and s.purchase_date between p.start_date and p.end_date
 group by p.product_id
 ;

-- Oracle, MySQL
select p.product_id,
       round(sum(p.price*s.units) / sum(s.units), 2) average_price
  from UnitsSold s
  join prices p
    on p.product_id = s.product_id
   and s.purchase_date between p.start_date and p.end_date
 group by p.product_id
 ;

-- SQL Server
select p.product_id,
       round(cast(sum(p.price*s.units) as numeric)/sum(s.units), 2) average_price
  from UnitsSold s
  join prices p
    on p.product_id = s.product_id
   and s.purchase_date between p.start_date and p.end_date
 group by p.product_id
 ;
