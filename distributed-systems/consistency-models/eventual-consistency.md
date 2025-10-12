# Eventual Consistency

Eventual consistency is a weak consistency model used in distributed systems. It guarantees that, if no new updates are made to a replicated data item, all replicas will eventually converge to the same value.

In other words, updates may not be immediately visible to all nodes, but given enough time and no further changes, every replica in the system will become consistent.

## Key characteristics:

* Updates propagate asynchronously across replicas.
* Temporary inconsistencies are allowed.
* The system ensures convergence once communication is stable and all updates have been delivered.

## Example:
In a distributed database, if a user updates their profile on one server, other servers might not see the change immediately. However, after the system synchronizes, all servers will show the same, updated profile.

Eventual consistency trades immediate consistency for higher availability and partition tolerance, following the principles of the CAP theorem.


<hr>

## Sources

<hr>

Related to: [consistency-models](consistency-models.md)
