SELECT p.product_name, SUM(o.unit) AS unit FROM Orders o
LEFT JOIN Products p ON p.product_id = o.product_id
WHERE o.order_date LIKE "2020-02-%" 
GROUP BY o.product_id
HAVING unit >= 100
