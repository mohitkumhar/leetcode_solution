# Write your MySQL query statement below

SELECT unique_id, name
from Employees as e
LEFT JOIN EmployeeUNI as eu
ON e.id = eu.id;
