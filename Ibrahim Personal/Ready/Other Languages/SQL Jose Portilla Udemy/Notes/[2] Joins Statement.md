# [5] Joins Statement

## [5.1] As Statement

* As allows us to rename columns or table selections with an alias.

```sql
SELECT payment_id AS Vasooli 
FROM payment LIMIT 5;
```

* Consider this example where it is really useful to rename the SUM(amount)

```sql
SELECT customer_id, SUM(amount) AS total_spent 
FROM payment GROUP BY customer_id;
```

## [5.2] Inner Joins

* Joining allows to relate data in one table to the data in other tables.
* There are several kinds of joins including INNER JOIN, OUTER JOIN and self-join.
* Suppose you want to get data from two tables named A and B.

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\1.PNG)

* The B table has the fka field that relates to the primary key of the A table. In a nutshell there is one column which is same in both A and B.
* To get the data from both tables, you use the INNER JOIN clause in the SELECT statement as follows:

```sql
SELECT A.pka, A.c1, B.pkb, B.c2 FROM A INNER JOIN B ON A.pka = B.fka;
```

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\3.PNG)

* In case if the name of the table is long, you can use a table alias and refer the columns as alias.column_name

* **INNER JOIN:**

  * The INNER JOIN clause returns rows in A table that have the corresponding rows in the B table.

  ![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\2.PNG)

* Example:

```sql
SELECT 
customer.customer_id, 
first_name, 
last_name,
email,
amount,
payment_date
FROM customer
INNER JOIN payment ON payment.customer_id = customer.customer_id;
```

* Note that it is not necessary to mention the table_name.column_name where the column exists in only one table. Also see the use of ORDER_BY statement.

```sql
SELECT 
customer.customer_id, 
first_name, 
last_name,
email,
amount,
payment_date
FROM customer
INNER JOIN payment ON payment.customer_id = customer.customer_id
--ORDER BY customer.customer_id DESC;
ORDER BY first_name DESC;
```

* Use of WHERE with JOINS.

```sql
SELECT 
customer.customer_id, 
first_name, 
last_name,
email,
amount,
payment_date
FROM customer
INNER JOIN payment ON payment.customer_id = customer.customer_id
WHERE customer.customer_id = 2;
```

```sql
SELECT 
customer.customer_id, 
first_name, 
last_name,
email,
amount,
payment_date
FROM customer
INNER JOIN payment ON payment.customer_id = customer.customer_id
WHERE first_name LIKE 'A%';
```

**Examples of Inner Join:**

Example 1: Note if we don't mention **INNER** word here then by default also SQL takes it as INNER JOIN

```sql
SELECT payment_id, amount, first_name, last_name FROM payment INNER JOIN staff ON payment.staff_id = staff.staff_id;
```

Example 2:

```sql
SELECT title, COUNT(title) AS copies_at_store_1 FROM inventory INNER JOIN film ON inventory.film_id = film.film_id WHERE store_id = 1 GROUP BY title ORDER BY title;
```

Example 3: Notice in the example below if you rename a string then you need to use that alias everywhere in the query even before declaring it 

```sql
SELECT film.title, lan.name AS movie_language
FROM film 
INNER JOIN language AS lan 
ON film.language_id= lan.language_id;
```

Example 4: Also Notice that AS statement is not mandatory

```sql
SELECT title, name movie_language
FROM film 
INNER JOIN language lan 
ON film.language_id= lan.language_id;
```

## [5.3] Overview of Join Types

Refer the slides here: 

[JOINS-Overview-2.pptx](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Notes)



![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\SQL JOINS.jpg)

Example 1: Left Outer Join Displaying the films not in the inventory but present in the film database

```sql
SELECT film.film_id, film.title, inventory_id
FROM film
LEFT OUTER JOIN inventory ON inventory.film_id = film.film_id
WHERE inventory.film_id IS NULL -- you can also write inventory.inventory_id
ORDER BY film.film_id;
```

* **Note here that even if we just write LEFT here SQL will know it is LEFT OUTER JOIN because of the keyword LEFT**



## [5.4] Union

* Combines result sets of two or more SELECT statements into a single result set.

```sql
SELECT column_1, column_2 FROM tbl_name_1 UNION SELECT column_1, column_2 FROM tbl_name_2;
```

* Rules applied to UNION query:
  * Both queries must return the same number of columns.
  * The corresponding columns in the query must have compatible data types. eg column_1 from both the data table must be of same data type.



* Uses of Union:
  * Removes all duplicate rows unless the UNION ALL is used.
  * Union Operator may place the rows in the first query before, after or between the rows in the result set of the second query.
  * To sort the rows in the combined result set by a specified column, you use the ORDER BY clause.
  * Union can be used to combine data from similar tables that are not perfectly normalized. Join statement doesn't works in this sense. **Union concatenates all the rows in one table to the rows in other**.

```sql
SELECT * FROM sales2007q1 UNION SELECT * FROM sales2007q2; -- UNION will remove all the duplicate columns. To get all the values use UNION ALL

SELECT * FROM sales2007q1 UNION ALL SELECT * FROM sales2007q2
```



