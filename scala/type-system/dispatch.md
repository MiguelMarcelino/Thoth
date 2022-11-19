#scala/type-system

# Dispatch

## Dispatch overview
A generic overview of dispatch:

![[dispatch.png]]

## Dispatch in Scala

As the JVM supports single dispatch, Scala is limited to this as well.
The example below is from the Scala [forum](https://users.scala-lang.org/t/dynamic-dispatch-on-object-but-static-dispatch-on-arguments-sometimes/5350) and displays the limitations of Scala.

```
class X {
  def m(x:X):Int = 1
}
class Y extends X {
  override def m(x:X):Int = 2
  def m(y:Y):Int = 3
}

val x:X = new X
val y:Y = new Y
val z:X = new Y
List(
  List(x.m(x), // 1
       x.m(y), // 1
       x.m(z)),  // 1
  List(
    y.m(x),  // 2
    y.m(y),  // 3 
    y.m(z)),  // 2, in CLOS this would be 3
  List(
    z.m(x), // 2
    z.m(y), // 2 --  Notice that y.m(y) returns 3, but this returns 2
    z.m(z))) // 2 
```



<hr>

## Sources
* https://www.youtube.com/watch?v=kc9HwsxE1OY
* https://docs.scala-lang.org/overviews/compiler-options/optimizer.html#motivation (only contains a partial description)
* https://users.scala-lang.org/t/dynamic-dispatch-on-object-but-static-dispatch-on-arguments-sometimes/5350