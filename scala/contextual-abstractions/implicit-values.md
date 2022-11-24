# Implicit Values
* A method can have _contextual parameters_, also called _implicit parameters_, or more concisely _implicits_.
* Parameter lists starting with the keyword `using` (or `implicit` in Scala 2) mark contextual parameters.

Examples:
```scala
// in a library
class Prefixer(val prefix: String)
def addPrefix(s: String)(implicit p: Prefixer) = p.prefix + s

// in your application
implicit val myImplicitPrefixer = new Prefixer("***")
addPrefix("abc")  // returns "***abc"
```

---

## Sources
* https://docs.scala-lang.org/tour/implicit-parameters.html
* https://stackoverflow.com/questions/10375633/understanding-implicit-in-scala
----

Related to: [[scala/scala-basics/contextual-abstractions]]