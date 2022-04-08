/*
Drop table If Exists Visits;
Drop table If Exists Transactions;
Create table If Not Exists Visits (user_id int, visit_date date);
Create table If Not Exists Transactions (user_id int, transaction_date date, amount int);
Truncate table Visits;
insert into Visits (user_id, visit_date) values ('1',  date'2020-01-01');
insert into Visits (user_id, visit_date) values ('2',  date'2020-01-02');
insert into Visits (user_id, visit_date) values ('12', date'2020-01-01');
insert into Visits (user_id, visit_date) values ('19', date'2020-01-03');
insert into Visits (user_id, visit_date) values ('1',  date'2020-01-02');
insert into Visits (user_id, visit_date) values ('2',  date'2020-01-03');
insert into Visits (user_id, visit_date) values ('1',  date'2020-01-04');
insert into Visits (user_id, visit_date) values ('7',  date'2020-01-11');
insert into Visits (user_id, visit_date) values ('9',  date'2020-01-25');
insert into Visits (user_id, visit_date) values ('8',  date'2020-01-28');
Truncate table Transactions;
insert into Transactions (user_id, transaction_date, amount) values ('1', date'2020-01-02', '120');
insert into Transactions (user_id, transaction_date, amount) values ('2', date'2020-01-03', '22');
insert into Transactions (user_id, transaction_date, amount) values ('7', date'2020-01-11', '232');
insert into Transactions (user_id, transaction_date, amount) values ('1', date'2020-01-04', '7');
insert into Transactions (user_id, transaction_date, amount) values ('9', date'2020-01-25', '33');
insert into Transactions (user_id, transaction_date, amount) values ('9', date'2020-01-25', '66');
insert into Transactions (user_id, transaction_date, amount) values ('8', date'2020-01-28', '1');
insert into Transactions (user_id, transaction_date, amount) values ('9', date'2020-01-25', '99');
*/
-- A bank wants to draw a chart of the number of transactions bank visitors
-- did in one visit to the bank and the corresponding number of visitors who
-- have done this number of transaction in one visit.

-- Write an SQL query to find how many users visited the bank and didn't do 
-- any transactions, how many visited the bank and did one transaction and so on.
-- The result table will contain two columns:
--  * transactions_count which is the number of transactions done in one visit.
--  * visits_count which is the corresponding number of users who did 
--    transactions_count in one visit to the bank.
-- transactions_count should take all values from 0 to max(transactions_count) 
-- done by one or more users.
-- Return the result table ordered by transactions_count.


-- The requirement was so badly written!!!
-- Postgres
with t1 as (
    select transactions_count,
           min(transactions_count) over() min_trx,
           max(transactions_count) over() max_trx,
           sum(visits) visits_count
      from (
            select coalesce(v.visit_date, transaction_date) op_date,
                   v.user_id,
                   count(distinct v.user_id) visits,
                   count(t.user_id) transactions_count
              from visits v
              full join Transactions t
                on v.user_id = t.user_id
               and visit_date = transaction_date
             group by v.user_id, coalesce(v.visit_date, transaction_date)
            ) a
      group by transactions_count
)
select t2.transactions_count,
       coalesce(t1.visits_count, 0) visits_count
  from (
        select generate_series(0, max_trx) transactions_count
          from (
                select max_trx
                  from t1
                 limit 1
               ) b
       ) t2
  left join t1
    on t2.transactions_count = t1.transactions_count
 order by t2.transactions_count
 ;

-- Oracle
with t1 as (
    select transactions_count,
           min(transactions_count) over() min_trx,
           max(transactions_count) over() max_trx,
           sum(visits) visits_count
      from (
            select coalesce(v.visit_date, transaction_date) op_date,
                   v.user_id,
                   count(distinct v.user_id) visits,
                   count(t.user_id) transactions_count
              from visits v
              full join Transactions t
                on v.user_id = t.user_id
               and visit_date = transaction_date
             group by v.user_id, coalesce(v.visit_date, transaction_date)
            ) a
      group by transactions_count
),
t2 as (
    select min_trx, 
           max_trx
      from t1
     where rownum = 1
),
t3 as (
    select level - 1 transactions_count
      from dual
   connect by level <= (select max_trx + 1 from t2)
)
select t3.transactions_count,
       coalesce(t1.visits_count, 0) visits_count
  from t3
  left join t1
    on t3.transactions_count = t1.transactions_count
 order by t3.transactions_count
 ;
