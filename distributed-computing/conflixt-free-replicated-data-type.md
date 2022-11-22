# Conflict-free Replicated Data type (CRDT)
Data structure that is replicated across multiple computers in a network, with the following features:
* The application can update any replica independently, concurrently and without coordinating with other replicas.
* An algorithm (itself part of the data type) automatically resolves any inconsistencies that might occur.
* Although replicas may have different state at any particular point in time, they are guaranteed to eventually converge.

<hr>

## Sources
* https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type

<hr>

Related to: [distributed-computing](distributed-computing)
Tags: #info-review