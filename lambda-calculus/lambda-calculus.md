# Lambda Calculus

## Introduction
- Works with applications of functions to arguments
- Example
	- Consider the following polinomial: `x^2−2⋅x+5`
	- In lambda calculus, one would represent it as follows: `λx[x^2−2⋅x+5]`
	- The λ operator allows us to abstract over x (it binds the variable to the expression)
- Central principle of lambda calculus is 𝛽-reduction (or 𝛽-conversion). 
	- `(λx[M])N⊳M[x:=N]`
	- We can reduce an application of an abstract term by replacing all instaces of x by N inside M.
	- This reduction is also one of the principles of functional programming. In essence, the abstraction over a given variable can be achieved through functions. As an example consider the following piece of code: `val a = {println(42); 42}`. Replacing a with the value 42 would not yield the same result, as it has the side-effect of printing the number 42 to stdout. Therefore, this is not a pure expression, as it has side-effects and cannot be replaced by its return value.
- Set theory vs. Lambda calculus
	- In set theory, a function is an argument-value pair, meaning: `(x,y)∈𝑓 and (x,z)∈f implies y=z`
		- The function f assigns the value y to the argument x
		- Two functions are identical iff they assign the same values to the same arguments
		- In essence: Functions-as-sets are extensional objects
	- Lambda calculus follows the principle of functions-as-rules
		- A function is given by a rule for how to determine its values from its arguments
		- For instance, the term `λx[M]` can be seen a function that, given 𝑥, produces M.
		- Given rules M and N, we cannot know whether `λx[M]` is equal to `λx[N]`. In other words, functions-as-rules are non-extensional objects (also known as intensional).
	- (In the present possible-worlds terminology, function concepts are classified as extensional or intensional based of their behaviour at possible-worlds. See more info about possible-worlds semantics the [source]( https://plato.stanford.edu/entries/lambda-calculus/))
- *hyperintensional*: A function concept that allows for intensionally equivalent functions to be distinct
	- The point is that in possible-worlds terminology, the function concept at work in the λ-calculus may be regarded not as intentional but *hyperintensional*.
	- As an example, consider the following example:
		- We have the following functions:
			- `ADD-ONE:=λx[x+1]` 
			- `ADD-TWO-SUBTRACT-ONE:=λx[[x+2]−1]`
		- The functions are extensionally equivalent: they assign the same value to the same input at the actual world
		- They are also intentionally equivalent, if we consider that the mathematical facts are the same in every possible world.

## Syntax

<u>Definition</u>
For the alphabet of the language of the λ-calculus we take the left and right parentheses, left and right square brackets, the symbol λ, and an infinite set of variables. The class of λ-terms is defined inductively as follows:
1. Every variable is a λ-term.
2. If M and N are λ-terms, then so is (MN).
3. If M is a λ-term and x is a variable, then `(λx[M])` is a λ-term.
By *term* we always mean λ-term. Terms formed according to rule (2) are called **_application terms_**. Terms formed according to rule (3) are called **_abstraction terms_**.


<u>Definition</u>
The syntactic functions FV and BV (for ‘free variable’ and ‘bound variable’, respectively) are defined on the set of λ𝜆-terms by structural induction thus:

For every variable x𝑥, term M, and term N:

|     | Free                     | Bound                    |
| --- | ------------------------ | ------------------------ |
| 1   | `FV(x)= {x}`             | `BV(x)= ∅`               |
| 2   | `FV(MN)= FV(M) ∪ FV(N)`  | `BV(MN)= BV(M) ∪ BV(N)`  |
| 3   | `FV(λx[M])= FV(M) − {x}` | `BV(λx[M])= BV(M) ∪ {x}` |

If `FV(M)=∅` then M is called a **_combinator_**.


<u>Definition (substitution)</u> 
We write `M[x:=N]` to denote the substitution of N for the free occurrences of x in M. A precise definition by recursion on the set of λ-terms is as follows: for all terms A, B, and M, and for all variables x and y, we define:
1. `x[x:=M] ≡ M` - Replacing the variable with something else will return the newly replaced value
2. `y[x:=M] ≡ y` (y distinct from x) - Nothing happens to y when we replace x (when both variables are different)
3. `(AB)[x:=M] ≡ A[x:=M]B[x:=M]` - Substitution is applied to all terms equally
4. `(λx[A])[x:=M] ≡ λx[A]` - If the bound variable is identical to the variable we are trying to substitute, then we do not perform any substitution. The variable x does not occur freely, so there is nothing to do.
5. `(λy[A])[x:=M] ≡ λy[A[x:=M]]` (y distinct from x) - This is an extension of the previous case, but where x occurs freely and y is a bound variable (x != y). Therefore, we replace all occurrences of x with M in the term A.

<u>Definition (change of bound variables, α-convertibility). </u>
The term N is obtained from the term M by a **_change of bound variables_** if, roughly, any abstraction term `λx[A]` inside M has been replaced by `λy[A[x:=y]]`.

Let us say that terms M and N are α-convertible if there is a sequence of changes of bound variables starting from M and ending at N.

<u>Axiom - β-conversion</u>
`(λx[M])N ⊳ 𝑀[𝑥:=𝑁]`, provided no variable that occurs free in N becomes bound after its substitution into M.

Example of α-convertibility and β-conversion
Let us consider the function: `λx[λy[x(y−5)]]`
If we wanted to apply the argument `2y` to this function, we couldn't, as that would violate the rule for β-conversion (y would become a bound variable, when it occurs free in N). Therefore, the following conversion would be illegal:
- `(λx[λy[x(y−5)]])2y ⊳ λy[2y(y−5)]`

Therefore, we have to apply α-convertibility and change the bound variable y. We could therefore do the following and replace y for z:
- `λx[λz[x(z−5)]]`

After applying α-convertibility, we can now apply β-conversion. This gives us the following valid conversion:
- `(λx[λz[x(z−5)]])2y ⊳ λz[2y(z−5)]`


## Combinators
A combinator is a λ-term with no free variables. There are many combinators that have proven useful in lambda calculus. Below are some of the most relevant ones.

| Name | Definition                                       | Comments                                                                                                                                                                                                                                                    |
| ---- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S    | `λx[λy[λz[xz(yz)]]]`                             | Substitute-and-apply operator. z ‘intervenes’ between x and y: instead of applying x to y, we apply xz to yz.                                                                                                                                               |
| K    | `λx[λy[x]]`                                      | Constant function. The value of KM is the constant function whose value for any argument is simply M.                                                                                                                                                       |
| I    | `λx[x]`                                          | The identity function (returns whatever value is provided)                                                                                                                                                                                                  |
| B    | `λx[λy[λz[x(yz)]]]`                              | Recall that ‘xyz𝑥𝑦𝑧’ is to be understood as (xy)z(𝑥𝑦)𝑧, so this combinator is not a trivial identity function.                                                                                                                                        |
| C    | `λx[λy[λz[xzy]]]`                                | Swaps an argument                                                                                                                                                                                                                                           |
| T    | `λx[λy[x]]`                                      | Truth value `true` (Identical to K)                                                                                                                                                                                                                         |
| F    | `λx[λy[y]]`                                      | Truth value `false`                                                                                                                                                                                                                                         |
| ω    | `λx[xx]`                                         | Self-application combinator                                                                                                                                                                                                                                 |
| Ω    | ωω (`λx[xx]λx[xx]`)                              | Self-application of the self-application combinator. Reduces to itself.<br>This is how recursion is defined. When passing `λx[xx]` to itself, it will apply that function twice. Since `x = λx[xx]`, we are essentially always repeating the term `λx[xx]`. |
| Y    | `λf[(λx[f(xx)])(λx[f(xx)]𝜆𝑓[(𝜆𝑥[𝑓(𝑥𝑥)])]` | The y combinator.  For every λ𝜆-term X𝑋, we have:<br>YX ⊳ `(λx[X(xx)])(λx[X(xx)])`<br>      ⊳ `X((λx[X(xx)])(λx[X(xx)])`<br><br>The terms YX and X(YX) reduce to a common term.                                                                           |
| Θ    | `(λx[λf[f(xxf)]])(λx[λf[f(xxf)]]`                | Turing’s fixed-point combinator. For every λ-term X, ΘX reduces to X(ΘX)                                                                                                                                                                                    |

### Notations

| Name      | Application                                                                                                                                                                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MN`      | The application of the function M𝑀 to the argument N𝑁.                                                                                                                                                                                                                      |
| `PQR`     | The application of the function PQ, which is itself the application of the function P to the argument Q, to R. The disambiguation rule allows us to read this term as follows: (PQ)R                                                                                          |
| `(λx[M])` | The λ term that binds the variable x in the body term M.<br>Some authors write `λx.M` or `λx⋅M`                                                                                                                                                                               |
| `M[x:=A]` | The λ-term that is obtained by substituting the λ-term A for all free occurrences of x inside M.<br>For example, suppose M is `λx[x+y]`, and A is z. When we perform the substitution `M[x:=A]`, we replace all occurrences of x with A, so `M[x:=A]` would become `λx[z+y]`. |
| M≡N       | The λ𝜆-terms M and N are identical: understood as sequences of symbols, M and N have the same length and corresponding symbols of the sequences are identical.                                                                                                               |


---
# Sources
- https://plato.stanford.edu/entries/lambda-calculus/