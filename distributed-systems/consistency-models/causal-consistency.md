# Causal Consistency

Causal Consistency is a consistency model used in distributed systems that ensures operations that are causally related are seen by all processes in the same order, while operations that are independent (concurrent) may be seen in different orders.


## Formal Definition

A system is causally consistent if:

> Whenever one operation could have influenced another (i.e., there is a *cause–effect* relationship), every node in the system observes those operations in that causal order.


## Key Points

* Causality is determined by three rules:

  1. If operation A happens before operation B on the same process, then A → B.
  2. If operation A sends a message that operation B receives, then A → B.
  3. The “happens-before” relation is transitive (if A → B and B → C, then A → C).

* Independent (concurrent) operations — those without a causal link—can be seen in different orders by different replicas.

## Example

1. User A posts a message.
2. User B comments on that message.
3. All users must see A’s post before B’s comment (causal relationship).

But unrelated posts or comments can appear in any order.


<hr>

## Sources

<hr>

Related to: [consistency-models](consistency-models.md)
