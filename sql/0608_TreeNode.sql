/*
drop table if exists tree;
Create table If Not Exists Tree (id int, p_id int);
Truncate table Tree;
insert into Tree (id, p_id) values ('1', null);
insert into Tree (id, p_id) values ('2', '1');
insert into Tree (id, p_id) values ('3', '1');
insert into Tree (id, p_id) values ('4', '2');
insert into Tree (id, p_id) values ('5', '2');
-- Second test case, only one node, easy to fail
Truncate table Tree;
insert into Tree (id, p_id) values ('1', null);
*/

-- Each node in the tree can be one of three types:
--  - "Leaf": if the node is a leaf node.
--  - "Root": if the node is the root of the tree.
--  - "Inner": If the node is neither a leaf node nor a root node.
-- Write an SQL query to report the type of each node in the tree.
-- Return the result table ordered by id in ascending order.

-- Postgres, Oracle, MySQL
select t.id, 
       coalesce(t3.type, 'Inner') "type"
  from tree t
  left join (
            select id, 'Root' "type"
              from tree
             where p_id is null
             union all
            select id, 'Leaf'
              from tree t1
             where t1.p_id is not null
               and not exists (
                    select null
                      from tree t2
                     where t2.p_id = t1.id
                   )
       ) t3
    on t.id = t3.id
 order by t.id
;


-- use left join instead
select distinct p.id,   -- distinct is important
       case when p.p_id is null then 'Root'
            when c.id is null then 'Leaf'
            else 'Inner'
        end "type"
  from tree p
  left join tree c
    on p.id = c.p_id
 order by 1
;
