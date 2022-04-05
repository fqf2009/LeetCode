-- Postgres, Oracle, MySQL, SQLServer
select stock_name,
       sum(price - prev_price) capital_gain_loss
  from (
        select stock_name,
               operation,
               operation_day,
               price,
               lag(price) over (partition by stock_name
                                order by operation_day) prev_price
          from Stocks s
       ) s
 where operation = 'Sell'
 group by stock_name
 ;
