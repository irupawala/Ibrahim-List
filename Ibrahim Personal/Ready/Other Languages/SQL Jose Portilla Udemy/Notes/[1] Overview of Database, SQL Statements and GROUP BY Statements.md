# [1] Overview of Database

* Definition
  * Databases are systems that allow users to store and organize data.
  * Users are Analysts, Software Engineers, Data Scientists.

* Spreadsheet:
  * one-time analysis
  * reasonable data set size
  * gives ability to untrained people to work with data.
* Databases:
  * Data Integrity
  * Can handle massive amount of data
  * Quickly combine different datasets
  * Automate steps for re-use
  * Can support data for websites and applications
* Leveraging spreadsheets knowledge to database:
  * Tabs in spreadsheets is tables in database.
  * Rows and columns are same in database. 

* Database Platform Options:

  * PostgreSQL
  * MySQL
  * SQLite

* SQL

  * Structured Query Language is the programming language used to communicate with our Database.

  * SQL language is case insensitive

  * Convention is to write SQL keyword in uppercase.

    

# [2] SQL Statement and Fundamentals

* Cheat sheet :

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\CheatSheet\Screen-Shot-2016-04-17-at-12.22.49-PM.png)

## [2.1] SELECT 

* Also called as **SELECT Clause**.

* Syntax:
  ```sql
  SELECT column1, column2,.... FROM table_name
  ```
  
  * If you want to query data from all column, you can use an asterisk (*) as the shorthand for all columns.*
  
  * It is not good practice to use the asterisk (*) in the SELECT statement as the data table can be really large and this makes server work harder and increase traffic between the database server and applications. As a result, it slows down your applications.
  
  * e.g:
    ```sql
    SELECT * FROM customer;
    
    SELECT first_name, last_name, email FROM customer;
    ```
    
    

## [2.2] SELECT DISTINCT 

* I an table, a column may contain duplicate values and sometimes you only want to list distinct values.

* DISTINCT keyword can be used to return only distinct values.

* Syntax:
  ```sql
  SELECT DISTINCT from column1, column2,......FROM table_name
  ```
  
  Other Examples:
  
  ```sQL
  SELECT DISTINCT release_year FROM film;
  SELECT DISTINCT rating FROM film;
  ```

## [2.3] SELECT WHERE

* What if we want to query just particular rows from a table ?

* Syntax:

  ```sql
  SELECT column1, column2...... FROM table_name WHERE conditions;
  ```

  

  ![](C:\Users\1000249643\Desktop\Capture.PNG)

* If you want to get all customers whose first name is Jamie and last name is Rice, then you can use WHERE clause as follows.

  ```sql
  SELECT first_name, last_name, FROM customer WHERE first_name = "Jamie" AND last_name = "Rice";
  ```

* To select a customer who paid rental < 1 OR > 8
  
  ```sql
  SELECT cutomer_id, amount, payment_date FROM payment WHERE amount <= 1 OR amount >= 8;
  ```
  
* Other Example:
  ```sql
  - SELECT first_name, last_name  FROM customer WHERE store_id=1; --Note here in this example that the columns to be queries doesn't necessarily needed to be included in the WHERE condition.**
  - SELECT * from payment WHERE amount >= 5;
  - SELECT amount, payment, date FROM payment WHERE amount = 4.99 AND amount = 1.99
  - SELECT * from customer WHERE store_id = 1 AND address_id > 5;
  ```

* Challenge Questions:

```sql
-- SELECT * FROM CUSTOMER;
-- Pulling out the email of the cust named Nancy Thomas
SELECT first_name, last_name, email FROM CUSTOMER WHERE first_name='Nancy' AND last_name='Thomas';
SELECT title, description FROM film WHERE title = 'Outlaw Hanky';
SELECT phone FROM address WHERE address='259 Ipoh Drive';
```

## [2.4] COUNT

* Syntax:

```sql
SELECT COUNT(*) FROM table;
```

* The COUNT(*) function returns the number of rows returned by a SELECT clause.
* When you apply the COUNT(*) to the entire table, PostgreSQL scans table sequentially.
* You can also specify a specific column count for readability

```sql
SELECT COUNT(column) FROM table;
```

