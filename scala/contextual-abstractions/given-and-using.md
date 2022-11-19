#scala/contextual-abstractions

# Given and Using
The following features are used for contextual abstraction:
* Given Instances define terms that can be used by the Scala compiler to fill in missing arguments
* Using Clauses specify parameters that can be ommited by the programmer at the call site and are automatically provided by the context

## Using clause

The `using` keyword allows the Scala compiler to perform *term inference*, which automatically finds the argument with the correct type.

Consider the following example from the documentation:
```
case class Config(port: Int, baseUrl: String)

def renderWebsite(path: String, c: Config): String =
    "<html>" + renderWidget(List("cart"), c)  + "</html>"

def renderWidget(items: List[String], c: Config): String = ???

val config = Config(8080, "docs.scala-lang.org")
renderWebsite("/home", config)
```

We can turn this into:
```
def renderWebsite(path: String)(using c: Config): String =
    "<html>" + renderWidget(List("cart")) + "</html>"

def renderWidget(items: List[String])(using c: Config): String = ???
```

Notice that the call to `List("cart")` now omits the parameter `c`, which is implicitly added by Scala.

## Given Instances

If there is a single canonical value for a particular type, then we use `given` instances
Consider the following example from the documentation:
```
val config = Config(8080, "docs.scala-lang.org")
given Config = config
```

The example above specifies that whenever we omit a value of type `Config`, the Scala compiler should infer `convig` as an argument.
We can now replace the last call from the first example from `renderWebsite("/home", config)` into `renderWebsite("/home")`, omiting the parameter `config`.￼## Dispatch overview


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/ca-given-using-clauses.html