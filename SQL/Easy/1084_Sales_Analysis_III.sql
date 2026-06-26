'''
After grouping the products, you need to identify only those groups 
where sales occurred exclusively within a specific time period. 

To do this, compare the total number of sales for a product 
with the number of sales within the group during the target period. 

If the counts match, it indicates that the product was not sold during any other period. 

You can use conditional aggregation to calculate sales for a specific period—summing 
only the sales from that timeframe—thereby determining both the total sales and the sales for that specific period.
'''
SELECT p.product_id, p.product_name
FROM Product p
RIGHT JOIN Sales s ON p.product_id = s.product_id
GROUP BY s.product_id
HAVING COUNT(*) = 
       SUM(CASE WHEN s.sale_date BETWEEN '2019-01-01' AND '2019-03-31' THEN 1 
                ELSE 0 END);