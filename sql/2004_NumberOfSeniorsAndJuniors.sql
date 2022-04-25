/*
Drop table If Exists Candidates;
Create table If Not Exists Candidates (employee_id int, experience varchar(20), salary int);
Truncate table Candidates;
insert into Candidates (employee_id, experience, salary) values ('1', 'Junior', '10000');
insert into Candidates (employee_id, experience, salary) values ('9', 'Junior', '10000');
insert into Candidates (employee_id, experience, salary) values ('2', 'Senior', '20000');
insert into Candidates (employee_id, experience, salary) values ('11', 'Senior', '20000');
insert into Candidates (employee_id, experience, salary) values ('13', 'Senior', '50000');
insert into Candidates (employee_id, experience, salary) values ('4', 'Junior', '40000');
-- test case 2
Truncate table Candidates;
insert into Candidates (employee_id, experience, salary) values ('1', 'Junior', '10000');
insert into Candidates (employee_id, experience, salary) values ('9', 'Junior', '10000');
insert into Candidates (employee_id, experience, salary) values ('2', 'Senior', '80000');
insert into Candidates (employee_id, experience, salary) values ('11', 'Senior', '80000');
insert into Candidates (employee_id, experience, salary) values ('13', 'Senior', '80000');
insert into Candidates (employee_id, experience, salary) values ('4', 'Junior', '40000');
*/
-- A company wants to hire new employees. The budget of the company for the 
-- salaries is $70000. The company's criteria for hiring are:
--  - Hiring the largest number of seniors.
--  - After hiring the maximum number of seniors, use the remaining budget to 
--    hire the largest number of juniors.
-- Write an SQL query to find the number of seniors and juniors hired under the mentioned criteria.
-- Return the result table in any order.

-- postgres, oracle, mysql
with t as(
    select count(*) accepted_candidates,
           max(csum_salary) senior_salary
      from (
            select sum(salary) over(order by salary 
                rows between unbounded preceding and current row) csum_salary
              from Candidates
             where experience = 'Senior'
           ) c
     where csum_salary <= 70000
 )
 select 'Senior' experience,
        accepted_candidates
   from t
  union all
 select 'Junior' experience,
        count(*) accepted_candidates
  from (
        select sum(salary) over(order by salary 
            rows between unbounded preceding and current row) csum_salary
          from Candidates
         where experience = 'Junior'
       ) c
 where csum_salary <= (select 70000 - coalesce(senior_salary, 0) from t)
 ;


-- practice again
-- Postgres
with t as(
    select count(*) senior_cnt,
           70000 - coalesce(max(csum_salary), 0) junior_budget
      from (
            select sum(salary) over(order by salary) csum_salary
              from Candidates
             where experience = 'Senior'
           ) s
     where s.csum_salary <= 70000
)
select 'Junior' experience,
       count(*) accepted_candidates
  from (
        select sum(salary) over(order by salary) csum_salary
          from Candidates c
         where experience = 'Junior'
       ) s
 where s.csum_salary < (select junior_budget from t)
 union all
select 'Senior', senior_cnt
  from t
 ;
