# Functional Set

## Functional Sets as Functions

* A `Set[A]` is defined as a function: `A => Boolean`.
* This means the set is characterized by its membership predicate.
* This approach aligns with the Church encoding idea in functional programming.
    * It aligns with Church encoding because it defines data by its operations (i.e., how it reacts to input), not its structure.
    * See [notes on church encoding](church-encoding) for more info.
* This design reinforces core FP concepts: immutability, higher-order functions, and declarative design.

## Key Operations Must Preserve Functional Purity

Each set operation must be implemented purely, without mutating data. These include:

* contains – implemented as function application.
* add – returns a new set with a predicate that includes the new element.
* union – combines two sets by logical OR.
* intersection – combines by logical AND.
* difference – includes elements in one set but not in the other.
* complement – flips the predicate logic.

Examples:

```scala
def union[A](s1: Set[A], s2: Set[A]): Set[A] = x => s1(x) || s2(x)
def intersect[A](s1: Set[A], s2: Set[A]): Set[A] = x => s1(x) && s2(x)
def diff[A](s1: Set[A], s2: Set[A]): Set[A] = x => s1(x) && !s2(x)
```

## Sets as First-Class Citizens

* Sets can be higher-order, meaning they can take or return other sets/functions.
* Sets can be composed using logic operators just like functions.

## Property-Based Sets
Absolutely — here's a structured and concise set of notes you can add to your "Advanced Scala" course notes for Property-Based Sets, in the same style as your functional set notes.

---

## Property-Based Sets (PBSet)
* A property-based set is defined by a predicate: `A => Boolean`.
* This predicate describes membership in the set.
* You don’t store actual elements. Instead, you define rules for which elements belong.
* This representation allows for:
  * Representing infinite sets (e.g., all even numbers, all x > 100).
  * Highly flexible composition of sets.
* It’s a natural extension of the functional set concept, generalizing the idea of sets as predicates.

---

### Key Operations

#### `+` (Add an element)

* Expands the predicate to also include the new element.
* Returns a new set that includes:
    * All elements previously in the set (`property(x)`), and
    * The new element `elem`.

```scala
infix def +(elem: A): FSet[A] =
  new PBSet(x => x == elem || property(x))
```

#### `++` (Union of sets)

* Builds a union of two sets by OR-ing their predicates.
* Resulting set contains elements that satisfy either predicate.

```scala
infix def ++(anotherSet: FSet[A]): FSet[A] =
  new PBSet(x => property(x) || anotherSet(x))
```

#### `contains` (Apply the predicate)

* Simply evaluates the set’s predicate on the given element.

```scala
def contains(elem: A): Boolean = property(elem)
```

### Limitations

* No iteration: you cannot enumerate the elements of a general `PBSet`, especially if it's infinite.
* Difficult (or impossible) to define operations like `map`, `flatMap`, or `foreach` unless the set is finite and concrete.
* You may need to restrict or override these methods in `PBSet` to prevent misuse.


### Simulating `Cons`
You cannot directly model a `case class Cons(head, tail)` as a property-based set because PBSet stores no elements or structure. However, you can mimic the construction of `Cons` by chaining predicates:

```scala
def cons[A](head: A, tail: PBSet[A]): PBSet[A] =
  new PBSet(x => x == head || tail(x))
```

This lets you simulate `Cons` behavior declaratively.

---

# Sources
- Advanced Scala - Rock the JVM Course

---

Related to: [advanced-functional-programming](advanced-functional-programming)