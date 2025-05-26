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


---
# Sources
- https://graphql.org/learn/

<hr>

Related to: [query-languages](query-languages)