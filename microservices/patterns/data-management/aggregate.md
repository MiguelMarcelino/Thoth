# Aggregate
A graph of objects that can be treated as a unit
* One of its component objects will be the aggregate root
	* Any references from outside the aggregate should only go to the aggregate root (root ensures integrity of the aggregate)
* DDD aggregates are the basic element of transfer of data storage
	* Transactions should not cross aggregate boundaries.
* DDD aggregates are domain concepts

<hr>

## Sources
* https://microservices.io/patterns/data/aggregate.html
* https://www.martinfowler.com/bliki/DDD_Aggregate.html


<hr>

Related to: [data-management](data-management.md), [domain-driven-design](domain-driven-design)
