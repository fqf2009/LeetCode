-- Postgres, MySQL, SQL Server
select gender, 
       day,
       sum(sum(score_points)) over (partition by gender order by day) total
  from scores
 group by gender, day
 order by gender, day
 ;

-- Oracle
select gender, 
       to_char(day, 'yyyy-mm-dd') day,
       sum(sum(score_points)) over (partition by gender order by day) total
  from scores
 group by gender, day
 order by gender, day
 ;
