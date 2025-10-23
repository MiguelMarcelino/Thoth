# REST APIs (Representational State Transfer)

A REST API is a set of conventions for building web services that allow systems to communicate using HTTP in a stateless way.
It’s the most common way microservices communicate.

## Core REST Concepts

| Concept              | Explanation                                                                | Example                                          |
| ------------------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Statelessness        | Each request contains all info needed; the server doesn’t store session state. | Client must send token on every request.             |
| Resources            | Everything is treated as a resource with a unique URL.                         | `/users`, `/orders`, `/products/123`                 |
| HTTP Methods         | Standard verbs for CRUD operations.                                            | GET, POST, PUT, DELETE, PATCH                        |
| Representations      | Data can be sent in JSON, XML, etc.                                            | Usually JSON today.                                  |
| HTTP Status Codes    | Indicate result of operations.                                                 | 200 OK, 201 Created, 404 Not Found, 500 Server Error |
| Versioning           | Maintain backward compatibility.                                               | `/api/v1/users`                                      |
| HATEOAS *(optional)* | Hypermedia links that guide clients.                                           | JSON responses that include next URLs.               |


## Example RESTful Endpoints

| Operation  | HTTP Method | Endpoint  | Meaning            |
| -------------- | --------------- | ------------- | ---------------------- |
| Read all users | GET             | `/users`      | Retrieve list of users |
| Read one user  | GET             | `/users/{id}` | Retrieve one user      |
| Create user    | POST            | `/users`      | Add new user           |
| Update user    | PUT             | `/users/{id}` | Replace user data      |
| Delete user    | DELETE          | `/users/{id}` | Remove a user          |



## REST + Microservices = Distributed System

In microservice architectures, REST APIs are often used for:

* Service-to-service communication
* Client-to-service communication (mobile/web apps)
* External integrations (third-party APIs)

However, as systems grow, REST sometimes gets replaced (or complemented) by:

* gRPC (binary, faster for internal communication)
* GraphQL (flexible querying)
* Async messaging (Kafka, RabbitMQ, etc.)

<hr>

Related to: [microservices](microservices)