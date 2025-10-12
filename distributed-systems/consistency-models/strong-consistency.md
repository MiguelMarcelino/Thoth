# Strong Consistency

Strong consistency (also called linearizability) is a consistency model in distributed systems where all operations appear to execute atomically and instantaneously at some point between their invocation and completion. All nodes always see the same order of operations, ensuring a single, globally consistent view of data.

## Purpose
The goal is to make the system behave as if there is one single copy of the data, even though it may be replicated across multiple nodes. This simplifies reasoning about system behavior.

## Key Idea

* Every read sees the most recent write.
* Updates are immediately visible to all processes.
* Operations appear in a total order consistent across all replicas.

## Example
If process A writes value 10 to a variable and process B reads it afterward, B must see 10. Any subsequent read by another process will also see 10 or a newer value.

## Trade-offs

* Strong consistency usually requires coordination between nodes (e.g., locking, consensus), which can reduce availability and increase latency.
* It is often difficult to maintain in large, geo-distributed systems.

<hr>

## Sources
- N/A

<hr>

Related to: [consistency-models](consistency-models.md)
