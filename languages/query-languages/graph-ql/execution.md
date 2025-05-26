# Execution

- We can think of each field in GraphQL as a function or method of the previous type, which returns the next type.
- Each field on each type is backed by a function called the `resolver`, which is provided by the GraphQL server developer
- When a field is executed, the corresponding resolver is called to produce the next value
	- If the field produces a scalar, the execution completes
	- If the field produces an object, then the query contains more fields that apply to that object

## List resolvers

GraphQL will attempt to retrieve objects in parallel, when possible. This is the case when loading list objects. Lets consider an example where we have a `Human` that pilots multiple `Starship`s and we want to retrieve all the starships the human pilots. In this case, GraphQL's resolver will return a list of Futures (or Promises in Javascript), each containing one starship. Below is how this would work:

```
Human: {
  starships(obj, args, context, info) {
    // Returns a Promise for every query
    return obj.starshipIDs.map( 
	  // We run the query for every starship
      id => context.db.loadStarshipByID(id).then(
        shipData => new Starship(shipData)
      )
    )
  }
}
```

GraphQL will wait for all these promises concurrently before continuing.


---
# Sources
- https://graphql.org/learn/

---

Related to: [graph-ql](graph-ql)