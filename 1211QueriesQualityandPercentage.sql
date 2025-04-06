# Write your MySQL query statement below
SELECT query_name, ROUND(SUM(rating/position)/COUNT(CASE WHEN query_name = "Dog" THEN 1 ELSE 0 END),2) as quality, ROUND(SUM(rating < 3)/count(*) * 100,2) as poor_query_percentage FROM Queries
GROUP BY query_name
