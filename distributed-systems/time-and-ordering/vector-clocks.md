# Vector Clocks

Vector clocks are a mechanism used in distributed systems to capture the causal relationships between events with greater precision than simple logical (Lamport) clocks. They allow the system to determine not only whether one event happened before another but also whether two events are concurrent.

## Purpose

The main goal of vector clocks is to provide a way to reason about causality among events occurring in different processes of a distributed system. They help detect concurrent updates and maintain causal ordering, which is essential for ensuring consistency and conflict resolution in replicated data systems.

## Key Idea

Each process in the system maintains a vector of logical counters, one for every process in the system. These counters collectively represent the knowledge a process has about the progress of all other processes.

## Mechanism

1. Every process starts with a vector initialized to zeros.
2. When a process performs a local event, it increments its own counter in the vector.
3. When a process sends a message, it attaches its current vector clock to the message.
4. Upon receiving a message, the receiver updates each element of its vector to be the maximum of its current value and the received vector’s corresponding value, then increments its own counter.

## Comparing Vector Clocks

Given two vector clocks, V1 and V2:

* V1 < V2 if every element of V1 is less than or equal to the corresponding element of V2, and at least one is strictly less. This means the event associated with V1 happened before V2.
* V1 and V2 are concurrent if neither V1 < V2 nor V2 < V1 holds.

## Limitation

Vector clocks require each process to maintain a vector whose size equals the number of processes in the system. This can become inefficient in systems with a very large number of nodes.

<hr>

## Sources

<hr>

Related to: [time-and-ordering](time-and-ordering.md)
