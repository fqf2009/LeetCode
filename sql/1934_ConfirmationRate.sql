-- Postgres, Oracle, MySQL 
select s.user_id,
       coalesce(c.confirmation_rate, 0) confirmation_rate
  from Signups s
  left join (
             select user_id,
                    round(sum(case when action = 'confirmed' then 1.0 else 0.0 end) /
                          count(*), 2) confirmation_rate
               from Confirmations c
              group by user_id
            ) c
         on s.user_id = c.user_id
         ;
