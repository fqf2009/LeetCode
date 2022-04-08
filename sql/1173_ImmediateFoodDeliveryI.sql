-- is it possible the table is empty?
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
