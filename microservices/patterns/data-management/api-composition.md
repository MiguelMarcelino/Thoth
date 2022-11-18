# API Composition

<div align="center">
	<img src="https://microservices.io/i/data/ApiBasedQueryBigPicture.png">
</div>

* Deals with the problem of how to implement queries in a Microservice. 
* Implement a query by defining an API Composer, which invokes the services that owns the data and performs an in-memory join of the results.
* This is usually done by an API Gateway

## Assumptions
* The [Database per service](database-per-service.md) pattern is in use.


<hr>

## Sources
* https://microservices.io/patterns/data/api-composition.html