# Event sourcing
* Persists the state of a business entity as a sequence of state-changing events.
* Whenever the state of a business entity changes, a new event is appended to the list of events. 
* Adding events is an atomic operation
* Events can be replayed to construct an entities current state
* Events are persisted in an event store

<div align="center">
	<img src="https://microservices.io/i/storingevents.png" style="width: 400pt;">
</div>

* The application persists each Order as a sequence of events.
* The CustomerService can subscribe to the order events and update its own state.

<hr>

## Sources
* https://microservices.io/patterns/data/event-sourcing.html

<hr>

Related to: [data-management](data-management)