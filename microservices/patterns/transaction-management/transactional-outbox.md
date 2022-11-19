#microservices/anti-patterns/transactional-outbox

# Transactional Outbox
Deals with the problem of reliably/atomically updating the database and send messages/events.
A service must atomically update the database and send messages in order to avoid data inconsistencies and bugs. That is, if we have, `T1 -> E1`, `T2 -> E2`, then since `T1` precedes `T2`, event `E1` must be published before `E2`.
The problem is that there’s no guarantee that the transaction will commit without 2PC.

**Solution:**
* A service that uses a relational database inserts messages/events into an outbox table as part of the local transaction. 
* A service that uses a NoSQL database appends the messages/events to attribute of the record (e.g. document or item) being updated. 
* A separate Message Relay process publishes the events inserted into database to a message broker.

<div align="center">
	<img src="https://microservices.io/i/patterns/data/ReliablePublication.png">
</div>

<hr>

## Sources