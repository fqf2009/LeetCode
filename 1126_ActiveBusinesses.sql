-- Postgres, Oracle, MySQL, SQLServer
select business_id
  from (
        select business_id,
               occurences,
               avg(occurences) over (partition by event_type) avg_occurences
          from Events
       ) e
 where occurences > avg_occurences
 group by business_id
having count(*) > 1
;
