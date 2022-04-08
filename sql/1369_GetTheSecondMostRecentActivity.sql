-- Postgres, MySQL
select username,
       activity,
       startDate,
       endDate
  from (
        select username,
               activity,
               startDate,
               endDate,
               row_number() over (partition by username order by startdate) rn
          from (
                select username,
                       activity,
                       startDate,
                       endDate,
                       row_number() over (partition by username order by startdate desc) rn
                  from UserActivity a
               ) a
         where rn <= 2
       ) a
 where rn = 1
 ;

-- Oracle
select username,
       activity,
       to_char(startDate, 'yyyy-mm-dd') startDate,
       to_char(endDate, 'yyyy-mm-dd') endDate
  from (
        select username,
               activity,
               startDate,
               endDate,
               row_number() over (partition by username order by startdate) rn
          from (
                select username,
                       activity,
                       startDate,
                       endDate,
                       row_number() over (partition by username order by startdate desc) rn
                  from UserActivity a
               ) a
         where rn <= 2
       ) a
 where rn = 1
 ;
 