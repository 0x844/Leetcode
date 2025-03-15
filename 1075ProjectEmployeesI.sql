# Write your MySQL query statement below
SELECT project_id, round(AVG(e.experience_years),2) as average_years FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY project_id
