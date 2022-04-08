-- Write an SQL query to report the nth highest salary from the Employee 
-- table. If there is no nth highest salary, the query should report null.

/*
drop table if exists Employee;
Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');
*/

-- Postgres 
--      nulls last is default for ascending
--      argmode 'in' precedes to the argument name
--      language plpgsql
--      returns numeric (not return)
--      as function_body (not is)
--      double dollar quoting, the last semicolon after $$
--      declare cannot be omitted
create or replace function getnthhighestsalary(in n numeric)
    returns numeric
    language plpgsql
as $$
declare
    result numeric;
begin
    select salary
      into result
      from (
            select salary,
                   dense_rank() over (order by salary desc) rk
              from employee e
           ) s
     where rk = n
     union all
    select null
     order by 1 nulls last
     limit 1
    ;

    return result;
end $$;

-- test
select nth, 
       getnthhighestsalary(nth) nthhighestsalary
  from generate_series(1, 4) nth;


-- Oracle (nulls last is default for ascending)
create or replace function getnthhighestsalary(n in number) return number is
    result number;
begin
    select secondhighestsalary
      into result
      from (
            select salary
              from (
                    select salary,
                          dense_rank() over (order by salary desc) rk
                      from employee e
                  ) s
             where rk = n
             union all
            select null
              from dual
             order by 1 nulls last
         )
     where rownum = 1;
    
    return result;
end;
/

-- test
select level nth,
       getnthhighestsalary(level)
  from dual
connect by level <= 4;


-- MySQL (NULL values are considered lower in order, than any non-NULL value)
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        select salary
          from (
                select salary,
                       dense_rank() over (order by salary desc) rk
                  from Employee e
               ) s
         where rk = n
         union all
        select null
         order by 1 desc
         limit 1
  );
end
