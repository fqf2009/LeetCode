/*
Drop table If Exists TVProgram;
Drop table If Exists Content;
Create table If Not Exists TVProgram (program_date timestamp, content_id int, channel varchar(30));
Create table If Not Exists Content (content_id int, title varchar(30), Kids_content varchar(2), content_type varchar(30));
Truncate table TVProgram;
insert into TVProgram (program_date, content_id, channel) values ('2020-06-10 08:00', '1', 'LC-Channel');
insert into TVProgram (program_date, content_id, channel) values ('2020-05-11 12:00', '2', 'LC-Channel');
insert into TVProgram (program_date, content_id, channel) values ('2020-05-12 12:00', '3', 'LC-Channel');
insert into TVProgram (program_date, content_id, channel) values ('2020-05-13 14:00', '4', 'Disney Ch');
insert into TVProgram (program_date, content_id, channel) values ('2020-06-18 14:00', '4', 'Disney Ch');
insert into TVProgram (program_date, content_id, channel) values ('2020-07-15 16:00', '5', 'Disney Ch');
Truncate table Content;
insert into Content (content_id, title, Kids_content, content_type) values ('1', 'Leetcode Movie', 'N', 'Movies');
insert into Content (content_id, title, Kids_content, content_type) values ('2', 'Alg. for Kids', 'Y', 'Series');
insert into Content (content_id, title, Kids_content, content_type) values ('3', 'Database Sols', 'N', 'Series');
insert into Content (content_id, title, Kids_content, content_type) values ('4', 'Aladdin', 'Y', 'Movies');
insert into Content (content_id, title, Kids_content, content_type) values ('5', 'Cinderella', 'Y', 'Movies');
*/

-- Postgres
select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where p.program_date between timestamp'2020-06-01 00:00:00' and timestamp'2020-06-30 23:59:59'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;

select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where date_trunc('day', p.program_date) between '2020-06-01 00:00:00' and '2020-06-30 23:59:59'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;

select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where date_trunc('day', p.program_date) between date'2020-06-01' and date'2020-06-30'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;

select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where date_trunc('day', p.program_date) between '2020-06-01' and '2020-06-30'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;

-- Oracle
select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where trunc(p.program_date, 'dd') between date'2020-06-01' and date'2020-06-30'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;

-- MySQL (program_date is DATETIME type)
select distinct title
  from TVProgram p
  join content c
    on c.content_id = p.content_id
 where p.program_date between '2020-06-01 00:00:00' and '2020-06-30 23:59:59'
   and c.kids_content = 'Y'
   and c.content_type = 'Movies'
   ;
