SELECT name from Employee
WHERE id in (
    SELECT managerId from Employee
    GROUP BY managerId
    HAVING COUNT(*) >=5
);
