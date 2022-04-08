-- Postgres, MySQL
select name results
  from (
        select name,
               ratings
          from users u
          join (
                select user_id,
                       count(*) ratings
                  from MovieRating r
                 group by user_id
               ) r
            on u.user_id = r.user_id
         order by ratings desc,
                  name
         limit 1
       ) u
 union all
select title results
  from (
        select title,
               rating
          from Movies m
          join (
                select movie_id,
                       avg(rating) rating
                  from MovieRating r
                 where created_at between date'2020-02-01' and date'2020-02-29'
                 group by movie_id
               ) r
            on m.movie_id = r.movie_id
         order by rating desc,
                  title
         limit 1
       ) m
;

-- Oracle
select name results
  from (
        select name,
               ratings
          from users u
          join (
                select user_id,
                       count(*) ratings
                  from MovieRating r
                 group by user_id
               ) r
            on u.user_id = r.user_id
         order by ratings desc,
                  name
       ) u
 where rownum = 1
 union all
select title results
  from (
        select title,
               rating
          from Movies m
          join (
                select movie_id,
                       avg(rating) rating
                  from MovieRating r
                 where created_at between date'2020-02-01' and date'2020-02-29'
                 group by movie_id
               ) r
            on m.movie_id = r.movie_id
         order by rating desc,
                  title
       ) m
 where rownum = 1
;
