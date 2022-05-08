## LeetCode SQL Problem Solutions

### Aggregate (Count(distinct column1, column2))
[0597_FriendRequestsI.sql](sql/0597_FriendRequestsI.sql)  

### Anti Join (not exists, not in, left join where is null)
[0183_CustomersWhoNeverOrder.sql](sql/0183_CustomersWhoNeverOrder.sql)  
[2020_NumberOfAccountsThatDidNotStream.sql](sql/2020_NumberOfAccountsThatDidNotStream.sql)  

### Bought A and B, but not C
[1398_CustomersBoughtProductsA_B_Not_C.sql](sql/1398_CustomersBoughtProductsA_B_Not_C.sql)  

### Contiguous (or Continuous) N records (group v.s. lag/lead)
[0601_HumanTrafficOfStadium.sql](sql/0601_HumanTrafficOfStadium.sql)  
[1454_ActiveUsers.sql](sql/1454_ActiveUsers.sql) **  

### Date functions (date_trunc)
[1511_CustomerOrderFrequency.sql](sql/1511_CustomerOrderFrequency.sql)  

### DML (Insert/Update/Delete)

### Left (right) outer join
[2142_NumberOfPassengersInEachBusI.sql](sql/2142_NumberOfPassengersInEachBusI.sql)  

### Midian
[0569_MedianEmployeeSalary.sql](sql/0569_MedianEmployeeSalary.sql)  

### Window function (analytic) on top of Aggregation
[0615_AverageSalaryDepartmentsVsCompany.sql](sql/0615_AverageSalaryDepartmentsVsCompany.sql)  
[1501_CountriesYouCanSafelyInvestIn.sql](sql/1501_CountriesYouCanSafelyInvestIn.sql)  

### Window function (lag, lead)
[0534_GamePlayAnalysisIII.sql](sql/0534_GamePlayAnalysisIII.sql)  
[0603_ConsecutiveAvailableSeats.sql](sql/0603_ConsecutiveAvailableSeats.sql)  
[1709_BiggestWindowBetweenVisits.sql](sql/1709_BiggestWindowBetweenVisits.sql)  
[2142_NumberOfPassengersInEachBusI.sql](sql/2142_NumberOfPassengersInEachBusI.sql)  

### Window function (running total, cumulative sum)
[1204_LastPersonToFitInTheBus.sql](sql/1204_LastPersonToFitInTheBus.sql)  

### Hierarchical Query, CTE (Common Table Expression or Recursive Subquery Factoring)
[1270_AllPeopleReportToGivenManager.sql](sql/1270_AllPeopleReportToGivenManager.sql)  

### Pivot and UnPivot
[1179_ReformatDepartmentTable.sql](sql/1179_ReformatDepartmentTable.sql)  

### Ratio
[1934_ConfirmationRate.sql](sql/1934_ConfirmationRate.sql)

### Scalar subquery (query in parentheses that returns exactly one row with one column)
[0626_ExchangeSeats.sql](sql/0626_ExchangeSeats.sql)  

### Self join (non-equal join)
[1917_LeetcodifyFriendsRecommendations.sql](sql/1917_LeetcodifyFriendsRecommendations.sql)  

### Set operation (intersect, union, union all, except (minus))
[1398_CustomersBoughtProductsA_B_Not_C.sql](sql/1398_CustomersBoughtProductsA_B_Not_C.sql)  
[2020_NumberOfAccountsThatDidNotStream.sql](sql/2020_NumberOfAccountsThatDidNotStream.sql)  

### Unnest v.s. union all
[1212_TeamScoresInFootballTournament.sql](sql/1212_TeamScoresInFootballTournament.sql)  
[1811_FindInterviewCandidates.sql](sql/1811_FindInterviewCandidates.sql)  

## what to check
```sql
not in

not exists

left/right/full join

unnest

lateral 

generate_series()

rank()

dense_rank()

row_number()

first_value, last_value, nth_value

lag, lead

greatest() / least()

order by [asc/desc] [nulls first/last]

limit offset

top n

consecutive n

group by

coalesce

-- By default, PostgreSQL assigns the names column1, column2, etc. 
values (1, 'one'), (2, 'two'), (3, 'three');
-- The same as
SELECT 1 AS column1, 'one' AS column2
UNION ALL
SELECT 2, 'two'
UNION ALL
SELECT 3, 'three';
-- This is better
SELECT * FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three')) AS t (num,letter);

SELECT f.*
  FROM films f
  join (VALUES('MGM', 'Horror'), ('UA', 'Sci-Fi')) AS t (studio, kind)
    on f.studio = t.studio AND f.kind = t.kind;

-- AS clause is required when VALUES is used in a FROM clause, just as is true for SELECT.
UPDATE employees SET salary = salary * v.increase
  FROM (VALUES(1, 200000, 1.2), (2, 400000, 1.4)) AS v (depno, target, increase)
  WHERE employees.depno = v.depno AND employees.sales >= v.target;


union, union all, intersect, except

-- Median
-- https://www.sisense.com/blog/medians-in-sql/
with ordered_purchases (
    select price,
           row_number() over (order by price) rn,
           count(*) as cnt
      from purchases
     where price is not null
)
select avg(price) as median
  from ordered_purchases
 where rn between cnt/2.0 and cnt/2.0 + 1

-- Median on Redshift
-- https://www.sisense.com/blog/medians-in-sql/
-- Note the limit 1: median is a window function and not an aggregate function
select median(price) over () as median
  from purchases
 limit 1
```
