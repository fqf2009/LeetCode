/*
Drop Table If Exists Variables;
Drop Table If Exists Expressions;
Create Table If Not Exists Variables (name varchar(3), value int);
Create Table If Not Exists Expressions (left_operand varchar(3), operator varchar(2), right_operand varchar(3));
Truncate table Variables;
insert into Variables (name, value) values ('x', '66');
insert into Variables (name, value) values ('y', '77');
Truncate table Expressions;
insert into Expressions (left_operand, operator, right_operand) values ('x', '>', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('x', '<', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'y');
insert into Expressions (left_operand, operator, right_operand) values ('y', '>', 'x');
insert into Expressions (left_operand, operator, right_operand) values ('y', '<', 'x');
insert into Expressions (left_operand, operator, right_operand) values ('x', '=', 'x');
*/
-- Write an SQL query to evaluate the boolean expressions in Expressions table.
-- Return the result table in any order.

-- Postgres
select e.left_operand,
       e.operator,
       e.right_operand,
       case when operator = '>' then v1.value > v2.value
            when operator = '=' then v1.value = v2.value
            else v1.value < v2.value
        end value
  from Expressions e
  join variables v1
    on e.left_operand = v1.name
  join variables v2
    on e.right_operand = v2.name
    ;

-- Postgres, MySQL, Oracle, SQL Server
select e.left_operand,
       e.operator,
       e.right_operand,
       case when operator = '>' then
                case when v1.value > v2.value then 'true' else 'false' end
            when operator = '=' then
                case when v1.value = v2.value then 'true' else 'false' end
            else case when v1.value < v2.value then 'true' else 'false' end
        end value
  from Expressions e
  join variables v1
    on e.left_operand = v1.name
  join variables v2
    on e.right_operand = v2.name
    ;
