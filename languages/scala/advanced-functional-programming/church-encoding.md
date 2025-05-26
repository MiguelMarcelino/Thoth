# Church encoding

* Church encoding is a way to represent data structures using pure functions.
* It originates from lambda calculus, the mathematical foundation of functional programming.
* Instead of using concrete data (like integers or lists), you encode data as functions that describe their behavior.
* For example:

  * A boolean is a function:
    ```
    true = (x, y) => x 
    false = (x, y) => y
    ```
  * A number (e.g. 0, 1, 2...) is a function representing repeated application of a function.
  * A list is a function that takes a reducer and an initial value (like `fold`).


<hr>

Related to: [advanced-functional-programming](advanced-functional-programming)