# [6] Advanced SQL Commands

## [6.1] Time Stamp

* SQL allows us to use the timestamp data type to retail time information.
* extract function extracts parts from a date.
  * extract (unit from date)
* Extract Function:

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\4.PNG)

**Refer to the Postgre Date time Documentation:**

https://www.postgresql.org/docs/9.1/datatype-datetime.html

https://www.postgresql.org/docs/9.6/functions-datetime.html

Notice that it is possible to perform arithmetic operations like +, - on the date time statements. Refer Documentation.

**Extract Examples**

```sql
SELECT extract(day FROM  payment_date) FROM payment;
```

```sql
SELECT customer_id, extract(day FROM  payment_date) AS day 
FROM payment;
```

Example of getting the month of receiving highest payment

```sql
SELECT SUM(amount) as total, extract(month FROM  payment_date) AS month 
FROM payment
GROUP BY month
ORDER BY total DESC
LIMIT 3;
```

## [6.2] Mathematical Functions

Check the documentation

https://www.postgresql.org/docs/10/functions-math.html

```sql
SELECT customer_id + rental_id AS new_id FROM payment;
SELECT customer_id * rental_id AS new_id FROM payment;
SELECT customer_id - rental_id AS new_id FROM payment;
SELECT customer_id / rental_id AS new_id FROM payment; -- Important, Check it online

SELECT round(AVG(amount), 2) FROM payment;
```

## [6.3] String Function and Operators

Check the documentation

https://www.postgresql.org/docs/9.1/functions-string.html

Concatenate two string columns

```sql
SELECT first_name || ' ' || last_name AS full_name FROM customer;
```

Character length

```sql
SELECT first_name, char_length(first_name) FROM customer;
```

Lower character

```sql
SELECT lower(first_name) FROM customer;
```

**See Documentation for REGEX**

## [6.4] SubQuery

* Suppose we want to find the films whose rental rate is higher than average rental rate.
* We can do it in two steps:
  * Find the average rental rate by using the SELECT statement and average function (AVG).
  * Use the result of the first query in the second SELECT statement to find the films that we want

First Step:

```sql
SELECT AVG(rental_rate) FROM film
```

Second Step:

```sql
SELECT title, rental_rate
FROM film
WHERE rental_rate > 2.98;
```

* Here we want to pass the result of the first query to the second query in one query.
* The solution is to use sub query.
* A subquery is a query nested inside another query.
* To construct a subquery, we put the second query in brackets and use it in the WHERE clause as an expression:

```sql
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);
```

* Return the inventory id for the films released between May 29th and May 30th

```sql
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);
```

* Now we will return the title for these film_id

```sql
SELECT film_id, title
FROM film 
WHERE film_id IN

(SELECT inventory.film_id
FROM rental
INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id
WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30');
```

* Here note that we are getting returned the list of multiple rows returned from the internal query and hence we have to use IN operator
* Note that in the previous example we have used comparator operator '>' and we must use LIKE statement if the string is to be returned. **Hence if a single character/integer is returned we will use comparison operator, equal or LIKE But if subquery is going to return bunch of rows back to you then we have to use IN operator.**

## [6.5] Self-Join

* Joining the table to itself
* You use self join when you want to combine rows with other rows in the same table.
* To perform the self join you must use a table alias to help SQL distinguish the left table from the right table of the same table.
* Consider this:

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\5.PNG)

* Also let us assume that for some reasons we cannot just say this:
  * SELECT employee_name FROM employee WHERE employee_location = "New York"

* So we could use a subquery.

```sql
SELECT employee_name FROM employee WHERE employee_location IN (SELECT employee_location FROM employee WHERE employee_name = "Joe")
```

* While subquery is a valid solution, it is actually more efficient to use a self join, where we join a table to itself !.

```sql
SELECT e1.employee_name FROM employee AS e1, employee AS e2 WHERE e1.employee_location = e2.employee_location AND e2.employee_name="Joe";
```

* Generally, queries that refer to the same table can be greatly simplified by re-writing the queries as self joins.

* There is definitely a performance benefit for this as well.

  

* Let us say we want to retreat all the customers whose last name matches the first name of another customer

```sql
SELECT a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name 
FROM customer AS a, customer AS b
WHERE a.first_name = b.last_name;
```

Also we can use sub join for this same job:

```sql
SELECT a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name 
FROM customer AS a 
JOIN customer AS b -- This is INNER JOIN by default
ON a.first_name = b.last_name
ORDER BY a.customer_id;
```

* Note here that the example above is Inner Join but self join is also capable of performing left join and right join.
* Let us say we want to perform LEFT JOIN which returns the values only in the left table regardless of whether there is a match or not but will only return the values in the right table when there is a match

```sql
SELECT a.customer_id, a.first_name, a.last_name, b.customer_id, b.first_name, b.last_name 
FROM customer AS a 
LEFT OUTER JOIN customer AS b -- Can also write LEFT instead of LEFT OUTER
ON a.first_name = b.last_name
ORDER BY a.customer_id;
```



**Google Employee Manager SELF JOIN**



# [7] Assessment Test 2

