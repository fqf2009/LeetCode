/*
Drop table If Exists Seat;
Create table If Not Exists Seat (id int, student varchar(255));
Truncate table Seat;
insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');
-- insert into Seat (id, student) values ('6', 'Bill');
*/
-- Write an SQL query to swap the seat id of every two 
-- consecutive students. If the number of students is odd, 
-- the id of the last student is not swapped.
-- Return the result table ordered by id in ascending order.


-- Postgres, Oracle, MySQL
select id,
       case when mod(id, 2) = 1 then
                case when id = (select max(id) id from seat) then student
                     else lead(student) over(order by id)
                end
            else lag(student) over(order by id)
       end student
  from seat
 order by id
;

-- Postgres, Oracle, MySQL
select id + 1 id, student
  from seat
 where mod(id, 2) = 1
   and id not in (select id 
                    from (select max(id) id from seat) s
                   where mod(id, 2) = 1
                 )
 union all
select id - 1 id, student
  from seat
 where mod(id, 2) = 0
 union all
select id, student
  from seat
 where id = (select max(id) id from seat)
   and mod(id, 2) = 1
 order by id
;
