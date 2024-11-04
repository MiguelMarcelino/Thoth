# Graph QL
- Query language for APIs and a server-side runtime for executing queries using a type system defined by the application's data
- The application defines types and fields. 
	- A function is written for every field to provide the required data

Below is an example of a service that returns the name of a logged in user

```
type Query {
	me: User
}

type User {
	name: String
}
```

This results in the creation of the following functions

```
// Provide data for the `me` field on the `Query` type
function Query_me(query, args, context, info) { 
	return context.request.auth.user
} 

// Provide data for the `name` field on the `User` type
function User_name(user, args, context, info) { 
	return context.db.getUserFullName(user.id)
}
```

The current user information is retrieved from the `context`, as it is the user that is currently authenticated. 


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
|                                                                                                                                                               |                                                                                                                                                                                                                                       |
Pass a separate `variables` dictionary

```
{
  "episode": "JEDI"
}
```

This allows us to simply pass a different variable instead of having to create a new query. It is good practice to use variables, as it clearly separates dynamic arguments from all remaining arguments. ==We should avoid doing string interpolation with user-supplied values==.


---
# Sources
- https://graphql.org/learn/

<hr>

Related to: [query-languages](query-languages)