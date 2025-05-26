# Singleton
* Scala's `object` keyword defines a singleton object, a.k.a. a class that has exactly one instance.
* Its methods can be accessed like static methods in a Java class. 
* With singleton objects, one can call the methods directly on the object, instead of having to create a new instance

## Companion Objects
A companion object can access the private methods and fields of a singleton object. Consider the following example from the documentation:

```
class Circle(radius: Double):
  import Circle.*
  def area: Double = calculateArea(radius)

object Circle:
  private def calculateArea(radius: Double): Double =
    Pi * pow(radius, 2.0)
```

Notice that the `Circle` class accesses the private `calculateArea` method, defined in the `Object` singleton.

## Creating modules from traits
Objects can also be used to implement traits to create modules. In this case, a module can extend one or more traits, allowing for them to be grouped into a single module. 

Example from documentation:

```
trait AddService:
  def add(a: Int, b: Int) = a + b

trait MultiplyService:
  def multiply(a: Int, b: Int) = a * b

// implement those traits as a concrete object
object MathService extends AddService, MultiplyService
```


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/taste-objects.html

<hr>

Related to:
* [scala-basics](scala-basics.md)