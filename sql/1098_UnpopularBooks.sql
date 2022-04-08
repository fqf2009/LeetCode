/*
Drop table If Exists Books cascade;
Drop table If Exists Orders cascade;
Create table If Not Exists Books (book_id int, name varchar(50), available_from date);
Create table If Not Exists Orders (order_id int, book_id int, quantity int, dispatch_date date);
Truncate table Books;
insert into Books (book_id, name, available_from) values ('1', 'Kalila And Demna', '2010-01-01');
insert into Books (book_id, name, available_from) values ('2', '28 Letters', '2012-05-12');
insert into Books (book_id, name, available_from) values ('3', 'The Hobbit', '2019-06-10');
insert into Books (book_id, name, available_from) values ('4', '13 Reasons Why', '2019-06-01');
insert into Books (book_id, name, available_from) values ('5', 'The Hunger Games', '2008-09-21');
Truncate table Orders;
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('1', '1', '2', '2018-07-26');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('2', '1', '1', '2018-11-05');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('3', '3', '8', '2019-06-11');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('4', '4', '6', '2019-06-05');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('5', '4', '5', '2019-06-20');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('6', '5', '9', '2009-02-02');
insert into Orders (order_id, book_id, quantity, dispatch_date) values ('7', '5', '8', '2010-04-13');
*/
-- Write an SQL query that reports the books that have sold less than 10 copies in
-- the last year, excluding books that have been available for less than one month 
-- from today. Assume today is 2019-06-23.
-- Return the result table in any order.

-- Postgres
select b.book_id,
       b.name
  from (
        select book_id,
               name
          from books
         where available_from <= date'2019-06-23' + interval '-1 month'
       ) b
  left join 
       ( select book_id,
                quantity
           from orders o
          where -- extract(year from dispatch_date) = 2018
                dispatch_date between date'2019-06-23' + interval '-1 year'
                                  and date'2019-06-23'
        ) o
     on b.book_id = o.book_id
  group by b.book_id,
           b.name
 having coalesce(sum(quantity), 0) < 10
;

-- Oracle
select b.book_id,
       b.name
  from (
        select book_id,
               name
          from books
         where available_from <= add_months(date'2019-06-23', -1)
       ) b
  left join 
       ( select book_id,
                quantity
           from orders o
          where -- extract(year from dispatch_date) = 2018
                dispatch_date between add_months(date'2019-06-23', -12)
                                  and date'2019-06-23'
        ) o
     on b.book_id = o.book_id
  group by b.book_id,
           b.name
 having coalesce(sum(quantity), 0) < 10
;

-- MySQL
select b.book_id,
       b.name
  from (
        select book_id,
               name
          from books
         where available_from <= date_add(date'2019-06-23', interval '-1' month)
       ) b
  left join 
       ( select book_id,
                quantity
           from orders o
          where -- extract(year from dispatch_date) = 2018
                dispatch_date between date_add(date'2019-06-23', interval '-1' year)
                                  and date'2019-06-23'
        ) o
     on b.book_id = o.book_id
  group by b.book_id,
           b.name
 having coalesce(sum(quantity), 0) < 10
;
