# Write your MySQL query statement below
# IFNULL(p1,p2) if p1 null, then replace with p2
SELECT p.product_id, round(IFNULL(SUM(p.price * u.units) / SUM(u.units), 0), 2) as average_price FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id and purchase_date between start_date and end_date
GROUP BY p.product_id
