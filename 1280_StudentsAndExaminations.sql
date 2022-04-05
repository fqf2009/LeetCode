-- Postgres, Oracle, MySQL, SQLServer
select st.student_id,
       st.student_name,
       sb.subject_name,
       coalesce(attended_exams, 0) attended_exams
  from Students st
 cross join subjects sb
  left join (
             select e.student_id,
                    e.subject_name,
                    count(*) attended_exams
               from Examinations e
              group by e.student_id,
                       e.subject_name
       ) e
    on st.student_id = e.student_id
   and sb.subject_name = e.subject_name
 order by st.student_id,
          sb.subject_name
          ;
