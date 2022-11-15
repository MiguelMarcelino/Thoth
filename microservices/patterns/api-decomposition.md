# API Decomposition
* Deals with the problem of how to implement queries in a Microservice. 
* Implement a query by defining an API Composer, which invoking the services that own the data and performs an in-memory join of the results.
* This is usually done by an API Gateway

## Assumptions
* The [Database per service](database-per-service) pattern is in use.


<hr>

## Sources
* https://microservices.io/patterns/data/api-composition.html