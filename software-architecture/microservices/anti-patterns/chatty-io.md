# Chatty I/O Antipattern
* Network calls and other I/O operations are inherently slow compared to compute tasks.
* The cumulative effect of a large number of I/O requests can have a significant impact on performance and responsiveness.
* The key idea is to reduce the number of I/O requests by packaging the data into larger, fewer requests.
	* For instance, consider a `User` entity. Instead of separate `GET` methods for each property, there is a single `GET` method that returns the `User`, resulting in fewer API calls.

Considerations:
* By reducing the amount of API calls, we are also retrieves more information per request. Therefore, the correct API design is dependent on the usage pattern.
* Ensure that I/O requests are not too large 
* Partition the information for an object into two chunks, frequently accessed data that accounts for most requests, and less frequently accessed data that is used rarely.
* When writing data, avoid locking resources for longer than necessary, to reduce the chances of contention during a lengthy operation.

<hr>

## Sources
* https://learn.microsoft.com/en-us/azure/architecture/antipatterns/chatty-io/


<hr>

Related to: [anti-patterns](anti-patterns),