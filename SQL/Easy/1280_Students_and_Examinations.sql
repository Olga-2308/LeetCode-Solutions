'''
First, we join the two tables to create a base structure where, by default, 
there is a record pairing every student with every exam. 

Then, we join the third table, which will be populated with the corresponding values. 

This approach ensures that even if a student has zero exams, the record is preserved.
'''
SELECT s.student_id, s.student_name, sub.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e ON s.student_id = e.student_id 
    AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id ASC, sub.subject_name ASC;