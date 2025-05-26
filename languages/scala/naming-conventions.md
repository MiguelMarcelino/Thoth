# Naming Conventions
There are some recommended naming conventions for the Scala language. These are the following:

| type                            | style                                     | example             |
| ------------------------------- | ----------------------------------------- | ------------------- |
| Classes                         | Upper cammel-case                         | `class MyFairLady`      |
| Objects                         | Upper cammel-case                         | `object ast {...}`      |
| Packages                        | lower case sepparated by dots (à la Java) | `package com.novell`    |
| Methods                         | lower camel-case                          | `myFairMethod`         |
| Constants, Values and Variables | upper camel-case                          | `object Container {...}` |
| Type Parameters (generics)      | single upper-case letter                  | `class List[A]`         |
| Annotations                     | lower camel-case                          | `@volatile`             |

Define local short names. This would be a bad practice in Java, but is a good practice in Scala. This convention works because properly-written Scala methods are quite short, only spanning a single expression and rarely going beyond a few lines.

---

## Sources
* https://docs.scala-lang.org/style/naming-conventions.html

---

Related to: [scala](scala)