/*
Drop table If Exists Users;
Drop table If Exists Orders;
Drop table If Exists Items;
Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10))
Create table If Not Exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int)
Create table If Not Exists Items (item_id int, item_brand varchar(10))
Truncate table Users
insert into Users (user_id, join_date, favorite_brand) values ('1', '2018-01-01', 'Lenovo')
insert into Users (user_id, join_date, favorite_brand) values ('2', '2018-02-09', 'Samsung')
insert into Users (user_id, join_date, favorite_brand) values ('3', '2018-01-19', 'LG')
insert into Users (user_id, join_date, favorite_brand) values ('4', '2018-05-21', 'HP')
Truncate table Orders
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2018-08-02', '2', '1', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2018-08-04', '1', '4', '2')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2018-08-04', '1', '3', '4')
insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4')
Truncate table Items
insert into Items (item_id, item_brand) values ('1', 'Samsung')
insert into Items (item_id, item_brand) values ('2', 'Lenovo')
insert into Items (item_id, item_brand) values ('3', 'LG')
insert into Items (item_id, item_brand) values ('4', 'HP')
*/
-- Write an SQL query to find for each user whether the brand of the second item (by date)
-- they sold is their favorite brand. If a user sold less than two items, report the 
-- answer for that user as no. It is guaranteed that no seller sold more than one item on a day.

-- Return the result table in any order.

-- Postgres, Oracle, MySQL, SQLServer
select u.user_id seller_id,
       case when u.favorite_brand = o.item_brand then 'yes'
            else 'no'
        end "2nd_item_fav_brand"
  from Users u
  left join (
            select seller_id,
                   i.item_brand
              from (
                    select seller_id,
                           item_id,
                           row_number() over (partition by seller_id order by order_date) rn
                      from Orders o
                   ) o
              join items i
                on i.item_id = o.item_id
             where rn = 2
            ) o
     on o.seller_id = u.user_id
    ;
