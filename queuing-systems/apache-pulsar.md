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
	-  ==One topic is always owned by a specific broker at any given time. ==
		- This helps with caching data for a topic
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
		- These can be seen as compute services that connect to an independent storage layer (they are scaled independently of storage)
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
	- The size of the partition is determined based on the size of the storage on the broker.
	- Log segments are replicated in order across brokers (one broker always stores the segments of a particular partition)
- Apache Pulsar is split into segments
	- Log segments are replicated in a configurable number of bookies across N possible bookies.
	- Log segments are evenly distributed to achieve horizontal scalability with no rebalancing.
		- Assumption: I assume that one of the advantages is that reconstructing in case of failure can be done from multiple nodes by segment.
	- This allows setting up tiered storage
		- Apache BookKeeper can store newer data, while historical data can be stored on AWS S3
		- Higher granularity when compared to Kafka

![[segments_vs_partitions.png]]

> **Personal Note**: The main differentiating factor is that Apache Kafka does not allow splitting the individual segments inside the partitions. When we replicate the partitions, then all segments inside those partitions are also replicated. 
> With Apache Pulsar, the individual segments are replicated and distributed across the Bookies. This is similar to removing the Partition definition from Kafka and allowing all segments to be split amongst individual bookies. This can allow for better horizontal scalability, as segments are smaller than partitions.

==Interesting Question: Is storing the individual segments actually better for performance? I have seen several compassions between Pulsar and Kafka, and Kafka always manages to have higher throughput. Maybe it is actually an advantage to keep all segments for a partition stored contiguously, instead of unordered in a Bookie (assuming they are actually unordered)?==

## Replicated Subscriptions
- Consumption will restart close to where a consumer left off. This allows for a small amount of duplications
- Implementation:
	- Markers are injected into the data flow
	- Consistent snapshot of message IDs is created across the cluster
	- Establish relationship: If `MA-1` were consumed in cluster A, then `MB-2` must have been consumed in Cluster B.

## Multi-Tenancy
- A single Pulsar Cluster supports multiple users and mixed workloads.
- Authentication, Authorization, Namespaces, Admin APIs
- I/O isolation between reads and writes
	- Provided by BookKeeper
	- Ensure readers draining backlog won't affect publishers.
- Soft isolation: Storage quotas, flow-control, back-pressure, rate limiting.
- Hardware Isolation: Constrain some tenants on a subset of brokers or bookies.

## Pulsar functions
- User supplied compute against a consumed message
	- ETC, data enrichment, filtering, routing
- Simplest possible API
	- Use language-specific function notation
	- No SDK required
- Language agnostic
- Pluggable runtime
	- Managed or manual deployment
	- Run as threads, processes, or containers in Kubernetes

### State Management
- Implemented on top of Apache BookKeeper's Table service
- BookKeeper provides a sharded key/value store based on
	- Log and Snapshot: Stored as Bookkeeper ledgers
	- Warm replicas that can be quickly promoted to leader
- In case of leader failure there is no downtime or huge log to replay

## Pulsar SQL
- Read data directly from BookKeeper into Presto
	- Bypass Pulsar Broker
- Many-to-many data reads.
	- Data is split even on a single partition
	- Multiple workers can read data in parallel from a single Pulsar partition
- Time-based indexing
	- `publishTime` is used in predicates to reduce data reads


---
# Sources
- https://www.youtube.com/watch?v=O2OXyA3YMMM

<hr>

Related to: [queuing-systems](queuing-systems)