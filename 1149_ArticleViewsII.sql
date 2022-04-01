-- Postgres, Oracle, MySQL
select distinct viewer_id id
  from (
        select viewer_id,
               view_date
          from views
         group by viewer_id,
                  view_date
        having count(distinct article_id) > 1
       ) v
 order by 1
 ;
