/*
Drop table If Exists Events;
Create table If Not Exists Events (business_id int, event_type varchar(10), occurences int);
Truncate table Events;
insert into Events (business_id, event_type, occurences) values ('1', 'reviews', '7');
insert into Events (business_id, event_type, occurences) values ('3', 'reviews', '3');
insert into Events (business_id, event_type, occurences) values ('1', 'ads', '11');
insert into Events (business_id, event_type, occurences) values ('2', 'ads', '7');
insert into Events (business_id, event_type, occurences) values ('3', 'ads', '6');
insert into Events (business_id, event_type, occurences) values ('1', 'page views', '3');
insert into Events (business_id, event_type, occurences) values ('2', 'page views', '12');
*/
-- The average activity for a particular event_type is the average occurences 
-- across all companies that have this event.
-- An active business is a business that has more than one event_type such that 
-- their occurences is strictly greater than the average activity for that event.
-- Write an SQL query to find all active businesses.
-- Return the result table in any order.


-- Postgres, Oracle, MySQL, SQLServer
select business_id
  from (
        select business_id,
               occurences,
               avg(occurences) over (partition by event_type) avg_occurences
          from Events
       ) e
 where occurences > avg_occurences
 group by business_id
having count(*) > 1
;
