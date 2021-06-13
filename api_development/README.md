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

```
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
| ------ | -------- |
| `1xx` |  Informational |
| `2xx` |  Success |
| `3xx` |  Redirection |
| `4xx` |  Client Error |
| `5xx` |  Server Error |

These are among the most common:

| Code | Definition |
| ---- | -----------|
| `200` |  OK |
| `201` |  Created |
| `304` |  Not Modified |
| `400` |  Bad Request |
| `401` |  Unauthorized|
| `404` |  Not Found |
| `405` |  Method Not Allowed |
| `500` |  Internal Server Error|

[HTTP Status Dogs](https://httpstatusdogs.com/)
[MDN Web Docs - HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
