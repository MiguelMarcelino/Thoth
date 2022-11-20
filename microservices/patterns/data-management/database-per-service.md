# Database per service
* Each Microservice should have its own database
	* As microservices are independently deployable, this is crucial to ensure that there are no dependencies to other services
* Loose coupling allows for finer-grained control over scalability

Disadvantages
* Extra Complexity when joining data from queries that span multiple services
* Complexity of managing multiple SQL and NoSQL databases

<hr>

## Sources
* https://microservices.io/patterns/data/database-per-service.html


<hr>

Related to: [data-management](data-management.md)
