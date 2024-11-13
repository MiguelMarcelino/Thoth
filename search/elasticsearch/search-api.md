# Search API
- A search consists of one or more queries that are combined and sent to Elasticsearch
- Search can be limited to a specific index or return a specific number of results
- Allows for searching or aggregating data stored in Elasticsearch data streams or indices


## Running a search

Below is an example of searching using a `match` query

```
GET /my-index-000001/_search
{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
```

This query will search for all the documents in the selected index that match the user ID `kimchy`.

## Common search options
- Query DSL: Supports a variety of query types, which include:
	- Boolean and Compound Queries: Allow combining queries and match results based on multiple criteria
	- Term-level queries: filtering and finding exact matching
	- Full text queries: used in search engines
	- Geo and spatial queries
- Aggregations: Search aggregations allow one to get statistics and analytics for search results. 
	- E.g. Average response time for servers, Top IP addresses hit on network, total transaction revenue by customer
- Search multiple data streams and indices: 
	- Comma-separated values and grep-like index patterns can be used to search several data streams and indices in the same request. 
- Paginate search results: Retrieve only first matching hits
- Retrieve selected fields: Query by properties
- Sort search results
- Run async search:
	- ==Since most results are returned in milliseconds, searches are synchronous by default. The search request waits for complete results before returning a response==.
	- Since complete results can take longer for searches across large data sets or multiple clusters, we can use async searches. This first retrieves partial results for long-running searches.

---

Related to: 
- [elasticsearch](elasticsearch)
