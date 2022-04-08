/*
drop table if exists stadium;
Create table If Not Exists Stadium (id int, visit_date DATE NULL, people int);
Truncate table Stadium;
insert into Stadium (id, visit_date, people) values ('1', '2017-01-01', '10');
insert into Stadium (id, visit_date, people) values ('2', '2017-01-02', '109');
insert into Stadium (id, visit_date, people) values ('3', '2017-01-03', '150');
insert into Stadium (id, visit_date, people) values ('4', '2017-01-04', '99');
insert into Stadium (id, visit_date, people) values ('5', '2017-01-05', '145');
insert into Stadium (id, visit_date, people) values ('6', '2017-01-06', '1455');
insert into Stadium (id, visit_date, people) values ('7', '2017-01-07', '199');
insert into Stadium (id, visit_date, people) values ('8', '2017-01-09', '188');
*/

-- Write an SQL query to display the records with three or more rows with consecutive
-- id's, and the number of people is greater than or equal to 100 for each.
-- Return the result table ordered by visit_date in ascending order.

-- Postgres, MySQL
select id, 
       visit_date, 
       people
  from (
        select id, 
               visit_date, 
               people, 
               lag(people, 1) over (order by id) prev1,
               lag(people, 2) over (order by id) prev2,
               lead(people, 1) over (order by id) next1,
               lead(people, 2) over (order by id) next2
          from stadium
       ) s
 where people >= 100
   and ((prev1 >= 100 and prev2 >= 100) or
        (prev1 >= 100 and next1 >= 100) or
        (next1 >= 100 and next2 >= 100))
 order by visit_date
 ;

-- Oracle
select id, 
       to_char(visit_date, 'yyyy-mm-dd') visit_date, 
       people
  from (
        select id, 
               visit_date, 
               people, 
               lag(people, 1) over (order by id) prev1,
               lag(people, 2) over (order by id) prev2,
               lead(people, 1) over (order by id) next1,
               lead(people, 2) over (order by id) next2
          from stadium
       ) s
 where people >= 100
   and ((prev1 >= 100 and prev2 >= 100) or
        (prev1 >= 100 and next1 >= 100) or
        (next1 >= 100 and next2 >= 100))
 order by visit_date
 ;

 -- How about n or more rows?
 -- Note this is not perfect if there is gap in id!!!
select id,
       visit_date,
       people
  from stadium s
  join (
        select start_id, 
               end_id
          from (
                select id start_id, 
                       start100,
                       lead(id, 1) over (order by id) end_id
                  from (
                        select id, 
                               case when people >= 100 and 
                                         coalesce(lag(people, 1) over (order by id), 0) < 100 then 1
                                    else 0
                                end start100,
                               case when people >= 100 and 
                                         coalesce(lead(people, 1) over (order by id), 0) < 100 then 1
                                    else 0
                                end stop100
                          from stadium
                       ) c
                 where (start100 + stop100) = 1
               ) c
         where start100 = 1 and (end_id - start_id + 1 >= 3)  -- parameter n = 3, note n > 1 !!!
       ) c
    on s.id between c.start_id and c.end_id
 order by s.visit_date
 ;

-- Works even if there is gap in id
select id,
       visit_date,
       people
  from (
        select id,
               visit_date,
               people,
               count(*) over (partition by rn) cnt -- how many rows in this range
          from stadium s
          join (
                select start_id, 
                       end_id, 
                       row_number() over () rn  -- differenciate each range
                  from (
                        select id start_id, 
                               start100,
                               lead(id, 1) over (order by id) end_id
                          from (
                                select id,
                                       case when people >= 100 and 
                                                 coalesce(lag(people, 1) over
                                                      (order by id), 0) < 100 then 1
                                            else 0
                                        end start100,
                                       case when people >= 100 and 
                                                 coalesce(lead(people, 1) over
                                                      (order by id), 0) < 100 then 1
                                            else 0
                                        end stop100
                                  from stadium
                               ) c
                         where (start100 + stop100) = 1
                       ) c
                 where start100 = 1
               ) c
            on s.id between c.start_id and c.end_id
       ) s
 where cnt >= 3   -- parameter for n consecutive
 order by s.visit_date
 ;