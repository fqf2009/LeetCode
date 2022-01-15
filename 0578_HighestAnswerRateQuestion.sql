/*
drop table if exists SurveyLog;
Create table If Not Exists SurveyLog (id int, action varchar(255), question_id int, answer_id int, q_num int, timestamp int);
Truncate table SurveyLog;
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '285', null, '1', '123');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'answer', '285', '124124', '1', '124');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'show', '369', null, '2', '125');
insert into SurveyLog (id, action, question_id, answer_id, q_num, timestamp) values ('5', 'skip', '369', null, '2', '126');
*/

-- The answer rate for a question is the number of times a user answered the question by the
-- number of times a user showed the question.

-- Write an SQL query to report the question that has the highest answer rate. If multiple questions 
-- have the same maximum answer rate, report the question with the smallest question_id.

-- Use Pandas to load test data set of json format into postgres
/*
data = json.load(open('survey.json'))
{'headers': {'SurveyLog': ['id',
   'action',
   'question_id',
   'answer_id',
   'q_num',
   'timestamp']},
 'rows': {'SurveyLog': [[5, 'show', 285, None, 1, 1],
   [5, 'answer', 285, 123, 1, 2],
   [6, 'show', 285, None, 1, 3],
   [6, 'answer', 285, 123, 1, 4],
   [5, 'show', 369, None, 2, 5],
   [5, 'answer', 369, 123, 2, 6],
   [5, 'skip', 369, None, 2, 7]]}}

df = pd.DataFrame(data['rows']['SurveyLog'], columns=data['headers']['SurveyLog'])
   id  action  question_id  answer_id  q_num  timestamp
0   5    show          285        NaN      1          1
1   5  answer          285      123.0      1          2
2   6    show          285        NaN      1          3
3   6  answer          285      123.0      1          4
4   5    show          369        NaN      2          5
5   5  answer          369      123.0      2          6
6   5    skip          369        NaN      2          7

import sqlalchemy as sqla
db = sqla.create_engine('postgresql://user1:secret@localhost:5432/db1')
df.to_sql('surveylog', con=db, index=False, if_exists='append')
*/

-- Postgres
select question_id  survey_log 
  from surveylog s
 group by question_id
 order by (count(*) filter (where action = 'answer'))::numeric / 
          count(*) filter (where action = 'show') desc,
          question_id
 limit 1
;

-- MySQL
select question_id  survey_log 
  from surveylog s
 group by question_id
 order by sum(case when action = 'answer' then 1 else 0 end) /
          sum(case when action = 'show'   then 1 else 0 end) desc,
          question_id
 limit 1
;

-- Oracle
select survey_log
  from (
        select question_id  survey_log 
          from surveylog s
         group by question_id
         order by sum(case when action = 'answer' then 1 else 0 end) /
                  sum(case when action = 'show'   then 1 else 0 end) desc,
                  question_id
       )
 where rownum = 1
 ;
