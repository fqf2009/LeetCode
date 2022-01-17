/*
Drop table if exists Student;
Drop table if exists Department;
Create table If Not Exists Student (student_id int,student_name varchar(45), gender varchar(6), dept_id int);
Create table If Not Exists Department (dept_id int, dept_name varchar(255));
Truncate table Student;
insert into Student (student_id, student_name, gender, dept_id) values ('1', 'Jack', 'M', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('2', 'Jane', 'F', '1');
insert into Student (student_id, student_name, gender, dept_id) values ('3', 'Mark', 'M', '2');
Truncate table Department;
insert into Department (dept_id, dept_name) values ('1', 'Engineering');
insert into Department (dept_id, dept_name) values ('2', 'Science');
insert into Department (dept_id, dept_name) values ('3', 'Law');
*/

-- Write an SQL query to report the respective department name and number 
-- of students majoring in each department for all departments in the Department 
-- table (even ones with no current students).

-- Return the result table ordered by student_number in descending order. In case 
-- of a tie, order them by dept_name alphabetically.


-- Better
select d.dept_name,
       coalesce(s.student_number, 0) student_number
  from department d
  left join (
            select s.dept_id,
                   count(*) student_number
              from student s
             group by s.dept_id
            ) s
    on d.dept_id = s.dept_id
 order by 2 desc, 1
 ;


-- Not the best
select dept_name,
       student_number
  from (
        select d.dept_id,                         -- this is necessary, unless dept_name is unique
               d.dept_name,
               count(s.student_id) student_number -- cannot be count(*)
          from department d 
          left join student s 
            on d.dept_id = s.dept_id
         group by d.dept_id, 
                  d.dept_name
       ) d
 order by 2 desc, 1;
