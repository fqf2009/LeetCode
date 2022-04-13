/*
Drop table If Exists Person;
Drop table If Exists Country cascade;
Drop table If Exists Calls;
Create table If Not Exists Person (id int, name varchar(15), phone_number varchar(11));
Create table If Not Exists Country (name varchar(15), country_code varchar(3));
Create table If Not Exists Calls (caller_id int, callee_id int, duration int);
Truncate table Person;
insert into Person (id, name, phone_number) values ('3', 'Jonathan', '051-1234567');
insert into Person (id, name, phone_number) values ('12', 'Elvis', '051-7654321');
insert into Person (id, name, phone_number) values ('1', 'Moncef', '212-1234567');
insert into Person (id, name, phone_number) values ('2', 'Maroua', '212-6523651');
insert into Person (id, name, phone_number) values ('7', 'Meir', '972-1234567');
insert into Person (id, name, phone_number) values ('9', 'Rachel', '972-0011100');
Truncate table Country;
insert into Country (name, country_code) values ('Peru', '051');
insert into Country (name, country_code) values ('Israel', '972');
insert into Country (name, country_code) values ('Morocco', '212');
insert into Country (name, country_code) values ('Germany', '049');
insert into Country (name, country_code) values ('Ethiopia', '251');
Truncate table Calls;
insert into Calls (caller_id, callee_id, duration) values ('1', '9', '33');
insert into Calls (caller_id, callee_id, duration) values ('2', '9', '4');
insert into Calls (caller_id, callee_id, duration) values ('1', '2', '59');
insert into Calls (caller_id, callee_id, duration) values ('3', '12', '102');
insert into Calls (caller_id, callee_id, duration) values ('3', '12', '330');
insert into Calls (caller_id, callee_id, duration) values ('12', '3', '5');
insert into Calls (caller_id, callee_id, duration) values ('7', '9', '13');
insert into Calls (caller_id, callee_id, duration) values ('7', '1', '3');
insert into Calls (caller_id, callee_id, duration) values ('9', '7', '1');
insert into Calls (caller_id, callee_id, duration) values ('1', '7', '7');
*/
-- A telecommunications company wants to invest in new countries. The company 
-- intends to invest in the countries where the average call duration of the 
-- calls in this country is strictly greater than the global average call duration.
-- Write an SQL query to find the countries where this company can invest.
-- Return the result table in any order.


-- Postgres
select name country
  from country c
  join (
        select substr(phone_number, 1, 3)   country_code,
               avg(duration)                country_avg_duration,
               sum(sum(duration)) over() / sum(count(*)) over ()    global_avg_duration
          from (
                select unnest(array[caller_id, callee_id]) person_id, -- cannot be used in join yet
                       duration
                  from calls
               ) c
          join person p
            on p.id = c.person_id
         group by country_code
       ) p
    on p.country_code = c.country_code
 where p.country_avg_duration > global_avg_duration
;


-- Postgres, MySQL
select name country
  from country c
  join (
        select substr(phone_number, 1, 3)   country_code,
               avg(duration)                country_avg_duration,
               sum(sum(duration)) over() / sum(count(*)) over ()    global_avg_duration
          from (
                select caller_id person_id,
                       duration
                  from calls
                 union all
                select callee_id person_id,
                       duration
                  from calls
               ) c
          join person p
            on p.id = c.person_id
         group by country_code
       ) c1
    on c1.country_code = c.country_code
 where c1.country_avg_duration > global_avg_duration
;

-- Oracle
select name country
  from country c
  join (
        select substr(phone_number, 1, 3)   country_code,
               avg(duration)                country_avg_duration,
               sum(sum(duration)) over() / sum(count(*)) over ()    global_avg_duration
          from (
                select caller_id person_id,
                       duration
                  from calls
                 union all
                select callee_id person_id,
                       duration
                  from calls
               ) c
          join person p
            on p.id = c.person_id
         group by substr(phone_number, 1, 3)    -- difference is here
       ) c1
    on c1.country_code = c.country_code
 where c1.country_avg_duration > global_avg_duration
  ;
