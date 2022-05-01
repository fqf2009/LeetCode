/*
Drop table If Exists Listens;
Drop table If Exists Friendship;
Create table If Not Exists Listens (user_id int, song_id int, day date);
-- Note there may be duplicates in Listens table

Create table If Not Exists Friendship (user1_id int, user2_id int);
-- (user1_id, user2_id) is the primary key for this table.
-- Note that user1_id < user2_id.

-- Test case 1
Truncate table Listens;
insert into Listens (user_id, song_id, day) values ('1', '10', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('1', '11', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('1', '12', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('2', '10', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('2', '11', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('2', '12', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('3', '10', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('3', '11', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('3', '12', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('4', '10', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('4', '11', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('4', '13', '2021-03-15');
insert into Listens (user_id, song_id, day) values ('5', '10', '2021-03-16');
insert into Listens (user_id, song_id, day) values ('5', '11', '2021-03-16');
insert into Listens (user_id, song_id, day) values ('5', '12', '2021-03-16');
Truncate table Friendship;
insert into Friendship (user1_id, user2_id) values ('1', '2');
-- Test case 2
Truncate table Listens;
insert into Listens (user_id, song_id, day) values (1,33, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,44, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,66, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,77, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,33, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (1,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,44, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,66, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,77, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,88, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (2,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,55, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (2,99, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (2,22, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (2,88, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (3,33, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (3,44, date'2021-03-17');
insert into Listens (user_id, song_id, day) values (3,88, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (3,44, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (3,99, date'2021-03-14');
insert into Listens (user_id, song_id, day) values (3,22, date'2021-03-14');
Truncate table Friendship;
insert into Friendship (user1_id, user2_id) values ('2', '3');
*/


-- Write an SQL query to recommend friends to Leetcodify users. 
-- We recommend user x to user y if:
--      Users x and y are not friends, and
--      Users x and y listened to the same three or more different songs on the same day.
-- Note that friend recommendations are unidirectional, meaning if user x and user y 
-- should be recommended to each other, the result table should have both user x 
-- recommended to user y and user y recommended to user x. Also, note that the 
-- result table should not contain duplicates (i.e., user y should not be recommended 
-- to user x multiple times.).
-- Return the result table in any order.

-- Postgres, Oracle, MySQL
select distinct user1 user_id,
       user2 recommended_id
  from (
        select l1.user_id user1,
               l2.user_id user2,
               l1.day
          from Listens l1
          join Listens l2
            on l1.user_id <> l2.user_id
           and l1.day = l2.day
           and l1.song_id = l2.song_id
         group by l1.user_id,
                  l2.user_id,
                  l1.day
        having count(distinct l1.song_id) >= 3  -- !!! distinct
       ) l
 where not exists (
     select null
       from Friendship f
      where (f.user1_id = l.user1 and f.user2_id = l.user2)
         or (f.user1_id = l.user2 and f.user2_id = l.user1)
 )
 ;


-- Left join seems have better performance
select user_id,
       recommended_id
  from (
        select distinct user1 user_id,
               user2 recommended_id
          from (
                select l1.user_id user1,
                       l2.user_id user2,
                       l1.day
                  from listens l1
                  join listens l2
                    on l1.user_id <> l2.user_id
                   and l1.day = l2.day
                   and l1.song_id = l2.song_id
                 group by l1.user_id,
                          l2.user_id,
                          l1.day
                having count(distinct l1.song_id) >= 3
               ) l
       ) l
  left join Friendship f
    on (f.user1_id = l.user_id and f.user2_id = l.recommended_id) or
       (f.user1_id = l.recommended_id and f.user2_id = l.user_id)
 where f.user1_id is null
;


-- based on the precondition in Friendship table: user1_id < user2_id
-- seems even faster, guess there are too much duplicates in listen table
with t as (
    select user_id,  
           recommended_id
      from (
            select distinct user1 user_id,
                   user2 recommended_id
              from (
                    select l1.user_id user1,
                           l2.user_id user2,
                           l1.day
                      from listens l1
                      join listens l2
                        on l1.user_id < l2.user_id  -- difference is here
                       and l1.day = l2.day
                       and l1.song_id = l2.song_id
                     group by l1.user_id,
                              l2.user_id,
                              l1.day
                    having count(distinct l1.song_id) >= 3
                  ) l
          ) l
      left join Friendship f
        on f.user1_id = l.user_id and f.user2_id = l.recommended_id
    where f.user1_id is null
)
select user_id,
       recommended_id
  from t
 union all
select recommended_id,
       user_id
  from t
;
