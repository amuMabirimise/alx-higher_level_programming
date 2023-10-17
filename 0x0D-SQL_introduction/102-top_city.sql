-- select and Displays the top 3 of cities temperature during July an august
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month between 07 and 08 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;i
