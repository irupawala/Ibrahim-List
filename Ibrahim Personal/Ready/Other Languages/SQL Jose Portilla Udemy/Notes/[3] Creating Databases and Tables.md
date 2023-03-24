# [1.1] Data Types	

* PostgreSQL supports following data types

1. Boolean - Keyword Bool

* When you insert data into a Boolean column PostgreSQL will convert it into the Boolean value e.g. 1, yes, y, t, true are converted to true and 0, no, n, false, f are converted to false.
* When you select data from a Boolean column, PostgreSQL display t for true, f for false and space character for NULL.

2. Character

   i. A single character: char

   ii. Fixed-length character strings

* If you insert a string shorter than the length of the column, Postgre SQL will pad spaces. If longer than the length of the column, Postgre SQL will issue an error.

* E.g Used so that customer does not put any other unintended values in the columns say the column of id numbers.

  iii. Variable-length character strings: varchar(n).

* Can store up to n characters with variable-length character strings. PostgreSQL does not pad spaces when the stored string is shorter than the length of the column.

* E.g Used for people's name.

3. Number

   i. Integers:

   * smallint:
     * 2 bytes signed integer
     * -32768 to +32767
   * Int:
     * 4 bytes integer
     * -214783648 to 214783647

   ii. serial:

   * serial is the same as integer except that PostgreSQL populate value into the column automatically.
   * Similar to AUTO_INCREMENT attribute into other database management system.

   

   4. Floating-point Numbers

   i. Float:

   * 8 bytes

   ii. Real or float8:

   * double-precision(8 -byte) floating-point number

   iii. Numeric or numeric(p,s)

   * real number with p digits with s number after the decimal point. The numeric with (p,) is the exact number.

     

4. Temporal i.e. , data type and time-related data types

* date stores date data

* time stores time data

* timestamp stores date and time

* interval stores stores difference is timestamps

* timestamptz store both timestamp and timezone data

  

5. Special types
6. Array



# [1.2] Primary and Foreign Keys

Primary keys:

* A primary key is a column or group of columns that is used to identify a row uniquely in a table.
* A table can have one and only one primary key.
* When you add a primary key to a table, PostgreSQL creates a unique index on the column or a group of columns used to identify the primary key.
* E.g Customer_id was the primary key column for the customer table we have seen earlier. **customer_id is a primary key because it is used to identify a row uniquely in the table.**
* **Serial datatype should be used for primary keys as it will automatically increment when you add new row to the table.**
* We add the primary key to a table when we define the table's structure using CREATE TABLE statement.
  * CREATE TABLE table_name (column_name data_type PRIMARY KEY, column_name data_type, ......);



Foreign keys:

* **A foreign key is a field or group of fields in a table that uniquely identifies a row in another table.**
* In other words, a foreign key is defined in a table that refers to the primary key of the other table.
* The table that contains the foreign key is called referencing table or child table. And the table to which the foreign key references is called reference table or parent table.
* A table can have multiple foreign keys depending on its relationships with other tables.
* E.g customer_id in the payment table is the foreign key while it is a primary key in the customer table.



* In PostgreSQL, you define a foreign key through a foreign key constraint.
* A foreign key constraint indicates that values in a column or group of columns in the child table match with the values in a column or group of columns of the parent table.



# [1.3] Create Table

## [1] Syntax:

```sql
CREATE TABLE table_name (column_name TYPE column_contraint, table_constraint) INHERITS existing_table_name;
```

* column_constraints defines the rules for the column e.g. NOT NULL.
* Then after the column_list, you define a table level constraint and that defines rules for the data in the table.
* **After that, you specify an existing table from which the new table inherits. It means the new table contains all columns of the existing table and the columns defined in the CREATE TABLE Statement.**



## [2] Postgre SQL Column Constraints

### 1. NOT NULL 

* Value of the column cannot be NULL.

### 2. UNIQUE 

* Value of the column must be unique across the table.

* **However, the column can have many NULL values because Postgre SQL treats each NULL value to be unique.**
* **Notice that SQL standard only allows one NULL value in the column that has the UNIQUE constraint.**

### 3. PRIMARY KEY 

* This constraint is the combination of NOT NULL And UNIQUE constraints.

* You can define one column as PRIMARY KEY by using column-level constraint. In case the primary key contains multiple columns, you must use the table-level constraint.

### 4. CHECK

* Check enables to check a condition when you insert or update data.
* E.g. the values in the price column of the product table must be positive values.

### 5. REFERENCES

* constrains the value of the column that exists in a column in another table.
* References are used for defining foreign key constraints.



## [3] Postgre SQL Table Constraints

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\6.PNG)

## [4] Examples

Table 1:

```sql
CREATE TABLE account(
	user_id serial PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(350) UNIQUE NOT NULL,
	create_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP);

```

Table 2:

```sql
CREATE TABLE role(
role_id serial PRIMARY KEY,
role_name VARCHAR(50) UNIQUE NOT NULL);
```

