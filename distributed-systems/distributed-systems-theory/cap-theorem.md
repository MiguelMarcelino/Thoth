# CAP Theorem
The CAP theorem states that a distributed system can only guarantee two of the following three properties at the same time:

* Consistency (C): Every read receives the most recent write (no stale data).
* Availability (A): Every request receives a (non-error) response, even if some nodes are down.
* Partition Tolerance (P): The system continues to operate even if there are communication failures between nodes.

## 2. Core Idea

In a distributed system, network partitions are inevitable - so you must decide whether to:

* Prioritize Consistency (block requests during a partition), or
* Prioritize Availability (serve possibly stale data).

You can’t fully have all three at once.


## 3. Examples

| Type                                        | Focus                                                   | Example                             |
| ------------------------------------------- | ------------------------------------------------------- | ----------------------------------- |
| CP (Consistency + Partition tolerance)  | Always consistent, may reject requests if partitioned   | HBase, Zookeeper, Etcd              |
| AP (Availability + Partition tolerance) | Always responds, even if data is stale                  | Cassandra, DynamoDB                 |
| CA (Consistency + Availability)         | Only possible in single-node or fully reliable networks | Traditional RDBMS (non-distributed) |


<hr>

Related to: [distributed-systems-theory](distributed-systems-theory.md)