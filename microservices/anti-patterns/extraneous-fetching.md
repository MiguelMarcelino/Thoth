# Extraneous Fetching

* More than needed data is retrieved for a business operation, often resulting in unnecessary I/O overhead and reduced responsiveness.
* This antipattern can occur if the application tries to minimize I/O requests by retrieving all of the data that it might need. --> It is literally the opposite of [Chatty I/O](chatty-io)
* Application users might only require a subset of the data that is being sent

Considerations:
* Paginate the results (e.g. showing 20 at a time).
* Horizontal partitioning can improve performance. If different operations access different attributes of the data, horizontal partitioning may reduce contention. 
* When possible, take advantage of features built into the data store. For example, SQL databases typically provide aggregate functions.

<hr>

## Sources
* https://learn.microsoft.com/en-us/azure/architecture/antipatterns/extraneous-fetching/

<hr>

Related to: [anti-patterns](anti-patterns),