Table 3:

```sql
CREATE TABLE account_role(
	user_id integer NOT NULL,
	role_id integer NOT NULL,
	grant_date timestamp without time zone,
	PRIMARY KEY (user_id, role_id), -- PRIMARY KEY TABLE LEVEL CONSTRAINTS will be used to define priamry key like this
	
  CONSTRAINT account_role_role_id_fkey FOREIGN KEY (role_id) -- FOREIGN KEY CONSTRAINTS are defined for role_id column from role table
      REFERENCES role (role_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
	
  CONSTRAINT account_role_user_id_fkey FOREIGN KEY (user_id) -- FOREIGN KEY CONSTRAINTS are defined for user_id column from account table
      REFERENCES account (user_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
```

# [1.4] INSERT

* SQL provides the INSERT statement that allows you to insert one or more rows into a table at a time.
* Syntax:

```sql
INSERT INTO table(column1, column2,......)
VALUES (value1, value2,.....)
```

* To add multiple rows use the following syntax

```sql
INSERT INTO table(column1, column2,......)
VALUES (value1, value2,.....),
VALUES (value1, value2,.....), ,,,,,;
```

* To insert data that comes from another table, you use the INSERT IMYP SELECT statement as follows :

```sql
INSERT INTO table
SELECT column1, column2,....
FROM another_table
WHERE condition;
```

Example:

* Consider creating  a table and then inserting columns in to it.

```sql
CREATE TABLE link(
	ID serial PRIMARY KEY,
	url VARCHAR(255) NOT NULL,
	name VARCHAR(255) NOT NULL,
	description VARCHAR(255),
	rel VARCHAR(50)
);
```

* Now let us insert columns 

```sql
--SELECT * FROM link;

INSERT INTO link (url, name)
VALUES ('www.google.com', 'Google');
```

* Notice here if you omit any columns **that accepts a NULL value in the INSERT statement**, the column will take its default value as NULL.
* Also you can specify what default value to take if you don' t want NULL to be automatic default value.

```sql
INSERT INTO link (url, name)
VALUES ('www.facebook.com', 'Yahoo');

--SELECT * FROM link;
```

* Note that ID will get on incrementing automatically each time we add the rows.

```sql
INSERT INTO link (url, name)
VALUES
('www.microsoft.com', 'Microsoft'),
('www.apple.com', 'Apple');
```

## [1] LIKE

* Now let us create another table to learn how to insert the column from one table to another.

```sql
CREATE TABLE link_copy (LIKE link);
```

* Notice the above command carefully. **It copies all the SCHEMAS from the table link to link_copy. Notice here that we are not copying the any table data but only the structure that is columns.**

* Now let us insert the data from one table to another. Notice here we are inserting just one row.

```sql
INSERT INTO link_copy 
SELECT * FROM link
WHERE name = 'Apple';
```

* Now inserting multiple rows

```sql
INSERT INTO link_copy
SELECT * FROM link;
```

* Notice that in this new table the old serial values will be copied.

# [1.5] UPDATE

* Update statement to update existing data in the table.
* To change the values of the columns in a table, you use the UPDATE statement.

```sql
UPDATE table 
SET column1 = value1,
	column2 = value2,....
WHERE condition;
```

* Note here that all the row values of the column1 will get updated with value1.
* If you want to update only certain rows then you have to use WHERE clause.

```sql
UPDATE link
SET description = 'empty description';
```

* In the statement above, all the rows will get updated.
* Similarly multiple rows can also be updated based on condition

```sql
UPDATE link_copy
SET description = 'Work Place'
WHERE name LIKE 'Goo%';
```

* Also you can copy the contents of one column to another.

```sql
UPDATE link_copy 
SET description = name
WHERE name NOT LIKE 'Goo%';
```

## [1] RETURNING

Note that we can get the updated rows using a `RETURNING` KEYWORD. This way we don't have to use `SELECT * FROM table_name;` each time after making any changes to the table. We can observe the columns affected by the change

```sql
UPDATE link_copy 
SET description = name
WHERE name NOT LIKE 'Goo%'
RETURNING *;
-- RETURNING name, description; -- Notice that we can also opt for returning few columns
```

# [1.6] DELETE

Syntax:

```sql
DELETE FROM table
WHERE condition
```

Example

```sql
DELETE FROM link_copy
WHERE name LIKE 'M%'
RETURNING *;
```

# [1.7] ALTER TABLE

To Change existing table structure, you use ALTER TABLE statement.

Syntax:

```sql
ALTER TABLE table_name action;
```

Postgre SQL provides many actions that allow you to:

- Add, remove, or rename column.
- Set default value for the column.
- Add CHECK constraint to a column.
- Rename table

The keywords to use will be:

* ADD COLUMN
* DROP COLUMN
* RENAME COLUMN
* ADD CONSTRAINT
* RENAME TO

Examples:

* To Drop entire table **IF IT EXISTS**

