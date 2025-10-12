# Two-Phase Commit (2PC)

## Definition
Two-Phase Commit is a protocol used to ensure atomicity of distributed transactions across multiple nodes. It coordinates all participants so that either all commit or all roll back.

## Purpose
To guarantee that a distributed transaction is applied atomically, even in the presence of failures, across multiple databases or nodes.

##  Mechanism

1. Phase 1 – Prepare:

   * Coordinator asks all participants if they are ready to commit.
   * Participants vote: "Yes" (can commit) or "No" (cannot commit).
2. Phase 2 – Commit/Rollback:

   * If all vote "Yes," coordinator instructs everyone to commit.
   * If any vote "No," coordinator instructs everyone to roll back.

## Advantages

* Guarantees atomicity.
* Simple to implement conceptually.

##  Disadvantages

* Can block indefinitely if the coordinator crashes during commit phase.
* Slower due to the two rounds of communication.

<hr>

## Sources
- N/A

<hr>

Related to: [distributed-transactions](distributed-transactions.md)