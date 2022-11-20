
# Traits
* Traits are used to share interfaces and fields between classes. 
* They are similar to Java’s interfaces. 
* Traits cannot be instantiated

Example:
```
trait Pet:
  val name: String

class Cat(val name: String) extends Pet
class Dog(val name: String) extends Pet
```


<hr>

## Sources
- https://docs.scala-lang.org/tour/traits.html#inner-main

<hr>

Related to: [oop](oop)