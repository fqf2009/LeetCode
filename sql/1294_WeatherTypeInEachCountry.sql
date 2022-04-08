-- Postgres, Oracle, MySQL
select country_name,
       case when avg_temp <= 15 then 'Cold'
            when avg_temp >= 25 then 'Hot'
            else 'Warm'
       end weather_type
  from (
        select c.country_id,
               c.country_name,
               avg(weather_state) avg_temp
          from Countries c
          join Weather w
            on c.country_id = w.country_id
         where day between date'2019-11-01' and date'2019-11-30'
         group by c.country_id,
                  c.country_name
       ) t
       ;
