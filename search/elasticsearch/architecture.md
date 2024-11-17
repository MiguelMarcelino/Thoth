# Architecture
- It can be seen as an API to many Lucene shards
- Instead of users having to figure out to which shard to connect/store the data to, Elasticsearch does it on its own.
- A group of related shards is presented to the user as an index.
	- An index is a group of related Lucene shards.

## Overview
Below is an overview of the architecture or Elasticsearch

![[elasticsearch_architecture.png]]

Keywords
- Node: A node can be seen as an independent machine that can communicate to other nodes through the network
	- It holds multiple Shards.
- Index: An index is a group of related shards
- Shard: A Shard on Elasticsearch is a Lucene index
	- It holds multiple segments
- Segment: Each Shard (Lucene index) is composed of multiple segments, which are composed of documents
	- A new segment is created every refresh interval (by default, this is set to 1 second)
	- Segments get merged by Lucene over time

Lets look at the architecture of Elasticsearch (and Lucene) from the inside-out.

## Data structure within segments
- Within each segment there is a data structure. It is composed of two parts
	- Sorted Dictionary: Contains the index terms, along with the frequency of those terms
	- Postings: Contains the documents related to those terms.
- The terms decide how we can search the data. 
- The performance of data search is influenced by what data we are searching for.
	- E.g. If we are searching for a suffix of a string, we have to index the inverted suffix
	- If the intent is to search for geolocation data, Lucene will instead index the hash of the coordinates
- Stored fields
	- Key-value store that helps render the search results
	- Relevant for when we want to search for properties in the documents
	- By default, Elasticsearch stores the entire JSON source, but this could have a negative impact to performance when searching through millions of documents.
- Document Values (Field cache)
	- Highly optimized for storing values of the same type
	- Good for aggregating, sorting for millions of files.
	- Loads all the values for the field into memory (uses a lot of memory)

## Deletes and insertions
- Segments are immutable
	- Deletions of documents are marked on a bitmap. 
	- Every subsequent search filters out these items based on this bitmap
	- To keep in mind when storing rapidly updated counters
- An update is a delete followed by a re-index
- Lucene is good at compressing data
	- Segments are a great scope for caches
	- Segments get merged into larger segments.

## Segment creation
- As we index new documents, Elasticsearch will buffer these documents
- Every refresh interval (default 1 second), it writes a new segment
- Over time, we will get a lot of segments
	- Elasticsearch merges these smaller segments periodically
	- This is when deleted documents are completely removed.
- The new segment will have cold caches
	- The majority of the data is still on old segments, which still have valid caches
	- Amount of cache invalidation is limited

## Searching through shards
- Searching shards is similar to searching within segments
	- We search all the shards and merge the results
	- Search needs to merge across nodes, which involves transfers across network
- Searching one ES index with 2 shards is the same as searching 2 ES indexes with one shard each (==TODO: Still not clear==)
	- E.g. Log data should be segmented by day
- Shards are used to evenly distribute data across nodes
	- One important thing: Although a shard can be moved to another node, it cannot be split into multiple shards.
	- There is a balance for the number of shards too create. Too many shards results in duplicating the data structures, such as the dictionaries. Large shards can result in poor shard distribution across nodes.

## Cluster state
- Cluster has a cluster state, which is replicated to all the nodes
	- Contains mappings, which contain information about how a field should be processed
	- Shard routing table, which allows any node in the cluster to route search requests


---
# Sources
- https://www.youtube.com/watch?v=PpX7J-G2PEo

---

Related to: 
- [elasticsearch](elasticsearch)
