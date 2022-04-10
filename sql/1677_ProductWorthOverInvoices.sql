-- Postgres, Oracle, MySQL, SQL Server
select name,
       coalesce(rest, 0) rest,
       coalesce(paid, 0) paid,
       coalesce(canceled, 0) canceled,
       coalesce(refunded, 0) refunded
  from product p
  left join (
            select p.product_id,
                   sum(rest) rest,
                   sum(paid) paid,
                   sum(canceled) canceled,
                   sum(refunded) refunded
              from Product p
              join Invoice i
                on p.product_id = i.product_id
             group by p.product_id
       ) i
    on p.product_id = i.product_id
 order by p.name
       ;
