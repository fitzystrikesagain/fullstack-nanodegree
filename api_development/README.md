# API Development and Documentation
## Course overview
In this course we’ll learn about:
* APIs - what they are and how they work. We’ll gain insights into Internet protocols and the RESTful philosophy
* Handling HTTP Requests - writing and accessing endpoints in Flask
* Routing and API Endpoints - we’ll use endpoints and payloads to extend API functionality. We’ll learn to organize endpoints, handle CORS requests, parse different request types, and handle errors.
* Documentation - We’ll write docs to enable others to use the API or contribute to the project
* Testing - We’ll learn and use TDD to ensure each function is working and handling errors. We’ll write tests even before defining functions

### Tech Stack
* Flask
* Flask-CORS
* SQLAlchemy
* JSONify
* Unittest
## Introduction to APIs
In the first section we’ll be covering the foundations:
* What are APIs?
* Benefits of APIs
* IP Communications
* RESTful APIs

### What are APIs
An Application Programming Interface (API) is simply a thing that allows two different systems to interact with one another. API functionality differs from the application implementation of the provider, so understanding the application isn’t necessary to utilize the API. APIs:
* Don’t expose implementations to those that shouldn’t have access
* Provides a standard way of accessing the application
* Makes it easier to access the application’s data

Frequently used APIs include:
*  [Google Maps API](https://developers.google.com/maps/documentation/)
*  [Stripe API](https://stripe.com/docs/api?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier&utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier)
*  [Facebook API](https://developers.facebook.com/docs)
*  [Instagram API](https://www.instagram.com/developer/)
*  [Spotify API](https://developer.spotify.com/documentation/web-api/)

### How APIs Work
1. Client sends a request to the server
2. The API parses that request
3. If the request is formatted correctly, the server queries the database for the information or performs the action in the request
4. The server formats the response and sends it back to the client
5. The client renders the response according to its implementation

[Postman blog - What is an API?](https://blog.postman.com/intro-to-apis-what-is-an-api/)

### Internet Protocols
Hosts us IP to send data across the internet. There are many protocols:

* Transmission Control Protocol (TCP) which is used for data transmission
* Hypertext Transmission Protocol (HTTP) which is used for transmitting text and hyperlinks
* File Transfer Protocol (FTP) which is used to transfer files between server and client

### RESTful APIs

REST stands for Representational State Transfer. The philosophy of REST was devised by Roy Fielding in [his dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf) and boils down to a few key principles:
* **Uniform Interface**: Every architecture must have a standardized way of accessing and processing resources. This includes URIs and descriptive response messaging that describes how to process the representation of the resource
* **Stateless**: Every client request is self-contained. The server does not store or need application or state data to process subsequent requests. This makes the implementation more scalable.
* **Client-Server**: There must be both a client and server
* **Cacheable & Layered System**: Caching and layering improves network efficiency

*  [What exactly is RESTful programming?](https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)
* An article from StackOverflow blogs-  [Best practices for REST API design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

## HTTP and Flask Basics
### Overview
HTTP provides a standardized way for computers to communicate. It’s been the standard for internet communication since 1990.
### Introduction to HTTP
#### Features
* **Connectionless**: Client opens a connection when sending a request and closes the connection after the response is received
* **Stateless**: There is no dependency between successive requests
* **Not Sessionless**: Sessions can be created using headers and cookies
* **Media Independent**: HTTP supports the transmission of arbitrary data formats. Only the client and server need to know how to process the data.

#### Elements
* Universal Resource Identifiers (URIs) are broken down into the following components:
  * Scheme: the protocol being used, e.g., `http`
  * Host: the host that owns the resources, e.g. www.example.com
  * Path: the resource being requested, e.g., `tasks`
  * Query: optional component that provides information the resource can use, such as a search parameter, e.g., `term=homework`
#### Additional Resources for HTTP basics
*  [StackExchange: What is the difference between a URI and a URL?](https://webmasters.stackexchange.com/questions/19101/what-is-the-difference-between-a-uri-and-a-url)
*  [StackOverflow: What is the difference between a URI, a URL, and a URN?](https://stackoverflow.com/questions/176264/what-is-the-difference-between-a-uri-a-url-and-a-urn)
*  [RFC 3986: Uniform Resource Identifier](https://www.ietf.org/rfc/rfc3986.txt)
*  [MDN Web Docs - An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

### HTTP Requests
An HTTP request consists of the following elements:

```bash
GET http://www.example.com/tasks?term=homework
HTTP/2.0
Accept-Language: en
```
Here’s a breakdown of each element:
* Method -> `GET`
  * Defines the operation to be performed
* Path -> `http://www.example.com/tasks?term=homework`
  * The URL of the resource to be fetched, excluding the scheme and host
* HTTP Version -> `HTTP/2.0`
* Headers (Optional) -> `Accept-Language: en`
  * optional information, success as Accept-Language
* Body (Optional) -> None
  * optional information, usually for methods such as POST and PATCH, which contain the resource being sent to the server

#### HTTP Methods

| Method  | Purpose |
| —————— | —————— |
| GET  | Retrieve information for a specific resource  |
| POST  | Send data to create a new resource |
| PUT  | Update *all* of a resource with the request data  |
| PATCH  | Update *some* of a resource with the data provided   |
| DELETE  | Remove a representation of a resource  |
| Content Cell  | Send the communication options for the requested resource  |

#### Additional reading for HTTP evolution
[MDN Web Docs - Evolution of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP)

### HTTP Responses
After the server processes the client’s request, it returns an HTTP response message. This message consists of the following elements:
* Status code and status message: 200, 400, 401, etc.
* HTTP Version
* Headers: provides contextual information about the response and resource representation
  * Date
  * Content-Type: the media type of the request body
* Body: optional data containing the resource

#### Status codes
It’s important to understand and communicate status codes in order to root cause and resolve errors. Codes fall into one of these five categories:

| Prefix | Category |
| ——— | —————— |
| `1xx` |  Informational |
| `2xx` |  Success |
| `3xx` |  Redirection |
| `4xx` |  Client Error |
| `5xx` |  Server Error |

These are among the most common:

| Code | Definition |
| ——— | —————— |
| `200` |  OK |
| `201` |  Created |
| `304` |  Not Modified |
| `400` |  Bad Request |
| `401` |  Unauthorized, Authentication Required |
| `404` |  Not Found |
| `405` |  Method Not Allowed |
| `500` |  Internal Server Error|

[HTTP Status Dogs](https://httpstatusdogs.com/)
[MDN Web Docs - HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Intro to Flask
There’s a basic example in this directory, `getting_started`. The videos recommended defining the app in `__init__.py`, which weirded me out. This is, however, what Flask recommends, along with using their Blueprints for larger applications: [Large Applications as Packages — Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/patterns/packages/)

Directory structure:
```bash
.
├── .env
├── Dockerfile-backend
├── README.md
├── __init__.py
├── docker-compose.yml
├── flaskr
│   ├── __init__.py
└── requirements.txt
```

The app code is in `flaskr/__init__.py`, and the function simply returns the app, rather than running it. The `.env` file contains all the variables Flask needs:
```bash
FLASK_APP=flaskr
FLASK_ENV=development
```
The `FLASK_APP` variable provides Flask a context. The `FLASK_ENV` variable tells Flask to enable automatic reload and debug mode. Then in our `docker-compose.yml` we just tell Flask to run (including `0.0.0.0` as the host so we can reach it inside the container):
```yaml
services:
  flask:
    build:
      context: .
      dockerfile: Dockerfile-backend
    command: flask run -h "0.0.0.0"
    container_name: flask-api
    env_file:
      - .env
    image: python:3.9.5
    ports:
      - "5000:5000"
    restart: unless-stopped
    volumes:
      - ./:/usr/src/app/
```

[Flask official docs - Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

### Introduction to Curl and Dev Tools
#### Dev Tools
The Network tab shows a bunch of information about various interactions, including API request methods, status codes, and request and response bodies. The following columns (or similar ones) can be found in the Network tab:
* Status: HTTP status code
* Method: GET, POST, etc.
* Domain: This is the host, without the path, e.g. `www.youtube.com`
* File: resource name
* Initiator: a link to the line of code that triggered the request
* Type: data format (html, json, gif, plain, etc.)
* Transferred and Size: size of the resource and bytes transferred

Clicking into any of these requests will open a new tab with much more detailed information, including headers, request and response bodies, content types, and sometimes previews.

[Network Monitor - Firefox Developer Tools | MDN](https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor)
[Firefox Developer Tools | MDN](https://developer.mozilla.org/en-US/docs/Tools)

#### cURL
cURL is a command line utility used to programmatically interact with various servers, particularly APIs. An unqualified `curl` command will send a `GET` to the resource. Here’s an example against [the REST Countries API](https://restcountries.eu/):
```bash
$ curl https://restcountries.eu/rest/v2/currency/cop
[{"name":"Colombia","topLevelDomain":[".co"],"alpha2Code":"CO","alpha3Code":"COL","callingCodes":["57"],"capital":"Bogotá","altSpellings":["CO","Republic of Colombia","República de Colombia"],"region":"Americas","subregion":"South America","population":48759958,"latlng":[4.0,-72.0],"demonym":"Colombian","area":1141748.0,"gini":55.9,"timezones":["UTC-05:00"],"borders":["BRA","ECU","PAN","PER","VEN"],"nativeName":"Colombia","numericCode":"170","currencies":[{"code":"COP","name":"Colombian peso","symbol":"$"}],"languages":[{"iso639_1":"es","iso639_2":"spa","name":"Spanish","nativeName":"Español"}],"translations":{"de":"Kolumbien","es":"Colombia","fr":"Colombie","ja":"コロンビア","it":"Colombia","br":"Colômbia","pt":"Colômbia","nl":"Colombia","hr":"Kolumbija","fa":"کلمبیا"},"flag":"https://restcountries.eu/data/col.svg","regionalBlocs":[{"acronym":"PA","name":"Pacific Alliance","otherAcronyms":[],"otherNames":["Alianza del Pacífico"]},{"acronym":"USAN","name":"Union of South American Nations","otherAcronyms":["UNASUR","UNASUL","UZAN"],"otherNames":["Unión de Naciones Suramericanas","União de Nações Sul-Americanas","Unie van Zuid-Amerikaanse Naties","South American Union"]}],"cioc":"COL"}]
```
We can pipe this to `jq` to prettify it:
```bash
curl https://restcountries.eu/rest/v2/currency/cop | jq
[
  {
    "name": "Colombia",
    "topLevelDomain": [
      ".co"
    ],
    "alpha2Code": "CO",
    "alpha3Code": "COL",
    "callingCodes": [
      "57"
    ],
    "capital": "Bogotá",
    "altSpellings": [
      "CO",
      "Republic of Colombia",
      "República de Colombia"
    ],
...
```

Here’s an example `POST`. Note that the `-x` flag requires a method parameter:
```bash
curl -X POST http://www.example.com/tasks/
```

Other command line options include:

```bash
-X or --request COMMAND
-d or --data DATA
-F or --form CONTENT
-u or --user USER[:PASSWORD]
-H or --header LINE
```

[Art Of Scripting HTTP Requests Using Curl](https://curl.se/docs/httpscripting.html)

# Bookshelf application
## Local Development
The instructions below are meant for the local setup only. The classroom workspace is already set for your to start practicing.

#### Pre-requisites
* Developers using this project should already have Python3, pip and node installed on their local machines.


* **Start your virtual environment**
  From the backend folder run
```bash
# Mac users
python3 -m venv venv
source venv/bin/activate
# Windows users
> py -3 -m venv venv
> venv\Scripts\activate
```

* **Install dependencies**<br>
  From the backend folder run
```bash
# All required packages are included in the requirements file. 
pip3 install -r requirements.txt
# In addition, you will need to UNINSTALL the following:
pip3 uninstall flask-socketio -y
```


### Step 0: Start/Stop the PostgreSQL server
Mac users can follow the commands below:
```bash
which postgres
postgres --version
# Start/stop
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop 
```
Windows users can follow the commands below:
- Find the database directory, it should be something like that: *C:\Program Files\PostgreSQL\13.2\data*
- Then, in the command line, execute the folllowing command:
```bash
# Start the server
pg_ctl -D "C:\Program Files\PostgreSQL\13.2\data" start
# Stop the server
pg_ctl -D "C:\Program Files\PostgreSQL\13.2\data" stop
```
If it shows that the *port already occupied* error, run:
```bash
sudo su - 
ps -ef | grep postmaster | awk '{print $2}'
kill <PID> 
```

### Step 1 - Create and Populate the database
1. **Verify the database username**<br>
   Verify that the database user in the `/backend/books.psql`, `/backend/models.py`, and `/backend/test_flaskr.py` files must be either the `student` or `postgres` (default username). FYI, the classroom workspace uses the `student`/`student` user credentials, whereas, the local implementation can use the dafault `postgres` user without a password as well. (See the `/backend/setup.sql` for more details!)

2. **Create the database and a user**<br>
   In your terminal, navigate to the */nd0044-c2-API-Development-and-Documentation-exercises/1_Requests_Starter/backend/* directory, and run the following:
```bash
cd nd0044-c2-API-Development-and-Documentation-exercises/1_Requests_Starter/backend
# Connect to the PostgreSQL
psql postgres
#View all databases
\l
# Create the database, create a user - `student`, grant all privileges to the student
\i setup.sql
# Exit the PostgreSQL prompt
\q
```


3. **Create tables**<br>
   Once your database is created, you can create tables (`bookshelf`) and apply contraints
```bash
# Mac users
psql -f books.psql -U student -d bookshelf
# Linux users
su - postgres bash -c "psql bookshelf < /path/to/exercise/backend/books.psql"

```
**You can even drop the database and repopulate it, if needed, using the commands above.**


### Step 2: Complete the ToDos and Start the backend server
Navigate to the `/backend/flaskr/__init__.py` file, and finish all the `@TODO` thereby building out the necessary routes and logic to get the backend of your app up and running.

Once you've written your code, start your (backend) Flask server by running the command below from the `/backend/` directory.
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application will run on `http://127.0.0.1:5000/` by default and is set as a proxy in the frontend configuration. Also, the current version of the application does not require authentication or API keys.



### Step 3: Start the frontend
(You can start the frontend even before the backend is up!)
From the `frontend` folder, run the following commands to start the client:
```
npm install // only once to install dependencies
npm start 
```
By default, the frontend will run on `localhost:3000`. Close the terminal if you wish to stop the frontend server.

---

## Additional information
#### Running Tests
If any exercise needs testing, navigate to the `/backend` folder and run the following commands:
```bash
psql postgres
dropdb bookshelf_test
createdb bookshelf_test
\q
psql bookshelf_test < books.psql
python test_flaskr.py
```