# BASE Transactions (NoSQL Approach)

## Definition
BASE is an approach used in distributed, highly-available databases that **relaxes strict ACID guarantees**. It stands for:

* **Basically Available** – The system remains operational even if some nodes fail.
* **Soft state** – The system state may change over time, even without new input.
* **Eventually consistent** – All nodes will converge to the same state eventually.

## Purpose
To provide high availability and scalability in distributed systems where strict consistency is not feasible or required.

## Mechanism

* Writes may be applied to some nodes and propagated asynchronously to others.
* Conflicts are resolved using techniques like version vectors, last-write-wins, or application-level reconciliation.

## Advantages

* Highly available and fault-tolerant.
* Scales well for large, geo-distributed systems.

## Disadvantages

* Sacrifices immediate consistency.
* Applications must handle temporary inconsistencies or conflicts.

## Example
Distributed key-value stores like Cassandra or DynamoDB use BASE principles to achieve eventual consistency across replicas.

<hr>

## Sources
- N/A

<hr>

Related to: [distributed-transactions](distributed-transactions.md)