# Composition vs Inheritance

## Inheritance
Inheritance should be used when the intent is to implement an is-a relationship between objects. It can be implemented by extending a base class to extend its functionality. Base properties are retained, and additional behaviour can be defined

As an example, lets consider the definition of an `Element`, which can be defined as an abstract class in Scala:

```scala
abstract class Element {
	def contents: Array[String]  
	val height = contents.length  
	val width =  
	if (height == 0) 0 else contents(0).length  
}
```

We can extend this base class by using Scala's `extend` keyword. Here, we define an `ArrayElement` object, which extends Element. Since we are defining a new `contents` method, Scala automatically overrides the method in the abstract class (there is no need for a specific override clause). The override is still necessary when overriding a concrete member in the parent class.

```scala
class ArrayElement(conts: Array[String]) extends Element {  
	def contents: Array[String] = conts  
}
```

Since Scala supports subtyping, we can always assign an an `ArrayElement` whenever an object of type `Element` is expected.
One important thing to remember is that both fields and methods share the same namespace in Scala. Therefore, a field can override a parameterless method without modifying the method definition in the parent class. Below is an example of this use-case:
```scala
class ArrayElement(conts: Array[String]) extends Element {  
	val contents: Array[String] = conts  // Use of val instead of def
}
```

We can further simplify this definition by combining the parameter and the field, creating a parametric field (we can also use var, if we intend to make the field modifiable):

```scala
class ArrayElement(val contents: Array[String]) extends Element
```

## Composition
Composition is used when the intent is to implement a has-a relationship between objects. It is achieved by defining instance variables with other objects. One compelling argument in favour of composition, is that it avoids common inheritance problems, such as the fragile base class problem, where changes in a superclass can inadvertently affect its subclasses.

As an example, let us consider adding a new `LineElement` class to the previous hierarchy. With inheritance, it would look something like this:

```scala
class LineElement(s: String) extends ArrayElement(Array(s)) {  
	override def width = s.length  
	override def height = 1  
}
```

Although this is possible, the implementation of `LineElement` becomes dependent of `ArrayElement`, which makes the code less flexible and less maintainable. As an alternative, we could use composition and allow `LineElement` to have its own array of elements:

```scala
class LineElement(s: String) extends Element {  
	val contents = Array(s)  
	override def width = s.length  
	override def height = 1  
}
```

This new implementation makes the code more flexible, as it decouples `LineElement` from `ArrayElement`.

---

Related to: [oop](oop)