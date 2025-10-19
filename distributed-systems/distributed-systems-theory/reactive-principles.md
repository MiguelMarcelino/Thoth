# Reactive Principles
Reactive Principles refer to a set of architectural guidelines that enable systems to be scalable, resilient, responsive, and elastic — even in the face of failure, variable load, and network unpredictability.

## Stay Responsive
* Always respond in a timely manner
* Ensures quality of service
	*  It does not matter that the system is correct if it cannot provide its functionality within their time constraints.
* Important aspects: low latency, fast response time, and managing changes (data, usage patterns, context, and environment).
	* Changes must become visible to the user
* In the worst-case, respond with an error message or provide a degraded but still useful level of service

## Accept Uncertainty
* Build reliability despite unreliable foundations
* There is no “now”. The present is relative and subjective, framed by the viewpoint of the observer.
	* inability to know what is happening on another node now (happens due to the lack of consistent and reliable shared memory)
* Order Methods: [Logical Clocks](logical-clocks.md) ([Vector Clocks](vector-clocks)), [Eventual Consistency](eventual-consistency.md)

## Embrace Failure
* Expect things to go wrong and design for resilience
* Principles:
	* Component autonomy: Ensures that the failure remains contained in as small an area of the application’s function as possible. 
	* Decoupling in space: Failure is contained inside a designated failure zone
	* Decoupling in time: Enables other components to reliably detect and handle failures even when they cannot be explicitly communicated.
* Reactive programming techniques associated:
	* `onError` in reactive streams
	* Throwing exceptions in observables 
	* Communicate occurrence but not nature of failure (encapsulate failure), just like in [actor model](actor-model.md)

## Assert Autonomy
* Design components that act independently and interact collaboratively
* Define the component boundaries
	* Who owns what data
	* How the owners make it available
* Protocols must be asynchronous and event-based

## Tailor Consistency
* Individualize consistency per component to balance availability and performance.
* Consistency guarantees the correctness and integrity of an application and user’s data.
* Convergence in distributed systems: the system is always in the process of convergence but never manages to fully “catch up” and reach a final state of convergence (on a global system scale). 
	* Define *units of consistency*: small islands of strong consistency
* Design systems for [eventual consistency](eventual-consistency.md) or [causal consistency](causal-consistency.md)

## Decouple Time
* Process asynchronously to avoid coordination and waiting
* Break the time availability dependency between remote components.

## Decouple Space
* Create flexibility by embracing the network
* Allow the system to live in multiple locations
* Use asynchronous message-passing
	* Makes the network explicit and first-class in the design
	* Forces you to design for failure and uncertainty

## Handle Dynamics
* Continuously adapt to varying demand and resources
* Reacting to changes in the input rate by increasing or decreasing the resources allocated to service these inputs
* Where resources are fixed, the scope of processed inputs needs to be adjusted
	* Being able to make such trade-offs at runtime requires the component to be autonomous
	* System must track relevant live usage metrics and continuously feed the data to predictive or reactive scaling algorithms (know how the application is coping)


<hr>

## Sources
* https://www.reactiveprinciples.org/principles/index.html

<hr>

Related to: [distributed-systems-theory](distributed-systems-theory.md)
Tags: #todo