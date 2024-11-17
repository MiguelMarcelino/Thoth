# Apache Pulsar

## Messaging vs Streaming
- Messaging
	- Message passing between different services, applications
	- Use Cases: Online Transaction, Integration
	- Main challenges: Latency, Availability, Data durability, High-level features (Routing, Dead-letter queues, delays)
- Streaming
	- Analyse events that happened
	- Use cases: Real-time analytics
	- Main challenges: Throughput, Ordering, Stateful processing, Batch + Real-time

## Pulsar
- Flexible Pub-Sub and Compute backend by durable log storage
- Durability: Data replicated and synched to disk
- Low latency: Low publish latency of 5ms at p99
- High Throughput: Up to 1.8M messages/s
- High Availability: System is available if any 2 nodes are up
- Cloud-Native: Take advantage of dynamic cluster scaling
- Unified Message model: Support both topic and queue semantics
- Highly Scalable: Supports millions of topics

## Messaging model

![[pulsar_messaging_model.png]]

There are multiple subscription models:
- Exclusive: Only one consumer is allowed to consume
- Failover: One active and multiple stand-by consumers, in case something happens to the active consumer
- Shared: Each consumer receives a portion of the messages. 
- Key_Shared: There are multiple consumers with ordering guarantees. The same message type will always go to the same consumer.

## Architecture

![[pulsar_architecture.png]]

- Components (It is a layered system):
	- Broker: Stateless service
		- Does not own the data for one topic
		- We can move them to different brokers.
	- Bookie: Storage node
		- They are IO bound.
- This layered architecture allows us to scale bookies independently from brokers

## Replicated Log storage
- Low-latency durable writes 
	- Writes are appended to a log
- Repeatable read consistency
- Highly available
- I/O isolation: Allows separating the write path from the read path in the bookies.
- Does not rely on OS page cache
- Slow consumers won't impact latency
- Very effective I/O patterns
	- Journal: Append only and no reads
	- Storage device: Bulk write and sequential reads
- Number of files is independent from number of topics.


## Segment Centric Storage
- In addition to partitioning, messages are stored in segments (based on time and size)
- Segments are independent from each others and spread across all storage nodes.
	- Guarantees write availability when one bookie goes down.

![[pulsar_segments.png]]

## Segments vs partitions
- Apache Kafka is split into multiple partitions
	- The size of the partition is determined based on the size of the storage on the node.
	- Log segments are replicated in order across brokers (one broker = one partition)
- Apache Pulsar is split into segments
	- Log segments are replicated in a configurable number of bookies across N possible bookies.
	- Log segments are evenly distributed to achieve horizontal scalability with no rebalancing.
	- Reconstructing in case of failure can be done from multiple nodes by segment.

![[segments_vs_partitions.png]]



---
# Sources
- https://www.youtube.com/watch?v=O2OXyA3YMMM

<hr>

Related to: [queuing-systems](queuing-systems)