Q.1 How can you retrieve all the information from the cd.facilities table?

```sql
SELECT * FROM cd.facilities
```

Q.2 You want to print out a list of all of the facilities and their cost to members. How would you retrieve a list of only facility names and costs?

```sql
SELECT name, membercost, guestcost FROM cd.facilities
```

Q.3 How can you produce a list of facilities that charge a fee to members?

```sql
SELECT name, membercost FROM cd.facilities WHERE membercost != 0;
```

Q.4 How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

```sql
SELECT facid, name, membercost, monthlymaintenance 
FROM cd.facilities 
WHERE membercost != 0 AND membercost < monthlymaintenance/50;
```

Q.5 How can you produce a list of all facilities with the word 'Tennis' in their name?

```sql
SELECT facid, name FROM cd.facilities WHERE name LIKE '%Tennis%'
```

Q.6 How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

```sql
SELECT t1.facid, t1.name, t2.facid, t2.name FROM cd.facilities as t1, cd.facilities as t2 WHERE t2.facid = 1 AND t1.facid = 5;
```

```sql
SELECT t1.facid, t1.name FROM cd.facilities AS t1 
WHERE t1.facid = 5 
UNION 
SELECT t2.facid, t2.name FROM cd.facilities as t2 
WHERE t2.facid = 1;
```

Solution by Jose:

```sql
SELECT * FROM facid WHERE facid IN (1,5);
```

Q.7 How can you produce a list of members who joined after the start of September 2012? Return the memid, surname, first name, and join date of the members in question.

```sql
SELECT memid, surname, firstname, EXTRACT (MONTH FROM joindate) AS MONTH, joindate 
FROM cd.members 
WHERE EXTRACT (MONTH FROM joindate) >= 07;
```

Solution by Jose:

```sql
SELECT memid, surname, firstname, joindate 
FROM cd.members 
WHERE joindate >= '2012-09-01';
```

Q.8 How can you produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.

```sql
SELECT DISTINCT surname FROM cd.members ORDER BY surname LIMIT 10;
```

Q.9 You'd like to get the signup date of your last member. How can you retrieve this information?

```sql
SELECT memid, firstname, surname FROM cd.members ORDER BY memid DESC LIMIT 1;
```

Solution by Jose:

```sql
SELECT MAX(joindate) AS latest FROM cd.members;
```

Q.10 Produce a count of the number of facilities that have a cost to guests of 10 or more.

```sql
SELECT  COUNT(*) FROM cd.facilities WHERE guestcost > 9;
```

Q.11 Skip this one, no question for #11.

Q.12 Produce a list of the total number of slots booked per facility in the month of September 2012. Produce an output table consisting of facility id and slots, sorted by the number of slots.

```sql
SELECT t1.name, t1.facid, SUM(t2.slots) AS total_slots FROM cd.facilities AS t1
JOIN cd.bookings as t2 ON t1.facid = t2.facid

WHERE (EXTRACT (MONTH FROM starttime) = 09) 
GROUP BY t1.name, t1.facid  
ORDER BY total_slots ASC;
```

Solution by Jose:

```sql
select facid, sum(slots) as "Total Slots" from cd.bookings where starttime >= '2012-09-01' and starttime < '2012-10-01' group by facid order by sum(slots);
```

Q.13 Produce a list of facilities with more than 1000 slots booked. Produce an output table consisting of facility id and total slots, sorted by facility id.

```sql
SELECT t1.name, t1.facid, SUM(t2.slots) AS total_slots FROM cd.facilities AS t1
JOIN cd.bookings as t2 ON t1.facid = t2.facid

GROUP BY t1.name, t1.facid HAVING SUM(t2.slots) > 1000
ORDER BY facid ASC;
```

Solution by Jose:

```sql
select facid, sum(slots) as "Total Slots" from cd.bookings group by facid having sum(slots) > 1000 order by facid;
```

Q.14 How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.

```sql
SELECT t1.name, t1.facid, t2.slots, t2.starttime FROM cd.facilities AS t1
JOIN cd.bookings as t2 ON t1.facid = t2.facid 

WHERE t1.name LIKE '%Tennis Court%' AND EXTRACT (DAY FROM t2.starttime) = 21
AND EXTRACT (MONTH FROM t2.starttime) = 09 

ORDER BY t2.starttime ;
```

Solution by Jose:

```sql
select bks.starttime as start, facs.name as name from cd.facilities facs inner join cd.bookings bks on facs.facid = bks.facid where facs.facid in (0,1) and bks.starttime >= '2012-09-21' and bks.starttime < '2012-09-22' order by bks.starttime;
```

Q.15 How can you produce a list of the start times for bookings by members named 'David Farrell'?

```sql
SELECT t1.firstname, t1.surname, t2.memid, t2.starttime FROM cd.members AS t1
JOIN cd.bookings as t2 ON t1.memid = t2.memid 

WHERE t1.firstname = 'David' AND t1.surname = 'Farrell';
```

Solution by Jose:

```sql
select bks.starttime from cd.bookings bks inner join cd.members mems on mems.memid = bks.memid where mems.firstname='David' and mems.surname='Farrell';
```

