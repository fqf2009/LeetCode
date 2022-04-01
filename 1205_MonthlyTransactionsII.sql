/*
Drop table If Exists Transactions;
Drop table If Exists Chargebacks;
Create table If Not Exists Transactions (id int, country varchar(4), state varchar(20), amount int, trans_date date);
Create table If Not Exists Chargebacks (trans_id int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('101', 'US', 'approved', '1000', date'2019-05-18');
insert into Transactions (id, country, state, amount, trans_date) values ('102', 'US', 'declined', '2000', date'2019-05-19');
insert into Transactions (id, country, state, amount, trans_date) values ('103', 'US', 'approved', '3000', date'2019-06-10');
insert into Transactions (id, country, state, amount, trans_date) values ('104', 'US', 'declined', '4000', date'2019-06-13');
insert into Transactions (id, country, state, amount, trans_date) values ('105', 'US', 'approved', '5000', date'2019-06-15');
Truncate table Chargebacks;
insert into Chargebacks (trans_id, trans_date) values ('102', date'2019-05-29');
insert into Chargebacks (trans_id, trans_date) values ('101', date'2019-06-30');
insert into Chargebacks (trans_id, trans_date) values ('105', date'2019-09-18');
*/
-- Write an SQL query to find for each month and country: the number of approved 
-- transactions and their total amount, the number of chargebacks, and their 
-- total amount.
-- Note: In your query, given the month and country, ignore rows with all zeros.
-- Return the result table in any order.

-- Postgres
select coalesce(t.yearmonth, c.yearmonth) "month", -- double quote is required
       coalesce(t.country, c.country) country,
       coalesce(t.approved_count, 0) approved_count,
       coalesce(t.approved_amount, 0) approved_amount,
       coalesce(c.chargeback_count, 0) chargeback_count,
       coalesce(c.chargeback_amount, 0) chargeback_amount
  from (
        select to_char(trans_date, 'yyyy-mm') yearmonth,
               country,
               sum(case when state = 'approved' then 1 else 0 end) approved_count,
               sum(case when state = 'approved' then amount else 0 end) approved_amount
          from Transactions t
         group by to_char(trans_date, 'yyyy-mm'),
                  country
       ) t
  full join (
        select to_char(c.trans_date, 'yyyy-mm') yearmonth,
               t.country,
               count(*) chargeback_count,
               sum(amount) chargeback_amount
          from Transactions t
          join Chargebacks c
            on c.trans_id = t.id
         group by to_char(c.trans_date, 'yyyy-mm'),
                  t.country
       ) c
    on t.yearmonth = c.yearmonth
   and t.country = c.country
 where coalesce(t.approved_amount, 0) + coalesce(c.chargeback_amount, 0) > 0
 ;

-- Oracle
select coalesce(t.yearmonth, c.yearmonth) month,
       coalesce(t.country, c.country) country,
       coalesce(t.approved_count, 0) approved_count,
       coalesce(t.approved_amount, 0) approved_amount,
       coalesce(c.chargeback_count, 0) chargeback_count,
       coalesce(c.chargeback_amount, 0) chargeback_amount
  from (
        select to_char(trans_date, 'yyyy-mm') yearmonth,
               country,
               sum(case when state = 'approved' then 1 else 0 end) approved_count,
               sum(case when state = 'approved' then amount else 0 end) approved_amount
          from Transactions t
         group by to_char(trans_date, 'yyyy-mm'),
                  country
       ) t
  full join (
        select to_char(c.trans_date, 'yyyy-mm') yearmonth,
               t.country,
               count(*) chargeback_count,
               sum(amount) chargeback_amount
          from Transactions t
          join Chargebacks c
            on c.trans_id = t.id
         group by to_char(c.trans_date, 'yyyy-mm'),
                  t.country
       ) c
    on t.yearmonth = c.yearmonth
   and t.country = c.country
 where coalesce(t.approved_amount, 0) + coalesce(c.chargeback_amount, 0) > 0
 ;

-- filter out unwanted rows earlier
select coalesce(t.yearmonth, c.yearmonth) month,
       coalesce(t.country, c.country) country,
       coalesce(t.approved_count, 0) approved_count,
       coalesce(t.approved_amount, 0) approved_amount,
       coalesce(c.chargeback_count, 0) chargeback_count,
       coalesce(c.chargeback_amount, 0) chargeback_amount
  from (
        select to_char(trans_date, 'yyyy-mm') yearmonth,
               country,
               sum(case when state = 'approved' then 1 else 0 end) approved_count,
               sum(case when state = 'approved' then amount else 0 end) approved_amount
          from Transactions t
         group by to_char(trans_date, 'yyyy-mm'),
                  country
        having sum(case when state = 'approved' then amount else 0 end) > 0 -- here
       ) t
  full join (
        select to_char(c.trans_date, 'yyyy-mm') yearmonth,
               t.country,
               count(*) chargeback_count,
               sum(amount) chargeback_amount
          from Transactions t
          join Chargebacks c
            on c.trans_id = t.id
         group by to_char(c.trans_date, 'yyyy-mm'),
                  t.country
        having sum(amount) > 0  -- here
       ) c
    on t.yearmonth = c.yearmonth
   and t.country = c.country
 ;

-- MySQL does not support full outer join
with t as (
    select date_format(trans_date, '%Y-%m') yearmonth,
           country,
           sum(case when state = 'approved' then 1 else 0 end) approved_count,
           sum(case when state = 'approved' then amount else 0 end) approved_amount
      from Transactions t
     group by date_format(trans_date, '%Y-%m'),
              country
    having sum(case when state = 'approved' then amount else 0 end) > 0
),
c as (
    select date_format(c.trans_date, '%Y-%m') yearmonth,
           t.country,
           count(*) chargeback_count,
           sum(amount) chargeback_amount
      from Transactions t
      join Chargebacks c
        on c.trans_id = t.id
     group by date_format(c.trans_date, '%Y-%m'),
              t.country
    having sum(amount) > 0
)
select t.yearmonth month,
       t.country country,
       t.approved_count approved_count,
       t.approved_amount approved_amount,
       coalesce(c.chargeback_count, 0) chargeback_count,
       coalesce(c.chargeback_amount, 0) chargeback_amount
  from t
  left join c
    on t.yearmonth = c.yearmonth
   and t.country = c.country
 union 
select c.yearmonth month,
       c.country country,
       coalesce(t.approved_count, 0) approved_count,
       coalesce(t.approved_amount, 0) approved_amount,
       c.chargeback_count chargeback_count,
       c.chargeback_amount chargeback_amount
  from t
 right join c
    on t.yearmonth = c.yearmonth
   and t.country = c.country
 ;
 