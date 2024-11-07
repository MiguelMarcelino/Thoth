# Schemas and Types

## Object types and fields

Object types represent a kind of object that can be fetched from a service. Below is an example of an object type:

```
type Character {
  name: String!
  appearsIn: [Episode!]!
}
```

We can go over each of the objects components:
- `Character`: A GraphQL Object Type.
- `name` and `appearsIn`: fields on the `Character` type. These are the only fields that can appear in a query operating on the `Character` type.
- `String`: Built-in scalar type. Other scalar types include
	- `Int`: A signed 32‐bit integer.
	- `Float`: A signed double-precision floating-point value.
	- `String`: A UTF‐8 character sequence.
	- `Boolean`: `true` or `false`.
	- `ID`: Represents a unique identifier often used to re-fetch an object or as the key for a cache.
- `String!`: Indicates the field is non-nullable
- `[Episode!]!`: Array of `Episode` objects. Since the array is non-nullable, we can always expect zero or more elements. Also, since `Episode!` is non-nullable, we can always expect every item of the array to be an `Episode` object.


## Arguments

Every field in a GraphQL object can have zero or more arguments. For instance, consider the example type below:

```
type Starship {
  id: ID!
  name: String!
  length(unit: LengthUnit = METER): Float
}
```

The `length` field has an argument named `unit`. In this case, `unit` is an optional argument, as it has a default value `METER`.

## Interfaces

An Interface is an abstract type that includes a certain set of fields that a type must include to implement the interface. Below is an example of a `Character` interface that represents a character in the Star Wars trilogy:

```
interface Charcter {
  id: ID!
  name: String!
  friends: [Character]
  appearsIn: [Episode]!
}
```

Other types that implement this interface need to define the exact same fields as specified in the interface and can also add new fields. As an example, consider the types `Human`  and `Droid` below:

| <code>type Human implements Character {<br>  id: ID!<br>  name: String!<br>  friends: [Character]<br>  appearsIn: [Episode]!<br>  starships: [Starship]<br>  totalCredits: Int<br>}<br></code> | <code>type Droid implements Character {<br>  id: ID!<br>  name: String!<br>  friends: [Character]<br>  appearsIn: [Episode]!<br>  primaryFunction: String<br>}<br></code> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Input Types

When we want to pass more complex objects to queries, and especially mutations, we can create input types. Input types allow us to pass whole objects to queries. Below is an example of an input type:

```
input ReviewInput {
  stars: Int!
  commentary: String
}
```


We can use an input type as follows (we omit the variables for brevity):

| Operation                                                                                                                                                                              | Response                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <code>mutation CreateReviewForEpisode($ep: Episode!, $review: ReviewInput!) {<br>  createReview(episode: $ep, review: $review) {<br>    stars<br>    commentary<br>  }<br>}<br></code> | <code>{<br>  "data": {<br>    "createReview": {<br>      "stars": 5,<br>      "commentary": "This is a great movie!"<br>    }<br>  }<br>}<br></code> |

The fields on an input object type can themselves refer to other input object types, but ==you can’t mix input and output types in your schema. Input object types also can’t have arguments on their fields==.

---
# Sources
- https://graphql.org/learn/

---

Related to: [graph-ql](graph-ql)