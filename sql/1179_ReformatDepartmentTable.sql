/*
Drop table If Not Exists Department;
Create table If Not Exists Department (id int, revenue int, month varchar(5));
Truncate table Department;
insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');
*/
-- Write an SQL query to reformat the table such that there is a 
-- department id column and a revenue column for each month.
-- Return the result table in any order.

/*
Drop table If Exists Department;
Create table If Not Exists Department (id int, revenue int, month varchar(5));
Truncate table Department;
insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');
*/
-- Write an SQL query to reformat the table such that there is a 
-- department id column and a revenue column for each month.
-- Return the result table in any order.

-- Postgres
select id,
       sum(revenue) filter (where month = 'Jan') Jan_Revenue, 
       sum(revenue) filter (where month = 'Feb') Feb_Revenue, 
       sum(revenue) filter (where month = 'Mar') Mar_Revenue, 
       sum(revenue) filter (where month = 'Apr') Apr_Revenue, 
       sum(revenue) filter (where month = 'May') May_Revenue, 
       sum(revenue) filter (where month = 'Jun') Jun_Revenue, 
       sum(revenue) filter (where month = 'Jul') Jul_Revenue, 
       sum(revenue) filter (where month = 'Aug') Aug_Revenue, 
       sum(revenue) filter (where month = 'Sep') Sep_Revenue, 
       sum(revenue) filter (where month = 'Oct') Oct_Revenue, 
       sum(revenue) filter (where month = 'Nov') Nov_Revenue, 
       sum(revenue) filter (where month = 'Dec') Dec_Revenue  
  from Department
 group by id;

-- Postgres, Oracle, MySQL
select id,
       sum(case when month = 'Jan' then revenue else null end) Jan_Revenue,
       sum(case when month = 'Feb' then revenue else null end) Feb_Revenue,
       sum(case when month = 'Mar' then revenue else null end) Mar_Revenue,
       sum(case when month = 'Apr' then revenue else null end) Apr_Revenue,
       sum(case when month = 'May' then revenue else null end) May_Revenue,
       sum(case when month = 'Jun' then revenue else null end) Jun_Revenue,
       sum(case when month = 'Jul' then revenue else null end) Jul_Revenue,
       sum(case when month = 'Aug' then revenue else null end) Aug_Revenue,
       sum(case when month = 'Sep' then revenue else null end) Sep_Revenue,
       sum(case when month = 'Oct' then revenue else null end) Oct_Revenue,
       sum(case when month = 'Nov' then revenue else null end) Nov_Revenue,
       sum(case when month = 'Dec' then revenue else null end) Dec_Revenue
  from Department
 group by id;
 
-- Oracle
select *
  from department 
       -- (select id, month, revenue from department) -- if there are extra redundant columns
 pivot (sum(revenue) as revenue for month in (  
            'Jan' as Jan,
            'Feb' as Feb,
            'Mar' as Mar,
            'Apr' as Apr,
            'May' as May,
            'Jun' as Jun,
            'Jul' as Jul,
            'Aug' as Aug,
            'Sep' as Sep,
            'Oct' as Oct,
            'Nov' as Nov,
            'Dec' as Dec
            )
       )
;
