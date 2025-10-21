# Paxos

Paxos is a family of consensus algorithms designed to achieve agreement among a group of unreliable or distributed nodes. Its goal is to ensure that all nodes in a distributed system agree on a single value (such as a log entry, configuration change, or transaction) even if some nodes fail or network delays occur.

It assumes a model where:

* Nodes can fail or recover at any time.
* Messages can be delayed, duplicated, or arrive out of order, but are not corrupted.
* A majority of nodes are functioning correctly.

Paxos operates through three main roles:

1. Proposers: Suggest a value to be agreed upon.
2. Acceptors: Vote on proposals; consensus is reached when a majority of acceptors agree on a value.
3. Learners: Receive and record the chosen value once consensus is achieved.

The algorithm has two key phases:

1. Prepare phase – A proposer asks acceptors to promise not to accept proposals older than a certain number.
2. Accept phase – Once promises are received, the proposer sends an accept request with the proposed value; if a majority accept, the value is chosen.

Paxos guarantees safety (no two nodes ever decide on different values) but may sacrifice liveness (progress) under certain timing or leadership conditions.
For practical use, systems like Google Chubby and etcd often use Multi-Paxos or Raft, which build on Paxos to support replicated logs and leader election in a simpler, more efficient way.

<hr>

Related to: [coordination](coordination.md)