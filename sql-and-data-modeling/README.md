# SQL and Data Modeling for the Web
## Course Introduction
Topics covered:
* How to do *Create*, *Read*, *Update*, and *Delete* (*CRUD*) operations
* How to apply these operations across both *databases* and *web applications*
* How to set up *relationships* between elements of an application
* How to think about important principles and patterns in building *data models* for a web application
### Tech Stack
* Python 3
* `Flask`
* `PostgresSQL`
* `psycopg2`
* `SQLAlchemy`
* `Flask-SQLAlchemy`
## Lesson 2: Interacting with Databases
### Intro
Topics covered:
* Interacting with a remote database (Postgres)
* Database Application Programming Interfaces (DBAPI)
* `psycopg2`

### Relational Databases
A database is a collection of data. A database system is a system for storing, retrieving, and writing data to ta database. Benefits of databases include:
* Persistence
* Shared source of truth
* Ability to store many types of data
* Concurrency control
  There are many other types of databases not covered in this course:
* Document stores, like MongoDB
* Object databases, like Perst
* Column stores, like Cassandra
* Graph databases like Neo4j
#### Additional Resources
*  [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)  Udacity course
*  [An Introduction to Relational Databases](https://www.youtube.com/watch?v=z2kbsG8zsLM)  YouTube video

### Primary Keys & Foreign Keys
#### Primary Key
Every row should have a column or set of columns that is a unique identifier for a particular row. PKs with multiple columns are known as **composite keys**.
#### Foreign Key
A primary key in another table, these are used to map relationships between tables.

### SQL
Structured Query Language (SQL) is a standard language for interacting with a database. There are many different dialects of SQL. This course will cover:
* `INSERT`
* `UPDATE`
* `DELETE`
* `SELECT`
* `CREATE TABLE`
* `ALTER TABLE`
* `DROP TABLE`
* `ADD COLUMN`
* `DROP COLUMN`
* `INNER/OUTER JOIN` (`LEFT` and `RIGHT`)
* `GROUP BY`, `SUM`, and `COUNT`
### Execution Plan
The DBMS takes SQL and generates a query plan. The plan can be reviewed and the query tweaked to improve performance. See also:
* [Explaining the unexplainable – part 2 – select * from depesz;](https://www.depesz.com/2013/04/27/explaining-the-unexplainable-part-2/#seq-scan)
* [25 tips to Improve SQL Query Performance - WinWire](https://www.winwire.com/25-tips-to-improve-sql-query-performance/)
* [PostgreSQL CREATE INDEX By Practical Examples](http://www.postgresqltutorial.com/postgresql-indexes/postgresql-create-index/)
* [Use the Force, Luke](https://i.imgflip.com/3oakl8.jpg)
* [What is a HashTable Data Structure](https://www.youtube.com/watch?v=MfhjkfocRR0)  video explanation by Paul Programming
*  [Intro to Hash tables](https://www.slideshare.net/AmyHua/intro-to-hash-tables)
### Client-Server Model
A server is a centralized program that communicates over a network to provide some service to *clients*. A client is a program (a web browser, for instance) that can request data from the server.
#### Adding databases
A database client is any program that can send a request to a database. The web server can simultaneously be a client of the database.

```
Client ---> Server ---> Database
```

### TCP/IP
Transmission Control Protocol/Internet Protocol (TCP/IP) is a set of communication rules that hosts use to communicate with one another on the Internet. Postgres fulfills the standard client/server model and was designed to be used over the web.

An IP address identifies the location of a computer on a network. Each IP address has many ports, which are used to route different types of traffic. HTTP traffic typically uses port 80 and Postgres typically uses 5432.

#### Additional Resources
* In addition to *port 80* and *port 5432*, there are a number of other common ports you might want to get familiar with. Here’s a list of  [14 of the most common ports](https://opensource.com/article/18/10/common-network-ports) .
* If you’re interested in going into much greater depth on computer networking, you can check out the free  [Udacity Course on Computer Networking offered by Georgia Tech](https://www.udacity.com/course/computer-networking--ud436) .

### Connections and Sessions in TCP/IP
Since TCP/IP is a connection-based protocol, a client and server will need to establish a **connection** to communicate with one another. Connecting starts a **session**. In a database session, many **transaction** can occur. A **transaction** does work to commit changes to a database.
### Transactions
Transactions capture logical bundles of work. Work is structured into transactions so that it can either succeed or fail. In case of success, the work is done, and in case of failure, the transaction is rolled back. To ensure consistency and integrity, databases use these atomic transactions to handle commits and rollbacks correctly. These are known as **[ACID transactions](https://www.geeksforgeeks.org/acid-properties-in-dbms/)**:
* Atomic
* Consistency
* Isolation
* Durability
