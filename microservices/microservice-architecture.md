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

## Patterns
* [API decomposition](api-composition.md)
* [CQRS](cqrs.md)
* [Event Sourcing](event-sourcing.md)
* [Gateway](api-gateway.md)
* [Saga](saga.md)
* [Transactional Outbox](transactional-outbox.md)

## Anti-patterns
* [Chaty I/O](chatty-io)
* [Extraneous Fetching](extraneous-fetching)
<hr>

## Sources
* https://microservices.io/patterns/microservices.html


