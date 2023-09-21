# Stateful Serverless

## Good uses for Faas
* Systems that require parallel processing and are invoked on demand
* Spiky workloads and low-traffic applications
* Stateless web applications
* Orchestration functions (coordination of calls to third party services)
* Composing chains of functions

## Disadvantages of Faas
* With Faas, functions don't keep state -> It is typically expensive to loose computational context
* State has to be kept in persistent storage -> one more layer to take care of
	* No direct addressability (requires external storage)
	* No co-location of state and processing
* Limitation to distributed state coordination and modelling data consistency guarantees

Faas does not offer support for managing in-memory durable session state across requests (e.g. a user session).
It would be beneficial that it could offer distributed, resilient transaction flows (e.g saga pattern)

## Technical requirements
* Stateful long-lived addressable virtual components (e.g. actors)
* Options for distributed communication and coordination across the virtual components (e.g. pub-sub, broadcasting, etc)
* Consistency mechanisms (e.g. eventual consistency)
* Physical colocation of state and processing
* Predictable performance, latency and throughput
* Ways to manage end-to-end guarantees

The problem with Faas is that functions are black boxes, which makes it hard to automate operations

While Faas deals with abstracting over communication, Stateless serverless deals with abstracting over state.


---
## Sources
* https://speakerdeck.com/jboner/cloudstate-towards-stateful-serverless?slide=9


<hr>

Related to: [faas](faas)