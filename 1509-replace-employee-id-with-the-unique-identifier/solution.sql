# Write your MySQL query statement below
Select unique_id, name
From Employees
left join EmployeeUNI
on EmployeeUNI.id =Employees.id 
