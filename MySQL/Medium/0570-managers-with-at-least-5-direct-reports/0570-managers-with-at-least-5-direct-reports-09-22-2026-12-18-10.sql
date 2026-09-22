# Write your MySQL query statement below


SELECT e1.name
FROM Employee AS e1

JOIN Employee AS e2

ON e1.id = e2.managerId

GROUP BY
    e1.id, e1.managerId

HAVING 
    COUNT(e1.id) >= 5
;
