# Write your MySQL query statement below
# Using left join we can have null values in left side of table.
select  Euni.unique_id, Emp.name from Employees as Emp left join EmployeeUNI as Euni
On Emp.id=Euni.id
