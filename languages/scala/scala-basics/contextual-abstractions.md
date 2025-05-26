# Contextual Abstractions
Omitting parameters for calls that are considered repetitive --> so called *Context Parameters*. This avoids writing repetitive code.
Consider the following example from the documentation:

```
val addresses: List[Address] = ...

addresses.sortBy(address => (address.city, address.street))
```

The `sortBy` function actually requires one more parameter, which is a comparison function that compares each element to determine how it is related to other elements. 
In this case, this is called a context parameter, which is infered by the compiler. As `address.city` and `address.street` are both strings, the compiler infers that it requires a string comparison method.

<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/taste-contextual-abstractions.html

<hr>

Related to:
* [scala-basics](scala-basics.md)