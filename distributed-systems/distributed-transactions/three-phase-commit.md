### Three-Phase Commit (3PC)

## Definition
Three-Phase Commit is an extension of 2PC that adds an extra phase to reduce the likelihood of blocking during failures.

## Purpose
To provide a non-blocking atomic commit protocol for distributed transactions in the presence of failures.

## Mechanism

1. **CanCommit Phase (Prepare)**: Coordinator asks participants if they can commit.
2. **PreCommit Phase**: Coordinator informs participants to prepare for commit; participants acknowledge.
3. **DoCommit Phase**: Coordinator instructs participants to commit.

## Advantages

* Reduces the chance of indefinite blocking compared to 2PC.
* Handles coordinator failures more gracefully.

## Disadvantages

* More complex than 2PC.
* Slightly slower due to the additional phase and messages.

<hr>

## Sources
- N/A

<hr>

Related to: [distributed-transactions](distributed-transactions.md)