DELETE t1 FROM Person t1
JOIN(
    SELECT MIN(id) AS id, email FROM Person
    GROUP BY email
) t2
ON t1.id > t2.id AND t1.email = t2.email
