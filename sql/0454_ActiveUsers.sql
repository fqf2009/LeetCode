/*
Drop table If Exists Accounts;
Drop table If Exists Logins;
Create table If Not Exists Accounts (id int, name varchar(10));
Create table If Not Exists Logins (id int, login_date date);
Truncate table Accounts;
insert into Accounts (id, name) values ('1', 'Winston');
insert into Accounts (id, name) values ('7', 'Jonathan');
Truncate table Logins;
insert into Logins (id, login_date) values ('7', '2020-05-30');
insert into Logins (id, login_date) values ('1', '2020-05-30');
insert into Logins (id, login_date) values ('7', '2020-05-31');
insert into Logins (id, login_date) values ('7', '2020-06-01');
insert into Logins (id, login_date) values ('7', '2020-06-02');
insert into Logins (id, login_date) values ('7', '2020-06-02');
insert into Logins (id, login_date) values ('7', '2020-06-03');
insert into Logins (id, login_date) values ('1', '2020-06-07');
insert into Logins (id, login_date) values ('7', '2020-06-10');
*/
-- Active users are those who logged in to their accounts for 
-- five or more consecutive days.
-- Write an SQL query to find the id and the name of active users.
-- Return the result table ordered by id.

-- Follow up: Could you write a general solution if the active users are
-- those who logged in to their accounts for n or more consecutive days?

-- Postgres, Oracle
select distinct a.id, a.name
  from accounts a
  join (
        select id,
               login_date,
               cont_start,
               cont_end,
               lead(login_date) over (partition by id order by login_date)  end_date
          from (
                select id,
                       login_date,
                       case when lag(login_date) over (
                                    partition by id order by login_date) = login_date - 1
                                then 'N'
                            else 'Y' 
                        end cont_start,
                       case when lead(login_date) over (
                                    partition by id order by login_date) = login_date + 1
                                then 'N'
                            else 'Y'
                        end cont_end
                  from (select distinct id, login_date
                          from logins
                       ) l
               ) l
         where cont_start <> cont_end
       ) l
    on l.id = a.id
 where l.cont_start = 'Y' and
       l.end_date - l.login_date + 1 >= 5
 order by a.id
;

-- MySQL
select distinct a.id, a.name
  from accounts a
  join (
        select id,
               login_date,
               cont_start,
               cont_end,
               lead(login_date) over (partition by id order by login_date)  end_date
          from (
                select id,
                       login_date,
                       case when lag(login_date) over (
                                    partition by id order by login_date) = date_add(login_date, interval '-1' day)
                                then 'N'
                            else 'Y' 
                        end cont_start,
                       case when lead(login_date) over (
                                    partition by id order by login_date) = date_add(login_date, interval '1' day)
                                then 'N'
                            else 'Y'
                        end cont_end
                  from (select distinct id, login_date
                          from logins
                       ) l
               ) l
         where cont_start <> cont_end
       ) l
    on l.id = a.id
 where l.cont_start = 'Y' and
       l.end_date >= date_add(l.login_date, interval '4' day)
 order by a.id
;
