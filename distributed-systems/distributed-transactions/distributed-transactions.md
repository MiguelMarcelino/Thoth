# Distributed Transactions

A distributed transaction is a transaction that spans multiple nodes or databases in a distributed system. It ensures that a set of operations across these nodes is executed atomically, so that either all operations succeed or none are applied, maintaining system consistency.

## Purpose
The goal is to maintain data integrity across multiple locations in a distributed system, even in the presence of failures or network issues. Distributed transactions are essential in systems where operations must be coordinated across multiple resources.

## Key Concepts (ACID)

* **Atomicity**: All parts of the transaction are applied, or none are.
* **Consistency**: The system moves from one valid state to another.
* **Isolation**: Concurrent transactions do not interfere with each other.
* **Durability**: Once committed, the results of a transaction are permanent, even after failures.

## Mechanisms

1. Two-Phase Commit (2PC)

   * Phase 1: **Prepare** – The coordinator asks all participating nodes if they can commit.
   * Phase 2: **Commit/Rollback** – If all nodes agree, the coordinator instructs them to commit; otherwise, it instructs a rollback.
   * Ensures atomicity but can block indefinitely if the coordinator fails.

2. Three-Phase Commit (3PC)

   * Adds an extra pre-commit phase to 2PC to reduce the chance of blocking.
   * Improves fault tolerance but is more complex and slower.

3. BASE Transactions (for NoSQL)

   * Basically Available, Soft state, Eventually consistent
   * Sacrifices strict ACID guarantees for higher availability and scalability.

## Challenges

* Network failures or node crashes during the transaction.
* Ensuring atomicity and isolation across multiple, possibly heterogeneous systems.
* Coordination overhead, which can impact performance.

## Example
A money transfer between two bank accounts in different databases:

* Debit account A in database X
* Credit account B in database Y

Both operations must succeed or neither should happen.

<hr>

## Sources
- N/A

<hr>

Related to: [distributed-systems](distributed-systems.md)