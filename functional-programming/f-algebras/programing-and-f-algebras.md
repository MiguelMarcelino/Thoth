# Tying F-Algebras to Programming

## 1. Data types are built from smaller parts
Like:
```haskell
data Expr = Add Expr Expr | Val Int
```
This is a **recursive structure**. It has expressions inside expressions.


## 2. We can break that down using functors
We define a shape:
```haskell
data ExprF a = AddF a a | ValF Int
```
This is the **pattern** of one layer of `Expr`. It has a hole (`a`) for the recursive part.


## 3. `Fix` glues the layers together
We write:
```haskell
type Expr = Fix ExprF
```
This says: keep nesting `ExprF` inside itself forever. That builds a full recursive type.


## 4. Lambek’s theorem says:
If we build this recursion the right way, we can always go **back and forth** between:
- a single layer: `ExprF Expr`
- and the full expression: `Expr`

In Haskell:
- `Fix` goes **from layer to full**.
- `unFix` goes **from full to layer**.

They are **perfect mirrors**.


## 5. Why it matters
Because this lets us:
- Write **generic recursion** (folds, interpreters)
- Build **safe, composable** programs
- Separate **structure** (`ExprF`) from **behavior** (how we fold it)

## In short:
We break things into pieces (`ExprF`), tie them back together (`Fix`), and get a powerful way to build and interpret programs. Lambek’s theorem tells us that this gluing is perfect.

---

## Examples

This example shows how this could all work with Haskell.


### 1. Define the **functor** (one layer of the expression):

```haskell
data ExprF a = ValF Int | AddF a a
  deriving Functor
```

This is **one level** of an expression — with a hole (`a`) for recursion.


### 2. Use `Fix` to build full recursive expressions:

```haskell
newtype Fix f = Fix (f (Fix f))

-- Smart constructors
val :: Int -> Fix ExprF
val n = Fix (ValF n)

add :: Fix ExprF -> Fix ExprF -> Fix ExprF
add x y = Fix (AddF x y)
```

Now we can build expressions like:

```haskell
expr :: Fix ExprF
expr = add (val 1) (add (val 2) (val 3))
```

Which represents: `1 + (2 + 3)`


### 3. Fold it (evaluate it):

```haskell
foldExpr :: (ExprF a -> a) -> Fix ExprF -> a
foldExpr alg (Fix f) = alg (fmap (foldExpr alg) f)

evalAlg :: ExprF Int -> Int
evalAlg (ValF n) = n
evalAlg (AddF x y) = x + y

evaluate :: Fix ExprF -> Int
evaluate = foldExpr evalAlg
```

Now:

```haskell
evaluate expr  -- => 6
```

#### How does fold work?
`foldExpr` is a function to evaluate or reduce a recursive expression. 

- It takes a recipe (ExprF a -> a) — how to evaluate one layer.
- It applies that recipe recursively to the full expression.

The definition is as follows:
```haskell
foldExpr alg (Fix f) = alg (fmap (foldExpr alg) f)
```
- `Fix f` is one layer of the structure.
- `fmap (foldExpr alg) f` means: "evaluate all the sub-parts first".
- Then `alg` combines them.

It basically translates to: Go to the leaves, evaluate up, one layer at a time.

##### Example with Addition
Addition of two values
```haskell
fmap (foldExpr evalAlg) (AddF (Fix (ValF 1)) (Fix (ValF 2))) =
```

Means
```
AddF (foldExpr evalAlg (Fix (ValF 1))) (foldExpr evalAlg (Fix (ValF 2)))
```

Evaluate both expressions:
```haskell
foldExpr evalAlg (Fix (ValF 1)) = evalAlg (ValF 1) = 1  
foldExpr evalAlg (Fix (ValF 2)) = evalAlg (ValF 2) = 2
```

So we end up with the following:
```
evalAlg (AddF 1 2) = 3
```

### What just happened?

- `ExprF` is one layer.
- `Fix ExprF` is the full recursive type.
- `evaluate` folds it using `evalAlg`.
- This is **how Lambek’s theorem** and **initial algebras** power real code.


<hr>

Related to: [f-algebra](f-algebra)