# Groups and F-Algebra

The structure of a **group** can be captured using the F-algebra formulation and how this method generalizes to other algebraic structures like rings.

## Definition of Group
A **group** is a mathematical structure that consists of:
1. A **binary operation** (`m × m → m`) – e.g., addition for integers.
2. A **unary operation** (`m → m`) – e.g., negation (inverse).
3. A **nullary operation** (`1 → m`) – e.g., identity element (zero for addition).

Traditionally, a group is defined by these three separate operations. Using **category theory**, we can combine these into one operation that takes an input from the disjoint union (`+`) of these types and produces an output of type `m`:

```
m × m + m + 1 = m
```

This means that instead of thinking of separate functions, we encapsulate everything into a **single algebraic structure**.

---

## Generalizing to a Ring
A **ring** extends a group by adding:
1. **One more binary operation** (multiplication: `m × m → m`).
2. **One more nullary operation** (multiplicative identity: `1 → m`).

Following the same pattern, we can describe a ring using a single function:

```
m × m + m × m + m + 1 + 1 = m
```

This captures:
- Two binary operations (`m × m` for addition and multiplication).
- One unary operation (`m → m` for negation).
- Two nullary operations (`1 → m` for both additive and multiplicative identity).

I actually find it easier to understand the haskell way:

```Haskell
data RingF a
  = Add a a   -- Addition: m × m → m
  | Mul a a   -- Multiplication: m × m → m
  | Neg a     -- Negation: m → m
  | Zero      -- Additive identity: 1 → m
  | One       -- Multiplicative identity: 1 → m
  deriving (Functor, Show)
```

Using the example from the article makes this even clearer. An example of a ring is the set of integers. We can choose Integer as the carrier type and define the evaluation function as:

```
evalZ :: **Algebra** RingF Integer
evalZ RZero      = 0
evalZ ROne       = 1
evalZ (RAdd m n) = m + n
evalZ (RMul m n) = m * n
evalZ (RNeg n)   = -n
```

## Tree data structure
If we go further, we end up with a tree structure.  The functor `RingF` is a structure with "holes" where it expects a type parameter `a`. Normally, we fill this hole with a concrete type (like `Int`), but instead, we can nest it within itself.

If we replace `a` with `Int`, we get non-recursive expressions.

```haskell
type RingF0 a = a  -- Just a simple type, no structure
```

But if we fill the type parameter a with RingF a, we start getting structure.

```
type RingF1 a = RingF (RingF a)
```

This means that instead of RingF Int, we now have RingF (RingF Int), where the first level of RingF operates on another RingF structure.

Let's say we have:

```haskell
Add (Mul 1 (-1)) 0
```

If we rewrite it explicitly:

```haskell
AddF (MulF One (NegF One)) ZeroF
```

Here, MulF One (NegF One) itself is another RingF, meaning we have a tree-like structure.
We can go on like this and define a Dept-2 tree. This then leads us to define a generalization

### Generalizing to Depth-n
We generalize this pattern:

```haskell
type RingFnPlus1 a = RingF (RingFn a)
```

This means every new level is constructed from the previous level. It creates an infinite tower of function applications. If we keep applying this infinitely, we reach a fixed point:

``` haskell
type Expr = Fix RingF
```

Here, `Expr` stops depending on `a`. This is because after infinite nesting, there's no more "hole" left to fill - `a` disappears entirely. We always end up at `Fix RingF`, no matter what we started with.

This works for the category Set (the category of all sets and functions), as it has a well-behaved notion of limits and recursion This means that the recursive construction always reaches a well-defined limit (our `Expr` type). In some other categories, this process might not converge nicely.


## Main Aspects of Groups
1. **Combining Operations**: Instead of treating operations separately, we package them into a single function signature.
2. **Generalization**: This approach works not just for groups but also for rings, fields, and other algebraic structures.
3. **They show the power of F-Algebras**: The left-hand side (input) represents a sum of different arities (binary, unary, nullary), while the right-hand side (output) is always `m`, making the definition uniform across structures.


---

# Sources
- https://ctfpis.gitbook.io/project/category-theory-for-programmers/part_three/f-algebras

<hr>

Related to: [f-algebra](f-algebra)