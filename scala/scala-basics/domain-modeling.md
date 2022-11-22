# Domain Modeling
The OOP part of Scala

## Traits and Classes
* Similar to Java's interfaces
* Can also contain abstract and concrete methods and fields

Example:

```
trait Speaker:
	def speak(): String  // abstract method
	def getSpeakerNumber(): Int = 0000

class Person(name: String, speakerNumber: Int) extends Speaker:
	def speak(): String = "Hello!"
	override def getSpeakerNumber(): Int = speakerNumber
```

A concrete class extends the trait, allowing us to create new instances of that class. We can override methods from traits by using the `override` keyword.


## Enumerations and Sum Types

Enumerations can be defined as follows:

```
enum Weather
	case Raining, Sunny, Windy, Snowing

val weather = Weather
weather match
	case Raining => println("It is raining today!")
	case Sunny => println("What a sunny day!")
	case Windy => println("Windy, it is today!")
	case Snowing => println("Snowing it is. A fire I must start!")
```

We defined an enum and then use the `match-case` syntax to go through all its elements.

A sum type can be the following:

```
enum Nat:
  case Zero
  case Succ(pred: Nat)
```

As the `Succ` case has parameters, this is called a sum type. In this case it is a recursive sum type.


## Product Types
* It is an Algebraic Data Type (ADT) that has only one shape
	* A singleton is represented by a `case` object
	* An immutable structute is represented by a `case` class

`case` class
* Constructor parameters are public and immutable (`val` fields).
* `unaply` method is generated, allowing one to use the class in match.
* `copy` method is generated, to create object copies.
* `equals` and `hashCode` methods are generated.
* `toString` method is generated.


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/taste-modeling.html#inner-main

<hr>

Related to:
* [scala-basics](scala-basics.md)