* Similar to the COUNT(*) function, the COUNT(column) function returns the number of rows returned by a SELECT clause.
* **However, it does not consider NULL values in the column.**
* Finally we can use COUNT with DISTINCT, for example:

```sql
SELECT COUNT(DISTINCT column) FROM table;
```

* Example:

```sql
SELECT COUNT(*) FROM table;
SELECT COUNT(DISTINCT amount) FROM payment;
SELECT COUNT(DISTINCT (amount)) FROM payment; -- This is also same as above statment
```

## [2.5] LIMIT

* LIMIT allows you to limit the number of rows you get back after a query.

```SQL
SELECT * FROM CUSTOMER LIMIT 5;
```

## [2.6] ORDER BY

* When you query data from a table PostgreSQL returns the rows in the order that they were inserted into the table.
* In order to sort the result set, you use the ORDER BY clause in the SELECT statement.
* The ORDER BY clause allows you to sort the rows returned from the SELECT statement in ascending or descending order based on criteria specified.
* Syntax:

```SQL
SELECT column_1, column_2 FROM table_name ORDER BY column_1 ASC/DESC;
```

* If you sort the result set by multiple columns, use a comma to separate between two columns.
* If you leave it blank, the ORDER BY clause will use ASC by default.
* Example: 

```sql
SELECT * FROM CUSTOMER;
SELECT first_name, last_name FROM customer ORDER BY first_name ASC;
SELECT first_name, last_name FROM customer ORDER BY last_name DESC;
SELECT first_name, last_name FROM customer ORDER BY first_name ASC, last_name DESC;
```

* Special Example only allowed in PostGre SQL:

* ```sql
  SELECT first_name FROM customer ORDER BY last_name ASC;
  ```

* The above example is only allowed in Postgre SQL most other SQL engines like MySQL and Oracle Databases only allows you to **ORDER the columns which are listed in the SELECTION list.**
* Also it is not recommended to use these statements as it cannot be shared to other engines.

```sQL
SELECT first_name, last_name FROM customer ORDER BY last_name ASC;
```

* customer_id for the top 10 payment amounts

```sql
SELECT customer_id, payment, amount FROM payment ORDER BY amount DESC LIMIT 10;
```

* select title for the first 5 film_ids

```sql
SELECT film_id, title FROM film ORDER by film_id ASC LIMIT 5
```

## [2.7] BETWEEN

* Between operators are used to match a value against a range of values.

```sql
value BETWEEN low AND high;
```

* If the value is greater than or equal to the low value and less then or equal to the high value, then the expression returns true and vice versa.
* We can rewrite the BETWEEN operator by using the greater than or equal (>=) or less than or equal (<=) operators as the following statement:

```sql
value >= low and value <= high;
```

* If we want to check if a value is out of range, we use the NOT BETWEEN operator as follows:

```sql
value NOT BETWEEN low AND high;
```

* can also be written as follows:

```sql
value < low OR value > high;
```

* Other Examples:

```sql
SELECT customer_id, amount FROM payment WHERE amount NOT BETWEEN 8 AND 9;
SELECT amount, payment_date FROM payment WHERE payment_date BETWEEN '2007-02-07' AND '2007-02-15'
```

## [2.8] IN 

* You use the IN operator with the WHERE clause to check if a value matches any value in a list of values.
* Syntax

```sql
value IN (value1, value2, ........)
```

* **The list of values is not limited to a list of numbers or strings but also a result set of a SELECT statement** as shown in the following query:

```sql
value IN (SELECT value FROM tbl_name)
```

* Just like with BETWEEN, you can use NOT to adjust an IN statement (NOT IN)
* Other examples:

```sql
SELECT customer_id, rental_id, return_date FROM rental WHERE customer_id IN (1, 2, 7, 13, 10) ORDER BY return_date DESC;
```

* This is equivalent to:

```sql
SELECT customer_id, rental_id, return_date FROM rental WHERE customer_id=2 OR customer_id=7 OR customer_id=13 OR customer_id=10 ORDER BY return_date DESC;
```

* Note that IN statement is much faster them the OR statements used above 
* Other example

```sql
SELECT * FROM payment WHERE amount in (7.99, 8.99) 
```

