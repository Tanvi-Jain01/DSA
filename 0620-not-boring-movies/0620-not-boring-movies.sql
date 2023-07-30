# Write your MySQL query statement below

# select * from Cinema
#  group by id
#  having count(*)%2=1 and description not in ('boring')

# order by rating desc;

select * from Cinema
where id % 2=1 and description not in('boring')
order by rating desc;


# When using aggregate functions like COUNT() in the SELECT clause without a GROUP BY clause, it will return a single value representing the count of all rows in the result set. In this query, the COUNT(id) function is used to count the occurrences of the id values in the entire Cinema table, not for each individual row.