-- Postgres, Oracle, MySQL, SQLServer
select distinct l.page_id recommended_page 
  from (
        select user1_id user_id
          from friendship
         where user2_id = 1
         union
        select user2_id
          from friendship
         where user1_id = 1
       ) f
  join likes l
    on l.user_id = f.user_id
 where not exists (
        select null
          from likes l2
         where l2.page_id = l.page_id
           and l2.user_id = 1
       )
       ;
