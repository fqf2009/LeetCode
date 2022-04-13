/*
Drop table If Exists Movies;
Drop table If Exists Users;
Drop table If Exists MovieRating;
Create table If Not Exists Movies (movie_id int, title varchar(30));
Create table If Not Exists Users (user_id int, name varchar(30));
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);
Truncate table Movies;
insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');
Truncate table Users;
insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'James');
Truncate table MovieRating;
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');
*/
-- Write an SQL query to:
-- Find the name of the user who has rated the greatest number of movies. 
-- In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. 
-- In case of a tie, return the lexicographically smaller movie name.


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
