/*
drop table if exists Candidate;
drop table if exists Vote;
Create table If Not Exists Candidate (id int, name varchar(255));
Create table If Not Exists Vote (id int, candidateId int);
Truncate table Candidate;
insert into Candidate (id, name) values ('1', 'A');
insert into Candidate (id, name) values ('2', 'B');
insert into Candidate (id, name) values ('3', 'C');
insert into Candidate (id, name) values ('4', 'D');
insert into Candidate (id, name) values ('5', 'E');
Truncate table Vote;
insert into Vote (id, candidateId) values ('1', '2');
insert into Vote (id, candidateId) values ('2', '4');
insert into Vote (id, candidateId) values ('3', '3');
insert into Vote (id, candidateId) values ('4', '2');
insert into Vote (id, candidateId) values ('5', '5');
*/

-- Write an SQL query to report the name of the winning candidate
-- (i.e., the candidate who got the largest number of votes).
-- The test cases are generated so that exactly one candidate wins the elections.

-- Postgres, MySQL
select  name
  from (
        select  c.id,
                c.name,
                count(*) cnt
          from  candidate c
          join  vote v
            on  v.candidateId = c.id
        group by c.id,
                 c.name
        order by 3 desc
        limit 1
       ) v
 ;
 
-- Oracle
select  name
  from (
        select  c.id,
                c.name,
                count(*) cnt
          from  candidate c
          join  vote v
            on  v.candidateId = c.id
        group by c.id,
                 c.name
        order by 3 desc
       ) v
where  rownum = 1
;
