# Write your MySQL query statement below

SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COUNT(e.student_id) AS attended_exams

FROM Students as s
CROSS JOIN Subjects AS sub
LEFT JOIN Examinations AS e

ON e.subject_name = sub.subject_name
AND s.student_id = e.student_id

GROUP BY
    s.student_id, 
    s.student_name, 
    sub.subject_name

ORDER BY
    s.student_id,
    sub.subject_name
    ASC
;