```sql
DROP TABLE IF EXISTS link;
```

* Creating a new table now

```sql
CREATE TABLE link(
	link_id SERIAL PRIMARY KEY,
	title VARCHAR(512) NOT NULL,
	url VARCHAR(1024) NOT NULL UNIQUE
);
```

* Adding a column boolean

```sql
ALTER TABLE link ADD COLUMN active boolean;
```

* Dropping boolean

```sql
ALTER TABLE link DROP COLUMN active;
```

* Renaming a column

```sql
ALTER TABLE link RENAME COLUMN title TO new_title;
```

* Renaming Table

```sql
ALTER TABLE link RENAME to link_new;
```

# [1.8] DROP TABLE

Syntax:

```sql
DROP TABLE [IF EXISTS] table_name;
```

* By writing **Options IF EXISTS** you avoid error messages from Postgre SQL.

```sql
DROP TABLE test_two;
```

* If you try to execute the above command many times than it will give error
* But If you write IF EXISTS then it  will give a warning but not error

```sql
DROP TABLE IF EXISTS test_two;
```

* Notice that there is a keyword "RESTRICT" which gets automatically input WHEN using DROP TABLE.
* What RESTRICT does is it refuses to drop table if there is any object dependent on it.
* PostGre SQL uses RESTRICT by default.

```sql
DROP TABLE IF EXISTS test_two RESTRICT;
```

* If you want to remove the table which has dependencies on it and also remove dependent objects together you can use keyword CASCADE.

```sql
DROP TABLE IF EXISTS test_two CASCADE;
```

# [1.9] CHECK Constraints

* A CHECK constraints is a kind of constraint that allows you to specify if a value in a column must meet a specific requirement.
* The CHECK constraint uses a Boolean expression to evaluate the values of a column.
* If the values of the column pass the check, PostgreSQL will insert or update those values.
* Example:
  * First creating a table with CHECK constraints:

```sql
CREATE TABLE new_users(
	id serial PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	birth_date DATE CHECK(birth_date > '1900-01-01'),
	join_date DATE CHECK(join_date > birth_date),
	salary integer CHECK(salary>0)
	
);
```

* Now let us insert a condition which deliberately violates the condition

```sql
INSERT INTO new_users
	(first_name, birth_date, join_date, salary)
	VALUES ('Ibrahim', '1889-08-21', '2020-01-01', 18000000); 
	
--SELECT * FROM new_users;
```

```sql
INSERT INTO new_users
	(first_name, birth_date, join_date, salary)
	VALUES ('Joe', '1980-02-21', '2020-01-01', -10); 
	
--SELECT * FROM new_users;
```

* Note that in both of these cases the SQL will notify which condition has been violated saying something like this "new_users_salary_check"

* Notice that you can also name your constraint using keyword CONSTRAINT

```sql
CREATE TABLE checktest(
sales integer CONSTRAINT positive_sales CHECK (sales>0));

INSERT INTO checktest
	(sales)
	VALUES (-90); 
```

* Now here when the condition is violated the error returned will be "positive_sales"

# [1.10] NULL constraint

* In database theory, NULL is unknown or missing information.

* The NULL value is different from empty or zero.
* For example, if we don't know the email address of a person we use the NULL value.
* In case the person does not have any email address, we can mark it as an empty string.
* Also zero sales for the month is different from not knowing the sales value.

Examples:

```sql
CREATE TABLE learn_null(
first_name VARCHAR(50) NOT NULL,
sales_no integer NOT NULL)  ;
```

```sql
INSERT INTO learn_null
(first_name)
VALUES ('John');
```

* Note here that if we don't give any value in the sales_no then it will give an error.

  # [1.11] Unique Constraints

* If it is found that the new value is already there, it would give back an error message and reject the changes.

```sql
CREATE TABLE people(
id serial PRIMARY KEY,
first_name VARCHAR(50),
email VARCHAR(100) UNIQUE);
```

```sql
INSERT INTO people
	(first_name, email)
	VALUES ('Joe', 'Joe@joe.com');
```

```sql
INSERT INTO people
	(first_name, email)
	VALUES ('Jacob', 'Joe@joe.com');
```

* Here we will get the error "ERROR:  duplicate key value violates unique constraint "people_email_key""

# [1.11] Assessment Test 3

```sql
CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	homeroom_number INTEGER NOT NULL,
	phone BIGINT NOT NULL UNIQUE,
	email VARCHAR(50) NOT NULL UNIQUE,
	GRADUATION_year INTEGER NOT NULL);
```

```sql
CREATE TABLE teachers(
teacher_id SERIAL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
homeeroom_number INTEGER NOT NULL,
department VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE,
phone BIGINT NOT NULL UNIQUE);
```

```sql
INSERT INTO students
	(first_name, last_name, homeroom_number, phone, email, graduation_year)
    VALUES ('Mark', 'Watney', 5, 7775551234, 'mark@mark.com', 2035);
```

```sql

```

