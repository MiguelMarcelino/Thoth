# Logical Clocks

Logical clocks are a mechanism used in distributed systems to order events without relying on physical time. They provide a way to determine the sequence of events based on causality rather than real-world timestamps.

## Purpose

In a distributed system, there is no global clock, and different machines may have unsynchronized physical clocks. Logical clocks help establish a consistent ordering of events to reason about causality, such as determining whether one event happened before another.

## Key Idea

The logical clock assigns a numerical timestamp to each event. These timestamps increase in a way that respects the "happens-before" relationship between events. If event A causally affects event B, then the logical timestamp of A is less than that of B.

## Lamport Clocks

One common type of logical clock is the Lamport clock, which works as follows:

1. Each process maintains a local counter.
2. The counter is incremented for every local event.
3. When a message is sent, it carries the sender’s counter value.
4. Upon receiving a message, the receiver sets its counter to be greater than both its current value and the received timestamp.

### Limitation

Lamport clocks can establish a partial order of events (causal relationships) but cannot distinguish between concurrent events. To handle that, more advanced mechanisms like vector clocks are used.


<hr>

## Sources
- N/A

<hr>

Related to: [time-and-ordering](time-and-ordering.md)