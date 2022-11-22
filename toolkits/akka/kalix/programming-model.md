# Programming Model
## Kalix service
* Code that implements functionality
	* Packaged and run on Kalix
* Components:
	* Entities: Domain object that encapsulate data and business logic. 
		* Atttributes: 
			* State model: Determines how Kalix stores data.
			* Key: unique identifier that Kalix uses to send your service the right instance at the right time.
			* Data field(s): Data related to an entity.
			* Operation(s): Commands called by clients that change an entity's state. (Implemented by Kalix users)
	* Actions: Each action contains logic and does not persist state
	* Views: Allow one to retrieve data from multiple entities using SQL-like queries.

Services can only be invoked by messages. Services can receive those messages over gRPC, over HTTP, or by subscribing to topics.

## Managing State
* Every service in Kalix has a proxy, which acts as an in-memory data store (cache-like), and is backed by durable storage.
* Kalix automatically handles data access, transactional concerns, and scalability.
* Kalix handles state, avoids contention for resources, and supports scaling and failover.

Kalix state management overview:

<div align="center">
	<img src="https://docs.kalix.io/concepts/_images/runtime-interaction.svg" style="height: 150pt;">
</div>


→ The developer just has to implement the Entities, Actions, and Views.

<hr>

## Sources
* https://docs.kalix.io/concepts/programming-model.html

<hr>

Related to: [kalix](kalix.md)