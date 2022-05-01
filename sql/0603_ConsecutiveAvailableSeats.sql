/*
drop table if exists cinema;
Create table If Not Exists Cinema (seat_id serial primary key, free bool);
Truncate table Cinema;
insert into Cinema (seat_id, free) values ('1', '1');
insert into Cinema (seat_id, free) values ('2', '0');
insert into Cinema (seat_id, free) values ('3', '1');
insert into Cinema (seat_id, free) values ('4', '1');
insert into Cinema (seat_id, free) values ('5', '1');
*/
-- Each row of this table indicates whether the ith seat is free 
-- or not. 1 means free while 0 means occupied.
-- Write an SQL query to report all the consecutive available seats in the cinema.
-- Return the result table ordered by seat_id in ascending order.

-- Postgres, MySQL
select seat_id
  from (
        select seat_id,
               case when free = true and
                    ( lag(free)  over (order by seat_id) = true or
                      lead(free) over (order by seat_id) = true ) then true
                    else false
                end consecutive
        from cinema
       ) c
 where consecutive
 order by seat_id
 ;

-- Postgres, MySQL both support bool type
 select seat_id
  from (
        select seat_id,
               case when free and
                    ( lag(free)  over (order by seat_id) or
                      lead(free) over (order by seat_id) ) then true
                    else false
                end consecutive
        from cinema
       ) c
 where consecutive
 order by seat_id
 ;
 
 -- Oracle
 select seat_id
  from (
        select seat_id,
               case when free = 1 and
                    ( lag(free)  over (order by seat_id) = 1 or
                      lead(free) over (order by seat_id) = 1 ) then 1
                    else 0
                end consecutive
        from cinema
       ) c
 where consecutive = 1
 order by seat_id
 ;
 

 -- Practise again
 select seat_id
  from (
        select seat_id,
               free,
               case when lag(free) over (order by seat_id) = 1 or
                         lead(free) over (order by seat_id) = 1 then 'Y'
                    else 'N'
                end consecutive
          from Cinema
       ) c
 where consecutive = 'Y' and
       free = 1   -- not as good as before
 order by 1;
