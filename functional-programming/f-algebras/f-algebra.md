# F-Algebra

F-algebras are a mathematical concept used in category theory and functional programming, especially in recursion schemes. They provide a structured way to describe recursive data types and computations over them.

## Definition
An **F-algebra** consists of a pair `(A, α)`, where:
1. **Carrier Object (`A`)**: An object in a category that represents the data structure.
2. **Structure Map (`α: F(A) → A`)**: A morphism that describes how the functor `F` — which defines the shape of the data structure — maps `F(A)` to `A`.


### Example A: Lists as an F-Algebra
Let's take a simple example: summing a list of integers.

1. **Define the functor**  
   A list can be represented as:
   - Either empty (`Nil`).
   - Or a value (`head`) and a rest (`tail`), written as `Cons(head, tail)`.

   We define a functor `F(X)` that describes this structure:

   ```scala
   sealed trait ListF[A]
   case class NilF[A]() extends ListF[A]
   case class ConsF[A](head: Int, tail: A) extends ListF[A]
   ```

2. **Define the carrier type**  
   The carrier type `A` represents what we compute on the structure. For summing a list, `A = Int`.

3. **Define the algebra function**  
   The algebra function `F(Int) => Int` specifies how to reduce a list structure into an integer:

   ```scala
   def sumAlgebra: ListF[Int] => Int = {
     case NilF()        => 0          // Base case: Empty list sums to 0
     case ConsF(h, t)   => h + t      // Sum head and tail recursively
   }
   ```

### Example 2: Natural Numbers as an F-Algebra

Consider the natural numbers, which can be represented using the following functor:

```haskell
data NatF a = ZeroF | SuccF a
```

Here, `NatF` is a functor that describes a number as either zero (`ZeroF`) or the successor (`SuccF`) of another number. An algebra for this functor would specify how to interpret these constructors into a specific carrier type. For instance, to compute the Fibonacci sequence, we can define the following algebra:

```haskell
fib :: NatF (Int, Int) -> (Int, Int)
fib ZeroF = (1, 1)
fib (SuccF (m, n)) = (n, m + n)
```

Applying the catamorphism (`cata fib`) to this algebra computes Fibonacci numbers by recursively applying the `fib` function.


## Catamorphisms (Folds)

A **catamorphism** is a generalization of the fold function, providing a way to deconstruct data structures defined as initial F-algebras. For a functor `F`, the catamorphism is defined as:


```haskell
cata :: Functor f => (f a -> a) -> Fix f -> a
cata alg = alg . fmap (cata alg) . unFix
```


This function recursively applies the algebra `alg` over the structure, effectively reducing it to a single value.

## Coalgebras

Dual to algebras, an **F-coalgebra** consists of a pair `(A, α)`, where `α: A → F(A)`. While algebras provide a way to deconstruct data structures, coalgebras describe how to construct or unfold them. For example, an infinite stream can be modeled as a coalgebra, where each step generates the next element and the subsequent state. 

Understanding F-algebras and their related concepts like catamorphisms and coalgebras offers a powerful framework for working with recursive data structures in functional programming and category theory.

### Why is this Useful?
- **Separation of structure and computation**: The functor `F` defines structure, and the algebra function defines computation.
- **Generalization**: You can replace `sumAlgebra` with any other computation, like finding the max or converting a list to a string.

---

# Sources
- https://en.wikipedia.org/wiki/F-algebra
- ChatGPT
