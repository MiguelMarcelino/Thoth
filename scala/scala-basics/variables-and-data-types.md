# Variables and Data Types
Scala has two types of variables:
* `val`: Creates an immutable variable
* `var`: Creates a mutable variable

### Type Inference
* If not explicitly provided, Scala will infer variable types. In simple assignments, this always works, but more complex assignments might require manual annotations.

### Data Types
* Scala has the following built-in data types: `Byte`, `Int`, `Long`, `Short`, `Double`, `Float`, `String`, `Char`
* It also supports arbitrary precision arithmetic through the types `BigInt` and `BigDecimal`
* All of these types are represented as objects in memory. It is not as in Java, where types are defined sepparate from boxed types.

### Extra
* Multiline strings are supported with 3 quotation marks `"""some string"""`
* String interpolation is supported as well with the syntax `"This is $interpolation"`, where variables are prefixed with `$`


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/taste-vars-data-types.html#inner-main

<hr>

Related to:
* [scala-basics](scala-basics.md)

