# Write your MySQL query statement below
Select product_name,year,price
from sales
inner join product
on product.product_id = sales.product_id
