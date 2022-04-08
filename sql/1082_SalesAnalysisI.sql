-- Postgres, Oracle, MySQL, SQLServer
select seller_id
  from (
        select seller_id,
               dense_rank() over (order by amount desc) rk
          from (
                select seller_id, 
                       sum(price) amount
                  from Sales s
                 group by seller_id
               ) s
       ) s
 where rk = 1
 ;
