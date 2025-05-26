# Methods

 Methods in Scala require the use of type hints (it is very hard to infer the types of functions)
* Methods can have parameters with default values
* Just like in Python, one can use named parameters without explicitly requiring any special syntax in the function definition.
	* This is epsecially useful if the calls are not clear, such as in `engage(true, true, true, false)`, where a programmer does not know what he is setting to `true` or `false`. 

Example of named parameters:
```
def sum(a:Int, b:Int) = a + b

# The following function calls all output the same result
sum(1, 2)
sum(a=1, 2)
sum(a=1, b=2)
sum(b=2, a=1)
```


<hr>

## Sources
- https://docs.scala-lang.org/scala3/book/taste-methods.html#inner-main

<hr>

Related to:
* [scala-basics](scala-basics.md)




