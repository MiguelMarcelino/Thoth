# Multiversal Equality

Scala used to have *universal equality*, where any two values could be compared for equality. This is because both the `==` and `!=` functions are implemented in terms of Java’s equals method, which compare values of any two reference types. However, this could become a problem for type safety. Consider the following example from Scala's documentation:

```
val x = ...   // of type T
val y = ...   // of type S, but should be T
x == y        // typechecks, will always yield false
```

This could result in unexpected runtime errors when executing the third operation when executing the `equals` method.
To solve this problem, multiversal equality is a way to opt-in to make classes support equals checks. An example from Scala's documentation is shown below:

```
case class Dog(name: String) derives CanEqual
```


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/ca-multiversal-equality.html#inner-main


<hr>

Related to: [contextual-abstractions](contextual-abstractions.md)