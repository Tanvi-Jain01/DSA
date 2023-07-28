<h2><a href="https://leetcode.com/problems/find-customer-referee">584. Find Customer Referee</a></h2><h3>Easy</h3><hr><p>Table: <code>Customer</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to report the names of the customer that are <strong>not referred by</strong> the customer with <code>id = 2</code>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
<strong>Output:</strong> 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
</pre>



 ### learn COALSCE function
 ```python
 SELECT name, COALESCE(email, 'Not available') AS email
FROM employees;
 ```
**In this query, the COALESCE function will check if the "email" column has a non-null value for each row. If the email is not null, it will be displayed in the result. If it is null, the COALESCE function will return the fallback value 'Not available,' and that value will be displayed in the result instead of null.

COALESCE is a helpful function for handling null values and providing meaningful default values in SQL queries. It ensures that the query results are more informative and easier to work with, especially when dealing with missing data.**
