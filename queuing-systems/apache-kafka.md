# Apache Kafka

## What is Kafka?
Kafka is an event streaming platform that combines three key capabilities
- To __publish (write) and subscribe to (read)__ streams of events
- To __store__ streams of events durably and reliably
- To __process__ streams of events as they occur or retrospectively

In Kafka, there are __servers__ and __clients__ that communicate via the TCP protocol
- Servers:
	- Kafka runs as a cluster of one or more servers that can span multiple datacenters or cloud regions
	- Storage layer servers are called __brokers__.
	- Other servers run Kafka Connect. These import/export data as events and integrate with existing systems, such as DBs.
- Clients:
	- Read, write and process streams of events in parallel


## Main Concepts and Terminology
- Event: Records the fact that "something happened". It can also be called a *record* or *message*
- Producers: Clients that write events to Kafka.
- Consumers: Clients that subscribe (read and process) events
	- A consumer is completely decoupled from the producer. A slow consumer does not affect a producer.
	- Kafka provides several guarantees, such as processing events exactly once.
	- Consumers keep track of the last message they read (they store the offset of the last position they read in the log)
	- Consumers live in groups
		- We can scale out consumers by adding more instances of a specific consumer
- Topics are similar to a folder in a filesystem, where the events are the files. 
	- A topic is a persistent record of events. They are streams of related messages. 
	- We can see topics as a log.
	- Topics are always multi-producer and multi-consumer: A topic can have zero, one, or many producers writing to it, as well as zero, one, or many consumers subscribing to the events.
	- Events from a topic can be read as often as needed (events are not deleted after consumption). 
	- Performance is constant, even with thousands of stored events
- Topics are partitioned
	- A topic is spread over a number of buckets located on different Kafka brokers.
	- Allows client applications to read and write data from/to many brokers at the same time.
	- Events with the same event key are written to the same partition
	- Consumers of a given topic-partition will always read that partition's events in exactly the same order as they were written
- Every topic can be replicated
	- It is common to have a replication factor of 3.

#### General Architecture

Zookeper
- Cluster Management
- Failure detection and recovery
- Store ACLs and secrets

![[kafka_architecture.png]]


#### Kafka Topics, Partitions, and Segments
- We can break a topic into partitions
- Partitions can be allocated to different brokers
	- A partition is a log.
		- Every partition contains a sequence of entries that behaves as a log. 
		- When a new entry is added to this log, it is attributed a unique index. Indexes start from zero and auto-increment when a new entry is added
		- Every partition is attributed its own offset. This ensures there is no clashes between partitions.
	- A message is added to the end of the partition (since logs are immutable, we can only add it to the end)
	- We have an ordered set of events.
	- Each partition is broken in multiple segments
- Messages with the same key always land on the same partition, as long as the number of partitions stays constant. The default strategy is as follows:
	- `hash(key) % number_of_partitions`

![[kafka_partitions_and_segments.png]]

One important thing to note is that not all partitions from a topic will be stored in the same broker. In the image below, topic a is stored in 3 partitions. These are stored across Brokers 101, 102, and 104.

![[kafka_partitions_and_segments_colour.png]]

#### Kafka message
Kafka messages are composed of 4 components:
- Header: Identify the event
- Key: Identifies an event
- Value: The contents of the event
- Timestamp: The time at which the event was created. Every message is automatically attributed a timestamp.


![[kafka_message.png]]

#### Broker Replication
Every partition is replicated across multiple brokers. When a partition is replicated, there are two main concepts:
- Leader: The main partition. 
	- The producer connects to the broker that has the lead partition
- Follower: The replicas of the main partition
	- Followers scrape the messages to be up-to-date

![[kafka_replication.png]]

## Kafka API
Kafka has 5 core APIs for Java and Scala:
- Admin API: Manage and Inspect topics, brokers and other Kafka objects.
- Producer API: Publish a stream of events to one or more Kafka topics.
- Consumer API: Subscribe to one or more topics and process streams of events.
- Kafka Streams API: To implement stream processing applications and microservices.
	- Higher-level functions to process streams: joins, aggregations, etc.
- Kafka Connect API: Build and run reusable data import/export connectors that consume or produce streams of events from and to external systems so they integrate with Kafka.
	- Kafka connect is used when we want to get data into Kafka (E.g. We want to import data from a database to a topic).

## K-SQL
To query for the data in Kafka, we can use a syntax that is similar to SQL called K-SQL. This allows us to select only the desired data from a given topic. The output of this query is another topic, which contains the results selected by the query. We can then use this topic to perform further analysis.


![[kafka_consumers.png]]


---

# Sources
- https://kafka.apache.org/documentation/#gettingStarted
- https://www.youtube.com/watch?v=06iRM1Ghr1k
- https://www.youtube.com/watch?v=B5j3uNBH8X4


<hr>

Related to: [queuing-systems](queuing-systems)