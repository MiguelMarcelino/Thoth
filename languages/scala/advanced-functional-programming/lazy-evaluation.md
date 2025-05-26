# Lazy evaluation

## Intro to `withFilter`

* `withFilter` is a lazy filtering method used in for-comprehensions.
* It behaves like `.filter`, but doesn't immediately evaluate or allocate a new collection.
* It’s used under the hood by `for`-comprehensions when you write an `if` clause.

## Why use `.withFilter`

* `.filter` creates a new collection immediately.
* `withFilter` delays filtering until the actual iteration or transformation happens — more efficient, especially in chains.

## How it's used in for-comprehensions

When you write this:

```scala
for {
  x <- List(1, 2, 3, 4) if x % 2 == 0
} yield x * 10
```

Scala desugars it into:

```scala
List(1, 2, 3, 4).withFilter(x => x % 2 == 0).map(x => x * 10)
```

So:

* The `if` becomes a `.withFilter(...)`
* It’s lazy and avoids creating temporary collections


## Important Details

* `withFilter` returns a special wrapper (`WithFilter`) that supports `.map`, `.flatMap`, and `.foreach` — but not all collection methods.
* If your custom collection defines `map`, `flatMap`, `foreach`, it must also define `withFilter` to work with for-comprehensions using `if`.

# Sources
- Advanced Scala - Rock the JVM Course

---

Related to: [advanced-functional-programming](advanced-functional-programming)