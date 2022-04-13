/*
Drop table If Exists Product;
Drop table If Exists Sales;
Create table If Not Exists Product (product_id int, product_name varchar(30));
Create table If Not Exists Sales (product_id int, period_start date, period_end date, average_daily_sales int);
Truncate table Product;
insert into Product (product_id, product_name) values ('1', 'LC Phone ');
insert into Product (product_id, product_name) values ('2', 'LC T-Shirt');
insert into Product (product_id, product_name) values ('3', 'LC Keychain');
Truncate table Sales;
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('1', date'2019-01-25', date'2019-02-28', '100');
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('2', date'2018-12-01', date'2020-01-01', '10');
insert into Sales (product_id, period_start, period_end, average_daily_sales) values ('3', date'2019-12-01', date'2020-01-31', '1');
*/
-- Write an SQL query to report the total sales amount of each item for each 
-- year, with corresponding product_id, product_name, and report_year.
-- Return the result table ordered by product_id and report_year.


-- Postgres (Lateral)
 select s.product_id,
        p.product_name,
        s.report_year::text     report_year,
        average_daily_sales * (end_date - start_date + 1) total_amount
   from (
         select product_id,
                average_daily_sales,
                greatest(period_start, to_date(report_year::text || '0101', 'yyyymmdd')) start_date, 
                least(period_end, to_date(report_year::text || '1231', 'yyyymmdd')) end_date,
                report_year
           from Sales s,
        lateral (select generate_series(extract(year from s.period_start), 
                                        extract(year from s.period_end)) report_year
                ) y
        ) s
   join product p
     on p.product_id = s.product_id
  order by product_id, report_year
  ;


-- Even if not using lateral, Postgres' generate_series still can make each row to several rows!
select  s.product_id,
        p.product_name,
        s.report_year,
        average_daily_sales * (end_date - start_date + 1) total_amount
from    (
        select  product_id,
                average_daily_sales,
                report_year,
                greatest(period_start, to_date(report_year::text || '0101', 'yyyymmdd')) start_date, 
                least(period_end, to_date(report_year::text || '1231', 'yyyymmdd')) end_date
        from  (
                select  product_id,
                        average_daily_sales,
                        period_start,
                        period_end,
                        generate_series(extract(year from s.period_start)::integer, 
                                        extract(year from s.period_end)::integer) report_year
                from    Sales s
                ) s
        ) s
   join product p
    on  p.product_id = s.product_id
  order by product_id, report_year
  ;


-- Oracle can do similar things, but not easy to understand
    select product_id,
           to_date((start_year + level - 1) || '0101', 'yyyymmdd') start_date,
           to_date((start_year + level - 1) || '1231', 'yyyymmdd') end_date,
           to_char(start_year + level - 1)   report_year
      from ( select product_id,
                    extract(year from s.period_start) start_year, 
                    extract(year from s.period_end) end_year
               from Sales s
           )
   connect by product_id = prior product_id and 
              prior sys_guid() is not null and        -- here!
              start_year + level - 1 <= end_year;


-- Oracle 11g (Connect by)
with t as(
    select to_date((start_year + level - 1) || '0101', 'yyyymmdd') start_date,
           to_date((start_year + level - 1) || '1231', 'yyyymmdd') end_date,
           to_char(start_year + level - 1)   report_year
      from ( select extract(year from min(s.period_start)) start_year, 
                    extract(year from max(s.period_end)) end_year
               from Sales s
           )
   connect by start_year + level - 1 <= end_year
)
 select s.product_id,
        p.product_name,
        t.report_year,
        s.average_daily_sales * (least(period_end, t.end_date) - 
                                 greatest(period_start, t.start_date) + 1) total_amount
   from Sales s
   join t
     on (s.period_start between t.start_date and t.end_date) or
        (s.period_end between t.start_date and t.end_date) or
        (s.period_start < t.start_date and s.period_end > t.end_date)
   join product p
     on p.product_id = s.product_id
  order by product_id, report_year
  ;


-- Oracle 12c (cross join lateral)
 select s.product_id,
        p.product_name,
        s.report_year,
        average_daily_sales * (end_date - start_date + 1) total_amount
   from (
         select product_id,
                average_daily_sales,
                greatest(period_start, to_date(report_year || '0101', 'yyyymmdd')) start_date, 
                least(period_end, to_date(report_year || '1231', 'yyyymmdd')) end_date,
                report_year
           from Sales s
           cross join lateral (
                    select extract(year from s.period_start) + level - 1 report_year
                      from dual
                   connect by extract(year from s.period_start) + level - 1 <=
                              extract(year from s.period_end)
                ) y
        ) s
   join product p
     on p.product_id = s.product_id
  order by product_id, report_year
  ;


-- Oracle 12c (cross apply), SQL Server syntax
 select s.product_id,
        p.product_name,
        s.report_year,
        average_daily_sales * (end_date - start_date + 1) total_amount
   from (
         select product_id,
                average_daily_sales,
                greatest(period_start, to_date(report_year || '0101', 'yyyymmdd')) start_date, 
                least(period_end, to_date(report_year || '1231', 'yyyymmdd')) end_date,
                report_year
           from Sales s
          cross apply (select start_year + level - 1 report_year
                           from ( select extract(year from s.period_start) start_year, 
                                         extract(year from s.period_end) end_year
                                    from dual
                                )
                         connect by start_year + level - 1 <= end_year
                      ) y
        ) s
   join product p
     on p.product_id = s.product_id
  order by product_id, report_year
  ;


-- MySQL (CTE)
with recursive t(start_year, end_year) as (
    select extract(year from min(s.period_start)) start_year, 
           extract(year from max(s.period_end)) end_year
      from Sales s
     union all
    select start_year + 1 start_year,
           end_year
      from t
     where start_year + 1 <= end_year
)
 select s.product_id,
        p.product_name,
        t.report_year,
        s.average_daily_sales * 
            (datediff(least(period_end, t.end_date),
                      greatest(period_start, t.start_date)) + 1) total_amount
   from Sales s
   join (select date(concat(start_year, '-01-01')) start_date,
                date(concat(start_year, '-12-31')) end_date,
                cast(start_year as char) report_year
           from t
        ) t
     on (s.period_start between t.start_date and t.end_date) or
        (s.period_end between t.start_date and t.end_date) or
        (s.period_start < t.start_date and s.period_end > t.end_date)
   join product p
     on p.product_id = s.product_id
  order by product_id, report_year
;