## [2.9] LIKE 

* Suppose the store manager asks you find a customer that he does not remember the name exactly.
* He just remembers that customer's first name begins with something like Jen.
* How do you find the exact customer ?.
* You can use the LIKE operator to as the following query:

```sql
SELECT first_name, last_name FROM customer WHERE first_name LIKE 'Jen%'
```

* % character here is referred as **Pattern**
* The query returns rows whose values starts with "Jen" followed by any sequence of characters. This technique is called pattern matching.
* You construct a pattern by combining a string with wildcard characters and use the LIKE or NOT LIKE operator to find the matches.
  * Percent(%) for matching any sequence of characters.
  * Underscore(_) for matching any single character.

* Other Example:

```sql
SELECT first_name, last_name FROM customer WHERE first_name LIKE 'Jen%';
SELECT first_name, last_name FROM customer WHERE first_name LIKE '%y'; -- returns the first_name ending with y
SELECT first_name, last_name FROM customer WHERE first_name LIKE '%er%'; -- returns the names with er anywhere in the first_name
```

* Examples for underscore (_) which helps in matching single character

```sql
SELECT first_name, last_name FROM customer WHERE first_name LIKE '_her%';
```

* Example for NOT LIKE

```sql
SELECT first_name, last_name FROM customer WHERE first_name NOT LIKE 'Jen%';
```

* LIKE operator is case-sensitive for the string provided. To get the results which are case-insensitive. Postgre SQL provides ILIKE statements.

### [2.9.1] ILIKE

Examples:

```sql
SELECT first_name, last_name FROM customer WHERE first_name ILIKE 'BaR%';
```

## [2.10] General Challenge 1

1. How many payment transactions were greater than 5$ ?

```sql
SELECT COUNT (*) FROM payment WHERE amount > 5;
```

2. How many actors have a first name that starts with the letter P ?

```sql
SELECT COUNT(*) FROM actor WHERE first_name LIKE 'P%';
```

3. **How many unique districts are our customers from ?**

```sql
SELECT COUNT(DISTINCT(district)) FROM address;
```

4. Retrieve the list of names for those distinct district from the previous question.

```sql
SELECT COUNT(DISTINCT(district)) FROM address;
```

5. How many films have a rating of R and a replacement cost between $5 and $15 ?

```sql
SELECT COUNT(*) FROM film WHERE Rating = 'R' AND replacement_cost BETWEEN 5 AND 15;
```

6. How many films have the word Truman somewhere in the title ?

``` sql
SELECT COUNT(*) FROM film WHERE title ILIKE '%truman%';
```

# [3] GROUP BY Statements

## [3.1] MIN MAX AVG SUM Aggregate Functions

* Aggregates the data in all the rows and combines it to a single value.

### [1] AVG

```sql
SELECT * FROM payment LIMIT 5;
SELECT AVG(amount) FROM payment;
```

### [2] ROUND Function

```sql
SELECT ROUND(AVG(amount),5) FROM payment;
```

### [3] Min

```sql
SELECT MIN(amount) FROM payment;
SELECT COUNT(amount) FROM payment where amount = 0.00;
```

### [4] Max

```sql
SELECT MAX(amount) FROM payment;
```

### [5] Sum

```sql
SELECT SUM(amount) FROM payment;
SELECT ROUND(SUM(amount), 1) FROM payment;
```

## [3.2] GROUP BY

* The GROUP BY clause divides the rows returned from the SELECT statement into groups.
* For each group, you can apply a aggregate function, for example: 
  * calculating the sum of items
  * count the number of items in the groups.
* Syntax:

```sql
SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1
```

* Some Examples:
* Without Aggregate what GROUP BY does is it just returns the unique values which it is functions similarly to SELECT DISTINCT

```sql
SELECT customer_id 
FROM payment
GROUP BY customer_id;
```

* Note that **Postgre SQL is flexible with GROUP BY but similar to ORDER BY other SQL engines are not hence the columns which is to be used with GROUP BY statement should also be included with SELECT statement**.
* **Also notice that in other SQL engines GROUP BY statements are not allowed to be used without the use of aggregate function as we did in the example above.**

