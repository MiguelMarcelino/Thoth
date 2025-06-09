# Monads

## What is a Monad?

A monad is a design pattern that consists of:

* A type constructor `M[_]`
* A `flatMap` (or `bind`) operation
* A `pure` (or `unit` / `return`) operation

So we have the following definition in Scala

```scala
trait Monad[M[_]] {
  def pure[A](a: A): M[A]
  def flatMap[A, B](fa: M[A])(f: A => M[B]): M[B]
}
```

## Monad Laws (Why Identity Matters)

There are three monad laws — and two of them are about identity:

| Law | Description  |
| ------------------ | ---------------------------------------------------------------------------------- |
|  Left identity  | Wrapping a value and flatMapping over it is the same as just applying the function |
| Right identity | flatMapping a monad with `pure` doesn't change it                                  |
|  Associativity      | Nested flatMaps can be reordered                                                   |

## Left Identity in Monads

```scala
pure(x).flatMap(f) == f(x)
```

> If you lift a value into a monad and immediately apply a function, it should be the same as just applying the function directly.

### Example with `Option`:

```scala
Some(3).flatMap(x => Some(x * 2)) == Some(6)
```

Is equal to:

```scala
val f = (x: Int) => Some(x * 2)
f(3) == Some(6)
```

---

## Right Identity in Monads

```scala
m.flatMap(pure) == m
```

> Meaning: If you flatMap a monad and just wrap the value again, it should be unchanged.

### Example with `Option`:

```scala
Some(3).flatMap(Some(_)) == Some(3)
```

---

## Why This Matters

These identity laws are essential for reasoning about monadic code. They guarantee that:

* Wrapping and unwrapping don’t cause side effects
* Chaining operations is predictable and composable
* Monads behave like algebraic structures, which helps build generic, reusable abstractions (e.g., in libraries like Cats, ZIO)

Without these laws, using monads would be like working with functions or collections that randomly mutate or behave inconsistently — which kills composability.


---

# Sources
- Advanced Scala - Rock the JVM Course

---

Related to: [advanced-functional-programming](advanced-functional-programming)