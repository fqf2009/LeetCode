/*
Drop table If Exists cinema;
Create table If Not Exists cinema (
    id int, movie varchar(255), description varchar(255), rating numeric(2, 1));
Truncate table cinema;
insert into cinema (id, movie, description, rating) values ('1', 'War', 'great 3D', '8.9');
insert into cinema (id, movie, description, rating) values ('2', 'Science', 'fiction', '8.5');
insert into cinema (id, movie, description, rating) values ('3', 'irish', 'boring', '6.2');
insert into cinema (id, movie, description, rating) values ('4', 'Ice song', 'Fantacy', '8.6');
insert into cinema (id, movie, description, rating) values ('5', 'House card', 'Interesting', '9.1');
*/

-- Write an SQL query to report the movies with an odd-numbered ID and a 
-- description that is not "boring".
-- Return the result table ordered by rating in descending order.
-- The query result format is in the following example.

-- postgres, oracle, mysql
select id,
       movie,
       description,
       rating
  from cinema
 where mod(id, 2) = 1
   and description <> 'boring'
 order by rating desc
 ;

-- postgres, mysql
select id,
       movie,
       description,
       rating
  from cinema
 where id % 2 = 1
   and description <> 'boring'
 order by rating desc
 ;
 
 