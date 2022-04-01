-- Postgres, Oracle, MySQL, SQLServer
select student_id, 
       course_id,
       grade
  from (
        select student_id, 
               course_id,
               grade,
               rank() over (partition by student_id
                            order by grade desc, course_id asc) rk
          from Enrollments
        ) e
  where rk = 1
  ;
  