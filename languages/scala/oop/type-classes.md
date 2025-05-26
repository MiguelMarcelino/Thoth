# Type Classes

- A type class is an abstract, parameterized type that lets one add new behaviour to a closed data type without subclassing
- A type class is useful when
	- Expressing how a type you don't own conforms to such behaviour
	- Expressing such a behaviour for multiple types without involving subtype relationships between those types.

### Example
Lets consider the Show type class, which is well known in Haskell.

```scala
// a type class
trait Showable[A]:
  extension (a: A) def show: String
```


Some important things to note
- Type classes take a parameter type to say which type we provide the implementation of show for (in this case, `A`)
- To add functionality to a type, the classic trait requires that A extends Show, while for type-classes we require to have an implementation of `Showable[A]`.
- In Scala 3, to allow the same method calling syntax in both Showable that mimics the one of Show, we define `Showable.show` as an extension method.

We can now implement a concrete instance that uses the show method:

```scala
case class Person(firstName: String, lastName: String)
```

To define Showable for person, we can do it as follows

```scala
given Showable[Person] with
  extension (p: Person) def show: String =
    s"${p.firstName} ${p.lastName}"
```

Once we defined the behaviour of `Showable[Person]`, we can now use it in Scala as follows:

```scala
val person = Person("John", "Doe")
println(person.show)
```


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/ca-type-classes.html

<hr>

Related to: [oop](oop)