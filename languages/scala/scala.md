# Scala Language

* Scala comes from the word *scalable*
* Combines Object-Oriented (OO) and Functional programming (FP/OOP fusion)
	* Functional
		* Functions are first-class values -> can be passed arround like any other object
	* Object Oriented
		* Every value is an instance of a class and every “operator” is a method.
		* Java distinction between primitive types and boxed types (e.g. int vs. Integer) isn’t present in Scala.
		* Boxing and unboxing is completely transparent to the user.
* Runs on the JVM, which brings many benefits
	* Scala code runs on the Java Virtual Machine (JVM), so you get all of its benefits:
	* Security
	* Performance
	* Memory management
	* Portability and platform independence
	* Benefit from existing Java and JVM libraries
* Everything in Scala is an expression
* Top level allows any expressions and statements. This is opposed to Java, which requires the contents of each file to be wrapped within a class.
* Statically Typed
	* Included Type inference mechanism, which reduces the amount of types necessary at compile-time
* Optimized for parallel operations
	* Partially inspired on Erlang (Built for scalable software)
* Can run in the browser using Scala.js
	* This offers an alternative to JavaScript, with the benefit of strong typing

## Compiler Optimizations
* When you compile your Scala code to Java bytecodes, the Scala compiler will use Java’s primitive types where possible to give you the performance benefits of the primitive types.