# [1] Views 

* A view is a database object that is of a stored query.
* A view can be accessible as a virtual table in PostgreSQL.
* In other words, a PostgreSQL view is a logical table that represents data of one or more underlying tables through a SELECT statement.

![](C:\Users\1000249643\Desktop\Programming Langauages\SQL Jose Portilla Udemy\Images\7.PNG)

* **Notice that a view does not store data physically.**
* Like a table, you can grant permissions to users through a view that contains specific data that the users are authorized to see.
* A view provides a consistent layer even the column of underlying table changes.
* Syntax:

```sql
CREATE VIEW view_name AS query;
```

* Example

```sql
SELECT first_name, last_name, email, address, phone
FROM customer
JOIN address 
ON customer.address_id = address.address_id;
```

* Note that if we want to save this query as a view we have to use VIEW 

```sql
CREATE VIEW customer_info AS
SELECT first_name, last_name, email, address, phone
FROM customer
JOIN address 
ON customer.address_id = address.address_id;
```

* Now observing the view

```sql
SELECT * FROM customer_info;
```

* Hence **notice that view is just a virtual table meaning its not making copy of the actual data. Its just viewing data from the other table based on the sql query given while creating this virtual table**.

## [1.1] Alter View

```sql
ALTER VIEW customer_info RENAME TO customer_master_list;

--SELECT * FROM customer_master_list;
```

* ALTER VIEW is used to create an alternate view like a copy

## [1.2] DROP View

```sql
DROP VIEW IF EXISTS customer_master_list;
```

