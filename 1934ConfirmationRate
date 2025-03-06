SELECT user_id, ROUND(total_confirms/total_messages,2) as confirmation_rate FROM 
    (SELECT s.user_id,
    SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) AS total_confirms,
    COUNT(*) as total_messages
    FROM Signups s
    LEFT JOIN Confirmations c ON c.user_id = s.user_id # left join to include values with no data
    GROUP BY user_id) AS subq
