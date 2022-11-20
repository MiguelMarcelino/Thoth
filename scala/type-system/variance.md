# Variance
Scala supports invariant, covariant and contravariant types. Here is an example from the documentation:
 
```
// an example of an invariant type
trait Pipeline[T]:
  def process(t: T): T

// an example of a covariant type
trait Producer[+T]:
  def make: T

// an example of a contravariant type
trait Consumer[-T]:
  def take(t: T): Unit
```

## Invariance
* Types like `Pipeline` are invariant in their type argument (T in this case). 
	* Types like `Pipeline[Item]`, `Pipeline[Buyable]`, and `Pipeline[Book]` are in no subtyping relationship to each other.
* A method that expects a `Pipeline[Buyable]` is not compatible with a method that expects a `Pipeline[Book]`, as these two functions can perform completely different operations

## Covariance
* In contrast to he `Pipeline` object, the `Producer` object is covariant
	* `Producer[Book]` can be seen as a ubtype of `Producer[Buyable]`
* Immutable container types are often covariant, as we can always guarantee that the objects are of a specific type

## Contravariance
* Whereas with covariance, we have `Producer[Book] <: Producer[Buyable]`, with contravariance we have  `Consumer[Buyable] <: Consumer[Book]`
	* We inverse the order from what we have seen with covariance


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/types-variance.html#inner-main

<hr>

Related to:
* [type-system](type-system)