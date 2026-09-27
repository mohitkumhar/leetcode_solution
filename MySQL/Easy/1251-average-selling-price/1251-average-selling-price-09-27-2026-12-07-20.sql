# Write your MySQL query statement below

SELECT 
    p.product_id,
    COALESCE(
        ROUND(
        SUM(u.units * p.price) / SUM(u.units),
        2
    ), 0
    ) AS average_price

FROM Prices AS p
LEFT JOIN UnitsSold AS u
    ON p.product_id = u.product_id
    AND p.start_date <= u.purchase_date 
    AND p.end_date >= u.purchase_date

GROUP BY p.product_id;