```sql
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id; -- This says that sum all the amount paid by particular customer_id
```

* We can also use ORDER BY statement with GROUP BY

```sql
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id 
ORDER BY SUM(amount) DESC;
```

* We can also use the GROUP BY to count the number of entries in each group of values of a particular column

```sql
SELECT staff_id, COUNT(payment_id) FROM payment GROUP BY staff_id;
--Note here that instead of payment_id we can use any other column name or also (*)
SELECT staff_id, COUNT(*) FROM payment GROUP BY staff_id;
```

* How many films do each rating types has:

```sql
SELECT title, rating FROM film;
SELECT rating, COUNT(*) FROM film GROUP BY rating ORDER BY COUNT(*);
```

* Get the counts of various rental durations

```sql
SELECT rental_duration, COUNT(rental_duration) FROM film GROUP BY rental_duration;
```

* Get the average rental rate for movie rating

```sql

```

* We have two staff members with Staff IDs 1 and 2. We want to give a bonus to the staff member that handled the most payments.
* How many payments did each staff member handle ? And how much was the total amount processed by each staff member

```sql
SELECT staff_id, COUNT(amount), SUM(amount)
FROM payment 
GROUP BY staff_id 
ORDER BY COUNT(*) DESC;
```

* Corporate headquarters is auditing our store ! They want to know the average replacement cost of movies by rating.
* For example, R rated movies have an average replacement cost of 20.23$

```sql
SELECT rating, ROUND(AVG(replacement_cost), 2) FROM film GROUP BY rating;
```

* We want to send coupons to the 5 customers who have spent the most amount of money.
* Get me the customer ids of the top 5 spenders.

```sql
SELECT customer_id, SUM(amount) FROM payment GROUP by customer_id ORDER BY SUM(amount) DESC LIMIT 5;
```

## [3.3] HAVING

* We often use the HAVING clause in conjunction with the GROUP BY clause to filter group rows that do not satisfy a specified condition.
* Syntax:

```sql
SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1 HAVING condition;
```

* **The HAVING clause sets the condition for group rows created by the GROUP BY clause after the GROUP BY clause applies while the WHERE clause sets the condition for individual rows before GROUP BY clause applies.**
* This is the main difference between the HAVING and WHERE statements.

```sql
SELECT customer_id, SUM(amount) FROM payment GROUP BY customer_id HAVING SUM(amount) > 200; 
```

* Note here that the HAVING statement can only be used with GROUP BY

```sql
SELECT store_id, COUNT(customer_id) FROM customer GROUP BY (store_id) HAVING COUNT(customer_id) > 300;
```

* Combination of WHERE BY, GROUP BY and HAVING statements

```sql
SELECT rating, AVG(rental_rate) FROM film WHERE rating IN ('R', 'G', 'PG') GROUP BY rating HAVING AVG(rental_rate) < 3;
```

* Challenge Question 1: The requirements for our platinum credit card is that customer should have at least a total of 40 transaction payments. What customers (by customer_id) are eligible for the credit cards ?

```sql
SELECT rating, AVG(rental_rate) FROM film WHERE rating IN ('R', 'G', 'PG') GROUP BY rating HAVING AVG(rental_rate) < 3;
```

* Challenge Question 2: When grouped by rating, what movie ratings have an average rental duration of more than 5 days ?

```sql
SELECT rating, ROUND(AVG(rental_duration),2) FROM film GROUP BY rating HAVING AVG(rental_duration) > 5;
```

# [4] Assessment Test

* Return the customer IDs of customers who have spent at least $110 with the staff member who have an ID of 2.

```sql
SELECT customer_id, SUM(amount) FROM payment WHERE staff_id = 2 GROUP BY customer_id HAVING SUM(amount) > 110 ORDER BY customer_id ASC;
```

* How many films begin with the letter J?

```sql
SELECT COUNT(title) FROM film WHERE title LIKE 'J%';
```

* What customer has the highest customer ID number whose name starts with an 'E' and has an address lower than 500 ?

```sql
SELECT first_name, last_name, customer_id FROM customer WHERE first_name LIKE 'E%' AND address_id < 500 ORDER BY customer_id DESC LIMIT 1;
```

