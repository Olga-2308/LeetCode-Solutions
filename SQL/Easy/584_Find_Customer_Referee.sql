# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE ISNULL(referee_id) = 1 OR referee_id != 2;