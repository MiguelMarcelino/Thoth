# Definitions - The simple kind

## Isomorphism, Homomorphism, and Lambeks theorem
Imagine you have a LEGO instruction manual (`F i`) and the finished LEGO spaceship (`i`). The **evaluator** `j` is like *building the spaceship* from the instructions. The **inverse** `m` is like *taking it apart back into instructions*.

Now:
- If you can **build and unbuild** the spaceship perfectly — no pieces lost, nothing extra — that means the instructions and the spaceship are basically *the same thing in disguise*. That’s what an **isomorphism** means.
- A **homomorphism** is just a way to translate from one set of LEGO instructions to another, while keeping the meaning (how they build a spaceship) the same.

Lambek’s theorem says: in this special LEGO universe, your building and unbuilding functions (`j` and `m`) are perfect mirrors — so the instructions and the final build are one and the same.

Hope this also helps explain the use of these words:

| Word         | Greek Parts        | Meaning                       |
|--------------|--------------------|-------------------------------|
| **Isomorphism** | iso (equal) + morph (form) | Exactly same structure      |
| **Homomorphism** | homo (same) + morph (form) | Structure-respecting map    |


## What is a **catamorphism**?

A **catamorphism** is just a **fancy word for a fold**. It means: "Take a recursive thing (like a list or expression), and **reduce** it to a value by combining its parts."


### 🧠 Example:

- A list `[1, 2, 3]`
- Fold with `+`: `1 + 2 + 3 = 6`

That’s a catamorphism.

In Haskell:
```haskell
foldr (+) 0 [1, 2, 3]
```

Or for expressions:
```haskell
foldExpr evalAlg expr
```

---

# Sources
- https://ctfpis.gitbook.io/project/category-theory-for-programmers/part_three/f-algebras

<hr>

Related to: [f-algebra](f-algebra)