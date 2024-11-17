# Apache BookKeeper
- Infinite stream of log records
- Horizontally scalable storage
- Fault-tolerant
- Low-latency writes
- Offers durability, tuneable replication, and strong consistency

## Use cases
- As write-ahead log (WAL) in 
	- HDFS namenode
	- Twitters Manhattan DB, which is a distributed key-value store
	- HerdDB: JVM embeddable distributed database
- [Apache Pulsar](apache-pulsar.md): Message and Offset store

## B-tree vs LSM
- Primary data structures for storage engines
- B-tree behind traditional databases
	- PostgreSQL, MySQL
	- Indexing for expensive random access on HDD
- Log structured Merge (LSM) trees
	- Good write throughput
	- Behind many modern workloads:
		- Stream: Apache BookKeeper, Kafka Streams, Apache Pulsar, Flink
		- OLTP: MongoRocks, CockroadDB
		- TSDB: influxDB
	- Takes advantage of SSD throughput

## BookKeeper = ZooKeeper + RocksDB
- RocksDB
	- Implements LSM
	- Embeddable
	- Key-value store
	- Append only: Low-latency and High throughput
	- Duplicate record for update/delete
	- Compaction to remove stale / deleted records
		- Values are not deleted immediately. Only when compaction happens is data compacted.
- Zookeeper
	- Metadata Store
	- Cluster coordination
	- Service discovery
	- Leader election

RocksDB is used on each node, while Zookeeper is used to coordinate amongst several nodes.


## Replication
- Data is replicated across Bookies
	- There is a given write quorum, which is composed of 2 or more Bookies
- Unhealthy bookies can be replaced by new healthy bookies.

![[bookkeeper_replication.png]]

## Bookie data
- Entries:
	- Actual data written to ledgers
	- Also includes metadata
	- Entry contains the following: `ledgerId`, `entryId`, `checksum`, …
- Entry log file:
	- Physical file entries
	- Offsets indexed for fast lookup
	- Asynchronous garbage collection of deleted and stale entries
- Journal
	- WAL (Write-ahead log)
	- Append only semantics
	- Low latency, high throughput
- Ledger
	- Logical unit of storage for APIs in BookKeeper
	- Append-only semantics
	- Indexed and cached for faster lookups
	- Includes: `status`, `lastEntryId`, …

## Client and Server
- Client-Based replication
	- BookKeeper has no leader/follower
	- Same responsibility across nodes
	- Bookie client implements replication, coordination, and consistency
	- Separate auto-detection and restore module if entries are lost

## Offsets
- Last Add Confirmed (LAC)
	- Sent in response to writes
	- Cumulative ACK
	- Readers can read until LAC
- Last Add Pushed (LAP)
	- Last entry client requested to write
	- Write in progress, not ACKed yet

![[bookkeeper_offsets.png]]

A new writer adds a new Ledger. Writes and reads continue from there.

## Pulsar Broker and BookKeeper

![[bookkeeper_and_pulsar.png]]


![[bookkeeper_and_pulsar_topic_mapping.png]]

---
# Sources
- https://www.youtube.com/watch?v=n5OuklSiyKY

<hr>

Related to: 
- [data_storage](data_storage.md)
