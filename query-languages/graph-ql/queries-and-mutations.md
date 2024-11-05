# Queries and Mutations

## Queries
- Queries are verified to conform to the API.
- Each query will run the required functions

As an example, consider the query below

| ------------ Operation ------------                 | ------------ Response ------------                                                                      |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <code>{ <br>	me { <br>		name <br>	}<br>}<br></code> | <code>{<br>  "data": {<br>    "me": {<br>      "name": "Luke Skywalker"<br>    }<br>  }<br>}<br></code> |
The client can create queries mirror the structure of data, making it simple to request exactly the data that is needed. This would then be expanded by GraphQL into the JSON shown above on the right.

In the previous examples, the operation name was omitted for simplicity. However, it is recommended to always define the operation in production systems. The previous query would look as follows:

```
query MyName { 
	me { 
		name 
	}
}
```

The operation type can be a query, mutation, or subscription, depending on the operation we want to do. We will omit the operation names on the following examples for simplicity, as they are al of type `query`. 

## Arguments
There are times where we want to retrieve only one object. For instance, we may want to retrieve information for an object with a given ID. In such cases, we can provide arguments that allow us to add filters to the queries. In REST, one can only pass a single set of arguments - the query parameters and URL segments in the request. In GraphQL, every field can have its own set of arguments. 
Below is an example of how this would look like.

| ------------ Operation ------------                                               | ------------ Response ------------                                                                                                  |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| <code>{<br>  human(id: "1000") {<br>    name<br>    height<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "human": {<br>      "name": "Luke Skywalker",<br>      "height": 1.72<br>    }<br>  }<br>}<br></code> |

## Aliases
Aliases allow us to query for the same field with different arguments, by renaming the result of a field. This avoids conflicts between fields. Below is an example of using aliases:

| ------------------ Operation ------------------                                                                                             | ------------- Response -------------                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>{<br>  empireHero: hero(episode: EMPIRE) {<br>    name<br>  }<br>  jediHero: hero(episode: JEDI) {<br>    name<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "empireHero": {<br>      "name": "Luke Skywalker"<br>    },<br>    "jediHero": {<br>      "name": "R2-D2"<br>    }<br>  }<br>}<br></code> |

## Fragments
Fragments allow us to define reusable units, which are sets of fields that can be included in queries. This avoids repeating queries and simplifies the request. Below is a demonstration of how this could be used.

| ------------------ Operation ------------------                                                                                                                                                                                                                                                       | ------------- Response -------------                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>{<br>  leftComparison: hero(episode: EMPIRE) {<br>    ...comparisonFields<br>  }<br>  rightComparison: hero(episode: JEDI) {<br>    ...comparisonFields<br>  }<br>}<br>​<br>fragment comparisonFields on Character {<br>  name<br>  appearsIn<br>  friends {<br>    name<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>     "leftComparison": {<br>      "name": "Luke Skywalker",<br>      ...<br>    },<br>    "rightComparison": {<br>      "name": "R2-D2",<br>      ...<br>    }<br>  }<br>}<br></code> |

In this case, we define a fragment called `comparisonFields`, which is then used to retrieve information for the `EMPIRE` and `JEDI` episodes without having to repeat the fields twice.

## Variables
When argument fields are dynamic, it becomes cumbersome to pass them directly in the query string, as client-side code would need to manipulate the query string an runtime. Instead, we can pass all these dynamic fields as a separate dictionary, effectively making the query string go unchanged.

Working with variables involves three main steps:
1. Replace the static value in the query with `$variableName`
2. Declare `$variableName` as one of the variables accepted by the query
3. Pass `variableName`: value in  separate variables dictionary

Below is an example illustrating this

| ------------------ Operation ------------------                                                                                                               | ------------- Response -------------                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>query HeroNameAndFriends($episode: Episode) {<br>  hero(episode: $episode) {<br>    name<br>    friends {<br>      name<br>    }<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "hero": {<br>      "name": "R2-D2",<br>      "friends": [<br>        {<br>          "name": "Luke Skywalker"<br>        },<br>        [...] // continue here<br>      ]<br>    }<br>  }<br>}<br></code> |

Pass a separate `variables` dictionary

```
{
  "episode": "JEDI"
}
```

This allows us to simply pass a different variable instead of having to create a new query. It is good practice to use variables, as it clearly separates dynamic arguments from all remaining arguments. ==We should avoid doing string interpolation with user-supplied values==.


## Directives
Directives are useful to model the request based on dynamic argument values. For instance, consider we only want to retrieve a value from the API when an argument is true. In such cases, we can use directives to specify when to query for something. Below is an example use of directives.


| ------------------ Operation ------------------                                                                                                                                                    | ------------- Response -------------                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <code>query Hero($episode: Episode, $withFriends: Boolean!) {<br>  hero(episode: $episode) {<br>    name<br>    friends @include(if: $withFriends) {<br>      name<br>    }<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "hero": {<br>      "name": "R2-D2"<br>    }<br>  }<br>}<br></code> |

The response on the right is what is produced for the query on the left if the following variables are supplied
```
{
  "episode": "JEDI",
  "withFriends": false
}
```

When `withFriends` is false, the `reponse` will not query for the `name` field. There are two directives we can use:
- `@include(if: Boolean)`: Only include this field in the result if the argument is `true`.
- `@skip(if: Boolean)`: Skip this field if the argument is `true`.

## Mutations
Although any query can cause data writes on the server, GraphQL has established a convention that any operation that causes writes should be sent as a mutation. Similar to how we can request fields in other queries, we can also ask for nested fields if the mutation returns an object. Below is an example of a mutation query (we omit the variables for brevity)

| ------------------ Operation ------------------                                                                                                                                        | ------------- Response -------------                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>mutation CreateReviewForEpisode($ep: Episode!, $review: ReviewInput!) {<br>  createReview(episode: $ep, review: $review) {<br>    stars<br>    commentary<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "createReview": {<br>      "stars": 5,<br>      "commentary": "This is a great movie!"<br>    }<br>  }<br>}<br></code> |

An important thing to take away, is that mutation fields run in series. This is opposed to query fields, which are executed in parallel. This implies that if we send two mutations in one request, the first is guaranteed to finish before the second one begins (there are no race conditions).


---
# Sources



---

Related to: [graph-ql](graph-ql)