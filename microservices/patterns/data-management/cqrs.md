#microservices/patterns/data-management 

# Command Query Responsability Segregation (CQRS)
* Focuses on the problem of retrieving data from multiple services
* The solution is to define a read-only replica that is designed to support that query.
* The application is updated through domain events

We have the example below from [Microservices.io](https://microservices.io/patterns/data/cqrs.html):
<div align="center">
	<img src="https://microservices.io/i/patterns/data/QuerySideService.png" style="height: 250pt;">
</div>
In this case, there are several services that own the data. This data is published to another replica using Domain Events. An event Handler is responsible for receiving those events at the receiving replica. For the case demonstrated above, the replica then publishes these changes to the database.

<hr>

## Sources
* https://microservices.io/patterns/data/cqrs.html