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
* Classes and singleton objects
	* When a singleton object shares the same name with a class, it is called that class’s **companion object**. 
	* You must define both the class and its companion object in the same source file. 
	* The class is called the companion class of the singleton object
	* A class and its companion object can access each other’s private members.
	* An image to help you rember what *companion* means:
		* <img src="https://www.akc.org/wp-content/uploads/2017/11/Portuguese-Podengo-standing-in-three-quarter-view.jpg" width="30%">
* Au contraire to Java, in Scala one can create an application's entry point with a singletone object that has a `main` method inside:
```Scala
object Something { 
	def main(args: Array[String]) { 
		// Do something
	} 
}
```
* An excerpt talking about operator methods and implicits that I found very important: 
	* "If used unartfully, both operator methods and implicit conversions can give rise to client code that is hard to read and understand. Because implicit conversions are applied implicitly by the compiler, not explicitly written down in the source code, it can be non-obvious to client programmers what implicit conversions are being applied. And although operator methods will usually make client code more concise, they will only make it more readable to the extent client programmers will be able to recognize and remember the meaning of each operator. 
	  The goal you should keep in mind as you design libraries is not merely enabling concise client code, but readable, understandable client code. Conciseness will often be a big part of that readability, but you can take conciseness too far. By designing libraries that enable tastefully concise and at the same time understandable client code, you can help those client programmers work productively."


---

## Sources
* The main source is the Book *"Programming in Scala"* by Martin Odersky

---

Related to: [scala](scala)