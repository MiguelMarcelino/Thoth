# Microservice Architecture
Architecture that structures the application as a set of loosely coupled, collaborating services. This approach corresponds to the Y-axis of the [scale-cube](scale-cube.md). Each service is:
* Highly maintainable and testable
	* Rapid and frequent development and deployment
* Loosely coupled with other services
	* Teams work independently
	* Teams are not impacted by changes to other services and don't affect other services
* Independently deployable
	* Deploy their service without having to coordinate with other teams
* Capable of being developed by a small team
	* high productivity 
	* Avoids high cocmmunication head of large teams


## Key Characteristics of Microservices

| Concept               | Description                                                  | Example                                                 |
| ------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------- |
| Independence          | Each microservice can be built, tested, and deployed separately. | Update “Payment Service” without redeploying the whole app. |
| Single Responsibility | Each service should do one thing well.                           | “User Service” only handles user data.                      |
| Decentralized Data    | Each service has its own database or data source (no shared DB). | MySQL for Orders, MongoDB for Users.                        |
| Communication         | Services talk over APIs or messaging.                            | REST, gRPC, RabbitMQ, Kafka.                                |
| Resilience            | System should survive when one service fails.                    | Circuit breakers, retries.                                  |
| Scalability           | You can scale individual services as needed.                     | Scale “Search Service” if it gets heavy traffic.            |



<hr>

## Sources
* https://microservices.io/patterns/microservices.html


