# Lambek's Theorem
- As mentioned in [f-algebra](f-algebra), an **F-algebra** consists of a pair `(A, α)` where `A` is a type (called the carrier), and `α :: F(A) -> A` is a function (called the structure map or evaluator). 

- An initial Algebra is a special F-algebra `(i, j)` that has a unique homomorphism to any other F-algebra.

- Lambek’s Theorem says that in an initial algebra `(i, j)`, the structure map `j :: F(i) -> i` is actually an isomorphism, meaning `F i ≅ i` (`F i` is the same in structure `i`). So, the carrier `i` is a fixed point of the functor `F`.

## What’s a Fixed Point?

A **fixed point** of a functor `F` is a type `i` such that:
```haskell
F i ≅ i
```

In Haskell, this is exactly what `Fix` does:
```haskell
newtype Fix f = Fix (f (Fix f))
```

The **structure** of `Fix f` is literally saying: "`Fix f` is isomorphic to `f (Fix f)`".

- `Fix` acts like the `j :: F i -> i` (folding a structure into a single value)
- `unFix :: Fix f -> f (Fix f)` is the inverse (unfolding)

---

## The Story Step-by-Step

### **1. Assume the initial algebra exists:**
We have:
```haskell
j :: F i -> i
```

This is our **evaluator** for the initial algebra with carrier `i`.

### **2. Create another F-algebra:**
Let’s build another F-algebra where the **carrier is `F i`**.

We need an evaluator:
```haskell
F j :: F (F i) -> F i
```
This is done by applying the functor `F` to `j`.

So now we have another algebra:
```haskell
(F i, F j)
```

### **3. Use the universal property of initial algebra:**
By definition of initial algebra `(i, j)`, there is a **unique homomorphism**:
```haskell
m :: i -> F i
```
that maps `(i, j)` to `(F i, F j)`.

### **4. Show that `j` is also a homomorphism:**
We trivially get another diagram where `j :: F i -> i` is a homomorphism from `(F i, F j)` to `(i, j)`.

So:
- `m :: i -> F i`
- `j :: F i -> i`

Now we have:
- `j . m = id_i` (from initiality)
- `m . j = id_{F i}` (from commuting diagrams)

Together, these say:
```haskell
j and m are inverses ⇒ j is an isomorphism
```

So:
```haskell
F i ≅ i
```

## Explanation

`j` is the evaluator of the algebra while `m` is an homomorphism of that same structure,. So while `j` will fold the structure into a result, `m` will unfold it back into its structure (homomorphism preserves the structure). As per Lambek's theorem, the build (`m`) and unbuild functions (`f`) are exact mirrors. This is why we always get the same thing back when we fold and unfold these structures:
1. `j . m = id` — if you unfold and then fold, you get the same thing back.
2. `m . j = id` — if you fold and then unfold, you also get the same thing back.

So, going back and forth between `F i` and `i` gives you the original thing, untouched. This means that:
- You can move freely between `F i` and `i`.
- They contain the same information.
- They’re structurally the same, just seen from different angles.

That’s exactly what an isomorphism means: two things that are different in form but equal in structure.

Taking this to programming, this could be defined as a function that receives an object and outputs the same object with some of its fields changed. The structure would be the same, but the output and input objects would be different.


### Key Insight
This formalizes what we already see in Haskell:
```haskell
newtype Fix f = Fix (f (Fix f))

-- So:
Fix f ≅ f (Fix f)
```

- `Fix :: f (Fix f) -> Fix f` — corresponds to `j`
- `unFix :: Fix f -> f (Fix f)` — corresponds to `m`
- These are inverses.

Thus, **`Fix f` is the initial algebra of the functor `f`**, and **Lambek’s theorem tells us that the structure map `Fix` is an isomorphism**.

## 📌 Summary

| Concept               | Category Theory           | Haskell                    |
|------------------------|----------------------------|-----------------------------|
| Functor               | `F`                        | `f`                         |
| Initial Algebra       | `(i, j :: F i → i)`        | `Fix f = f (Fix f)`         |
| Structure Map         | `j`                        | `Fix` constructor           |
| Inverse of `j`        | `m :: i → F i`             | `unFix`                     |
| Lambek’s Theorem      | `F i ≅ i`                  | `Fix f ≅ f (Fix f)`         |


<hr>

# Sources
- https://ctfpis.gitbook.io/project/category-theory-for-programmers/part_three/f-algebras

<hr>

Related to: [f-algebra](f-algebra)