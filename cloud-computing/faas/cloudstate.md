# Cloudstate
* Allows developers to focus on business logic, data model, and workflows, instead of implementation details
* It manages:
	* Distributed and concurrent systems
	* Distributed state: Consistency, Replication, and Persistance
	* Message routing, Scalability, Fail-over, and Recovery

## Some terminologies
* Polyglot: Client libs (in JavaScript, Java, and Go)
* PolyState: Powerful state models (Event sourcing, Key-values)
* PolyDB: Support for Databases and in-memory replications


## Architecture

![[cloudstate-architecture.png]]


## Communication

![[cloudstate_communication.png]]

## Akka cluster state management
+ Actor based distributed runtime
+ Decentralized masterless P2P
+ Epidemic gossip, self healing
+ State sharding and routing on Entity key
+ Forwarding of requests
+ Colocation of state and processing
+ Backed by and event log
	+ This allows things to be replayed in the case of failures
+ Automatic Failover, Rehydration and Rebalancing
+ Highly scalable

## Benefits of Event sourcing
+ One single source of truth with all history
+ Durable in-memory state
+ Avoids object relational mismatch
+ Allows entities to subscribe to state changes
+ Follows single writer principle

## Conflict-free Replicated Data Types (CRDTs)
* Strong eventual consistency
* Replicated and Decentralised
* Highly available and scalable
* Data types contain resolution logic
* Always converge correctly

CRDTs properties
+ Associative (Batch insensitive; grouping does not matter) -> a+(b+c)=(a+b)+c
+ Commutative (Order insensitive) -> a+b=b+a
+ Idempotent (Retransmission insensitive) -> a+a=a

---
## Sources
* https://speakerdeck.com/jboner/cloudstate-towards-stateful-serverless?slide=9


<hr>

Related to: [stateful-serverless](stateful-serverless)
