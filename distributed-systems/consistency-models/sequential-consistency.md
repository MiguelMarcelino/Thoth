# Sequential Consistency

Sequential consistency is a consistency model in distributed systems where the result of execution is the same as if operations were executed in some sequential order, and the operations of each individual process appear in that order in program order.

## Purpose
It provides a relaxed form of strong consistency, allowing nodes to see operations in a consistent order without requiring instantaneous updates.

## Key Idea

* Operations appear in a total order that is consistent with the order in which each process issued them.
* Unlike strong consistency, sequential consistency does not guarantee that this order reflects real-time ordering.

## Example
If process A writes 10, then 20 to a variable, and process B reads it, B may see 10 then 20 or just 20 if reads are concurrent, but all processes will agree on a single sequential order of writes.

## Trade-offs

* Easier to implement than strong consistency.
* Can have temporary anomalies due to message delays.
* Still maintains a predictable program-order view for each process.


<hr>

## Sources

<hr>

Related to: [consistency-models](consistency-models.md)
