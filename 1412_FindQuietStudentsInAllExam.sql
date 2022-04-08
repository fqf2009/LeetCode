/*
Drop table If Exists Student;
Drop table If Exists Exam;
Create table If Not Exists Student (student_id int, student_name varchar(30));
Create table If Not Exists Exam (exam_id int, student_id int, score int);
Truncate table Student;
insert into Student (student_id, student_name) values ('1', 'Daniel');
insert into Student (student_id, student_name) values ('2', 'Jade');
insert into Student (student_id, student_name) values ('3', 'Stella');
insert into Student (student_id, student_name) values ('4', 'Jonathan');
insert into Student (student_id, student_name) values ('5', 'Will');
Truncate table Exam;
insert into Exam (exam_id, student_id, score) values ('10', '1', '70');
insert into Exam (exam_id, student_id, score) values ('10', '2', '80');
insert into Exam (exam_id, student_id, score) values ('10', '3', '90');
insert into Exam (exam_id, student_id, score) values ('20', '1', '80');
insert into Exam (exam_id, student_id, score) values ('30', '1', '70');
insert into Exam (exam_id, student_id, score) values ('30', '3', '80');
insert into Exam (exam_id, student_id, score) values ('30', '4', '90');
insert into Exam (exam_id, student_id, score) values ('40', '1', '60');
insert into Exam (exam_id, student_id, score) values ('40', '2', '70');
insert into Exam (exam_id, student_id, score) values ('40', '4', '80');
*/
-- A quiet student is the one who took at least one exam and did not score
-- the high or the low score.
-- Write an SQL query to report the students (student_id, student_name) 
-- being quiet in all exams. Do not return the student who has never 
-- taken any exam.
-- Return the result table ordered by student_id.

-- Postgres, Oracle, MySQL, SQLServer
select s.student_id, 
       student_name
  from student s
  join (
        select distinct student_id
          from exam
         where student_id not in (
                select student_id
                  from (
                        select student_id,
                               rank() over (partition by exam_id order by score) rk1,
                               rank() over (partition by exam_id order by score desc) rk2
                          from exam
                       ) e
                 where rk1 = 1 or rk2 = 1
               )
       ) e
    on s.student_id = e.student_id
 order by s.student_id;
