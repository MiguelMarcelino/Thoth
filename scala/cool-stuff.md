# Cool Scala stuff
This note contains a list of really cool stuff I might waht to use in the future. Here we gooooooo.

* Anonymous functions can be done with the following syntax: `(x: Int, y: Int) => x + y`
* Although it is not very common, you can indeed do loops in Scala:
```Scala
// Similar to for each in Java
for (arg <- args) 
	println(arg)

// With a range
for (i <- 0 to 2) 
	print(greetStrings(i))
```
* List concatenation has its own syntax
```Scala
List("a", "b") ::: List("c", "d") // concatenates both lists
val thrill = "Will" :: "fill" :: "until" :: Nil // New list with elements: ["Will", "fill", "until"]
```
* sss


---

## Sources
* The main source is the Book *"Programming in Scala"* by Martin Odersky

---

Related to: [scala](scala)