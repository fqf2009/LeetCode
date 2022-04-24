/*
Drop table if exists Scores;
Create table If Not Exists Scores (id int, score DECIMAL(3,2));
Truncate table Scores;
insert into Scores (id, score) values ('1', '3.5');
insert into Scores (id, score) values ('2', '3.65');
insert into Scores (id, score) values ('3', '4.0');
insert into Scores (id, score) values ('4', '3.85');
insert into Scores (id, score) values ('5', '4.0');
insert into Scores (id, score) values ('6', '3.65');
*/

-- Write an SQL query to rank the scores. The ranking should be calculated 
-- according to the following rules:
--  - The scores should be ranked from the highest to the lowest.
--  - If there is a tie between two scores, both should have the same ranking.
--  - After a tie, the next ranking number should be the next consecutive 
--    integer value. In other words, there should be no holes between ranks.
-- Return the result table ordered by score in descending order.

-- Oracle, Postgres
select score,
       dense_rank() over (order by score desc) rank
  from scores
 order by score desc
 ;

 -- MySQL
 -- keyword and reserved rank has to be quoted: single, double or back quote
select score,
       dense_rank() over (order by score desc) "rank"
  from scores
 order by score desc
 ;

 -- without analytic function
 select score,  
        (select count(distinct r.score) 
           from Scores r
          where r.score >= s.score
        ) "Rank"
   from Scores s
  order by 1 desc
  ;
