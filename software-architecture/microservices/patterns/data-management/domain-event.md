# Domain Event
* A domain event should be used to propagate state changes across multiple aggregates within the same domain model.
* It is an event that happens withing a specific domain.
	* Other processes should know of this domain.
* Events should be raised from the domain operation one is currently running. Any side effects should occur within the same domain.
* Help express, explicitly, the domain rules, based in the ubiquitous language provided by the domain experts. 
* Enable a better separation of concerns among classes within the same domain.



<hr>

## Sources
* https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation

<hr>

Related to: [data-management](data-management.md), [domain-driven-design](domain-driven-design)
