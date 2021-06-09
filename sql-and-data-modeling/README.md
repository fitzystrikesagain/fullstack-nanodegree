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

A database is a collection of data. A database system is a system for storing, retrieving, and writing data to ta
database. Benefits of databases include:

* Persistence
* Shared source of truth
* Ability to store many types of data
* Concurrency control There are many other types of databases not covered in this course:
* Document stores, like MongoDB
* Object databases, like Perst
* Column stores, like Cassandra
* Graph databases like Neo4j

#### Additional Resources

* [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)  Udacity course
* [An Introduction to Relational Databases](https://www.youtube.com/watch?v=z2kbsG8zsLM)  YouTube video

### Primary Keys & Foreign Keys

#### Primary Key

Every row should have a column or set of columns that is a unique identifier for a particular row. PKs with multiple
columns are known as **composite keys**.

#### Foreign Key

A primary key in another table, these are used to map relationships between tables.

### SQL

Structured Query Language (SQL) is a standard language for interacting with a database. There are many different
dialects of SQL. This course will cover:

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

The DBMS takes SQL and generates a query plan. The plan can be reviewed and the query tweaked to improve performance.
See also:

* [Explaining the unexplainable – part 2 – select * from depesz;](https://www.depesz.com/2013/04/27/explaining-the-unexplainable-part-2/#seq-scan)
* [25 tips to Improve SQL Query Performance - WinWire](https://www.winwire.com/25-tips-to-improve-sql-query-performance/)
* [PostgreSQL CREATE INDEX By Practical Examples](http://www.postgresqltutorial.com/postgresql-indexes/postgresql-create-index/)
* [Use the Force, Luke](https://i.imgflip.com/3oakl8.jpg)
* [What is a HashTable Data Structure](https://www.youtube.com/watch?v=MfhjkfocRR0)  video explanation by Paul
  Programming
* [Intro to Hash tables](https://www.slideshare.net/AmyHua/intro-to-hash-tables)

### Client-Server Model

A server is a centralized program that communicates over a network to provide some service to *clients*. A client is a
program (a web browser, for instance) that can request data from the server.

#### Adding databases

A database client is any program that can send a request to a database. The web server can simultaneously be a client of
the database.

```
Client ---> Server ---> Database
```

### TCP/IP

Transmission Control Protocol/Internet Protocol (TCP/IP) is a set of communication rules that hosts use to communicate
with one another on the Internet. Postgres fulfills the standard client/server model and was designed to be used over
the web.

An IP address identifies the location of a computer on a network. Each IP address has many ports, which are used to
route different types of traffic. HTTP traffic typically uses port 80 and Postgres typically uses 5432.

#### Additional Resources

* In addition to *port 80* and *port 5432*, there are a number of other common ports you might want to get familiar
  with. Here’s a list of  [14 of the most common ports](https://opensource.com/article/18/10/common-network-ports) .
* If you’re interested in going into much greater depth on computer networking, you can check out the
  free  [Udacity Course on Computer Networking offered by Georgia Tech](https://www.udacity.com/course/computer-networking--ud436)
  .

### Connections and Sessions in TCP/IP

Since TCP/IP is a connection-based protocol, a client and server will need to establish a **connection** to communicate
with one another. Connecting starts a **session**. In a database session, many **transaction** can occur. A **
transaction** does work to commit changes to a database.

### Transactions

Transactions capture logical bundles of work. Work is structured into transactions so that it can either succeed or
fail. In case of success, the work is done, and in case of failure, the transaction is rolled back. To ensure
consistency and integrity, databases use these atomic transactions to handle commits and rollbacks correctly. These are
known as **[ACID transactions](https://www.geeksforgeeks.org/acid-properties-in-dbms/)**:

* Atomic
* Consistency
* Isolation
* Durability

### DBAPIs and `psycopg2`

A Database Application Programming Interfaces (DBAPIs) provides a standard interface for a programming language to talk
to a relational database. These are sometimes known as database adapters. Different APIs exist for every server,
framework, or language/database system. Examples of these include:

* For Ruby (e.g. for Sinatra, Ruby on Rails):  [pg](https://www.ruby-toolbox.com/projects/pg)
* For NodeJS:  [node-postgres](https://node-postgres.com/)
* For Python (e.g. for Flask, Django):  [pyscopg2](http://initd.org/psycopg/)

## Lesson 3: SQLAlchemy Basics

### Intro

SQLAlchemy is the most popular open source Python library for relational databases. It’s an Object-Relational Mapping (
ORM) library, which provides an OOP interface for database interactions.

#### OOP Syntax

A `CREATE TABLE` statement like the following:

```
CREATE TABLE todos (
	id INTEGER PRIMARY KEY,
	description VARCHAR NOT NULL,
	completed BOOLEAN NOT NULL DEFAULT FALSE
);
```

can be written in SQLAlchemy like this:

```
# Our todo table inherits from SQLAlchemy's db model
class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)
```

A query like this:

```
SELECT * FROM todos
```

becomes this, which has the additional benefit of being dialect-agnostic:

```
Todo.query.all()
```

#### Additional Benefits

* Features **function-based query construction**: allows SQL clauses to be built via Python functions and expressions.
* **Avoid writing raw SQL**. It generates SQL and Python code for you to access tables, which leads to less
  database-related overhead in terms of the volume of code you need to write overall to interact with your models.
* Moreover, you can **avoid sending SQL to the database on every call**. The SQLAlchemy ORM library features **automatic
  caching**, caching collections and references between objects once initially loaded.

#### ORMs in other languages

* [Sequelize](https://sequelize.org/)  and  [Bookshelf.js](https://bookshelfjs.org/)  for NodeJS
* [ActiveRecord](https://guides.rubyonrails.org/active_record_basics.html) , which is used
  inside  [Ruby on Rails](https://rubyonrails.org/)
* [CakePHP](https://book.cakephp.org/3/en/orm.html)  for PHP.

### Layers of Abstraction

DBAPIs are simple but not scalable or conducive to complexity. SQLAlchemy offers several layers of abstraction and
tooling for more convenient DB interactions:

![Layers of abstraction](../assets/layers_of_abstraction.png)

The lowest level offers a DBAPI, but SQLAlchemy is simply a SQL generator. SQLAlchemy depends on `psycopg2` or other
DBAPIs to send statements to the database. At the other end is the ORM, which allows Pythonic dialect-agnostic
interactions.

### The Dialect

The Dialect layer abstracts dialects away from the developer. It allows us to switch out seamlessly between them.
[SQLAlchemy Docs on the Dialect](https://docs.sqlalchemy.org/en/latest/dialects/)

### The Connection Pool

This abstracts the need to open, close, and manage connections to DBs. Connections are easily reused after they are
started. This reduces dropped connections and helps avoid making many small changes.
[SQLAlchemy Docs on its Connection Pooling](https://docs.sqlalchemy.org/en/latest/core/pooling.html)

### The Engine

The Engine is one of three main layers for how we interact with the database. It is the lowest layer of database
interaction and is similar to using `psycopg2` to manage a connection directly.

```
from sqlalchemy import create_engine

engine = create_engin("postgres://...")
conn = engine.connect()
result = conn.execute("SELECT * FROM vehicles;")

row = result.fetchone()
rows = result.fetchall()

result.close()
```

* The Engine in SQLAlchemy refers to both itself, the Dialect and the Connection Pool, which all work together to
  interface with our database.
* A connection pool gets automatically created when we create a SQLAlchemy engine.
  [SQLAlchemy Docs on the Engine](https://docs.sqlalchemy.org/en/latest/core/engines.html) .

### SQL Expressions

Instead of sending raw SQL using the Engine, we can build Python objects:

```
# Instantiate a table
todos = Table("todos", ...)

# Insert values
ins = todos.insert().values(
	description="Clean my room",
	completed=False
)

# Select rows
s = select([todos])

conn = engine.connect()
result = conn.execute(ins)
result = conn.execute(s)

result.close()

todos.c.description
	-> <Column 'description' in 'todos' table>
```

### SQLAlchemy ORM

The ORM is the highest level of abstraction. The ORM lets us compose SQL expressions by building Python objects which
map to tables in the database.

SQLAlchemy is split into two libraries:

* SQLAlchemy Core
* SQLAlchemy ORM: offered as an optional library
    * ORM uses the Core library inside
    * Lets us map from the database schema to the application’s objects
      ![Layers of Abstraction Diagram](./assets/layers_of_abstraction_overview.png)

### Mapping Between Tables and Classes

In Python we instantiate a class like this:

```
class Human:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
```

and create objects as instances of that class like this:

```
sarah = Human("Sarah", "Silverman", 48)
bob = Human("Bob", "Saget", 54)
```

In SQL we may create a similar table like this:

```
CREATE TABLE human (
	id INTEGER PRIMARY KEY,
	first_name VARCHAR,
	last_name VARCHAR,
	age INTEGER
);
```

Note the similarities:

* A column matches to a class attribute
* The table schema maps to the class definition
* Table rows map to instances of the class

### Hello App with Flask-SQLAlchemy - Part 1

* [Flask Docs](https://flask.palletsprojects.com/)  under “Quickstart”
* [Flask-SQLAlchemy Docs](http://flask-sqlalchemy.palletsprojects.com/)  under “Quickstart”
* [Primer on decorators from Real Python](https://realpython.com/primer-on-python-decorators/#decorators-with-arguments)
  . Application [here](./app.py)

### Connecting to the Database

A SQLAlchemy URI looks like this:
![URI parts](../assets/database_uri_parts.png)

To add a SQLAlchemy connection to our Flask app, we need to do the following:

```
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udacitystudios@localhost:5432/example'
db = SQLAlchemy(app)
```

### `db.Model` and Defining Models

Given an instance of the SQLAlchemy class from Flask-SQLAlchemy,

```
db = SQLAlchemy(app)
```

* `db` is an interface for interacting with our database
* `db.Model` lets us create and manipulate **data models**
* `db.session` lets us create and manipulate **database transactions**

### Syncing Models, `db.create_all()`

`db.create_all()` detects models and creates tables for them (if they don’t exist). SQLAlchemy will auto increment an
integer column set as the primary key.

### Inserting Records, Using Debug Mode

We’ll finish off creating a Hello App that says hello to our name by inserting a record into the persons table in our
database, and showing the person’s name on the index route.

```
postgres@localhost:mydb> INSERT INTO persons (name) VALUES ('Fitzy');
INSERT 0 1
Time: 0.019s
postgres@localhost:mydb> select * from persons
+------+--------+
| id   | name   |
|------+--------|
| 1    | Fitzy  |
+------+--------+
```

Exercise [here](./flask-hello-app.py)

### Experimenting in Interactive Mode

```
We can insert new records into the database using SQLAlchemy by running
person = Person(name=‘Amy’)
db.session.add(person)
db.session.commit()
```

### SQLAlchemy Data Types

![Data types](https://video.udacity-data.com/topher/2019/August/5d5a43a0_screen-shot-2019-08-18-at-11.36.57-pm/screen-shot-2019-08-18-at-11.36.57-pm.png)
SQLAlchemy data types. Source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

Flask-SQLAlchemy data types generally map to SQLAlchemy’s library of data types.

Check out the SQLAlchemy docs on Column and Data Types to learn more.

#### Resources

* [Flask-SQLAlchemy: Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)
* [Getting Started with PostgreSQL Data Types](http://www.postgresqltutorial.com/postgresql-data-types/)

### SQLAlchemy Constraints

* Column constraints ensure data integrity across our database, allowing for database accuracy and consistency.
* Constraints are conditions on your column, that provide checks on the data’s validity. It does not allow data that
  violates constraints to be inserted into the database (it will raise an error if you attempt to).
* In SQLAlchemy, constraints are set in `db.Column()` after setting the data type.
    * `nullable=False` is equivalent to `NOT NULL` in SQL
    * `unique=True` is equivalent to `UNIQUE` in SQL Example

```
class User(db.Model):
  …
  name = db.Column(db.String(), nullable=False, unique=True)
```

* [SQLAlchemy Constraints Docs](https://docs.sqlalchemy.org/en/latest/core/constraints.html) . Constraints available in
  SQLAlchemy are (generally) available in Flask-SQLAlchemy, and exposed by db.<sqlalchemy_method_or_interface>.

### Additional Resources on SQLAlchemy

* Bookmark
  this:  [SQLAlchemy Cheat Sheet](https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-sqlalchemy.rst#set-a-database-url)
* [Using PostgreSQL through SQLAlchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)

## SQLAlchemy ORM in Depth

We can import the db object and Person class to introspect the table in Python

```
Python 3.9.5 (default, May 12 2021, 15:26:36)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.24.1 -- An enhanced Interactive Python. Type '?' for help.

>>> # Import db and Person
>>> from flask_hello_app import db, Person

>>> # Select all persons and show the first ten
>>>  Person.query.all()[0:10]
[<Person ID: 1, name: Scott>,
 <Person ID: 2, name: Max>,
 <Person ID: 3, name: Alyssa>,
 <Person ID: 4, name: Twig>,
 <Person ID: 24, name: Gina>,
 <Person ID: 25, name: Michelle>,
 <Person ID: 26, name: Melissa>,
 <Person ID: 27, name: Jamie>,
 <Person ID: 28, name: Andrea>,
 <Person ID: 29, name: Allison>]

>>> # Find a specific person
>>> Person.query.filter_by(name="Max").all()
[<Person ID: 2, name: Max>]

>>> # Add a new person
>>> person = Person(name="Maximillian")
>>> db.session.add(person)
>>> db.session.commit()

>>> # Show our new person
>>> Person.query.all()[-1]
<Person ID: 64, name: Maximillian
```

### `Model.query`

The query object exists on a given model defined by us. It is the source of all select statements generated by the ORM.
Here are the most common methods:

```
# Select * from persons where name = 'Amy'
Person.query.filter_by(name="Amy")

# Select * from persons
Person.query.all()

# Select count(*) from persons
Person.query.count()

# More flexible filtering
Person.query(Person.name == "Amy", Team.name == "Udacity"

# Get person by primary key
Person.query.get(1)

```

Query enables easy bulk operations as well:

```
Product.query.filter_by(category="Misc").delete()
```

Finally, query provides method chaining:

```
Person.query \
	.filter(Person.name == "Amy") \
	.filter(Team.name == "Udacity") \
	.first()

Driver.query \
	.join("vehicles") \
	.filter_by(driver_id=3) \
	.all()
```

There are two ways to access the query object:

```
Person.query
is the same as
db.session.query(Person)
```

The latter is model-agnostic and useful for joins:

```
session.query(Person).join(Team)
```

#### Review and other useful methods:

```
# All records
MyModel.query.all()

# The first record
MyModel.query.first()

# All records with my_table_attribute of 'some value'
MyModel.query.filter_by(my_table_attribute='some value')
MyModel.query.filter(MyOtherModel.some_attr='some value')

# All orders with Product id of 3
OrderItem.query.filter(Product.id=3)

# Order by
MyModel.order_by(MyModel.created_at)
MyModel.order_by(db.desc(MyModel.created_at))

# Limit
Order.query.limit(100).all()

# Aggregates
query = Task.query.filter(completed=True)
query.count()

# Get object by id
model_id = 3
MyModel.query.get(model_id)

# Bulk deletes
query = Task.query.filter_by(category='Archived')
query.delete()

# Join
Driver.query.join('vehicles')
```

[SQLAlchemy Query Cheatsheet](https://video.udacity-data.com/topher/2019/August/5d5a52af_query-cheat-sheet/query-cheat-sheet.pdf)

* [SQLAlchemy Query API Documentation](https://docs.sqlalchemy.org/en/latest/orm/query.html)

### SQLAlchemy Object Lifecycle — Part 1

We can insert new records like

```
person = Person(name="Amy")
db.session.add(person)
db.session.commit()
```

This builds and commits a transaction. The changes won’t get committed until we run `db.session.commit()` We can
rollback an in-flight transaction by running `db.session.rollback()`.

#### Stages

1. Transient: an object is defined, but not attached to a session.
2. Pending: an object is attached to a session. We can rollback.
3. Flushed: almost ready for commit, this translates actions into SQL.
4. Committed: transaction is persisted and the transaction is cleared for subsequent changes.

### SQLAlchemy Object Lifecycle — Part 2

A flush takes pending changes and translates them into commit-ready commands. This occurs when we:

* call `Query`, or
* run `db.session.commit`

![Lifecycle diagram](../assets/object_lifecycle.png)

---
