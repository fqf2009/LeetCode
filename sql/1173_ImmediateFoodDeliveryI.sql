-- Postgres
select round(sum(case when order_date = customer_pref_delivery_date
                            then 1 
                      else 0
                 end)::numeric
       / count(*) * 100, 2) immediate_percentage
  from delivery;

-- Oracle, MySQL
select round(sum(case when order_date = customer_pref_delivery_date
                            then 1 
                      else 0
                 end)
       / count(*) * 100, 2) immediate_percentage
  from delivery;

-- is it possible the table is empty?
select round(case when total_cnt = 0 then 0.0
                  else immediate_cnt::numeric / total_cnt
             end * 100, 2)  immediate_percentage
  from (
        select sum(case when order_date = customer_pref_delivery_date then 1 
                        else 0
                   end)     immediate_cnt,
               count(*)     total_cnt
          from delivery
       ) d
       ;
