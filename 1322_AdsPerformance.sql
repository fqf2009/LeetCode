-- Postgres, Oracle, MySQL, SQLServer
select ad_id,
       round(case when viewed + clicked = 0 then 0.0
                  else clicked * 100.0 / (viewed + clicked)
              end, 2) ctr
  from (
        select ad_id,
               sum(case when action = 'Clicked' then 1 else 0 end) clicked,
               sum(case when action = 'Viewed' then 1 else 0 end) viewed
          from ads
         group by ad_id
       ) a
 order by 2 desc,
          ad_id
 ;
