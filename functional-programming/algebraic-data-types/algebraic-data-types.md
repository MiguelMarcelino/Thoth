# Algebraic Data Types (ADTs)

In computer science, particularly in functional programming and type theory, algebraic data types are a way to define complex types by combining other types. They are composed using two main constructs:
Sum types (also called tagged unions or variants)
Product types (like tuples or records).

These types are called algebraic because you can think of them like algebraic expressions - using `+` for sum types and `×` for product types.


## Product Types (AND)

These combine multiple values into one. Think of a struct or tuple: you have all the values.

Example:

```Haskell
data Point = Point { x :: Double, y :: Double }
```

Here, a Point has both an x and a y. This is like `Point = number × number`.

## Sum Types (OR)

These allow a value to be one of many types. Each option is tagged so you know what kind of value it is.

Example:
```Haskell
data Shape
= Circle { radius :: Double }
  | Rectangle { width :: Double, height :: Double }
```

A Shape is either a circle or a rectangle, but not both. This is like `Shape = Circle + Rectangle`.


## Why ADTs Matter
- They model real-world data clearly and safely.
- Help with pattern matching, which is powerful in languages like Haskell, Rust, or OCaml.
- Make your code easier to reason about and less error-prone.

### Example: Pattern Matching

This function shows how pattern matching works naturally with ADTs in Haskell.

```Haskell
area :: Shape -> Double
area (Circle r) = pi * r * r
area (Rectangle w h) = w * h
```

---

# Sources
- https://bartoszmilewski.com/2015/01/13/simple-algebraic-data-types/

<hr>

Related to: [functional-programming](functional-programming)