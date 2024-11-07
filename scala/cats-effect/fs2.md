# FS2 Streams
The FS2 library has two major capabilities:
- The ability to build arbitrarily complex streams, possibly with embedded effects
- The ability to transform one or more streams using a small but powerful set of operations
- A stream is like a logical thread of execution
	- Interleaving logical threads allows complex behaviour
	- Declarative and composable
- Streams are good for:
	- Data that is too big to fit into memory
	- Control flow that is too hard to fit into one's head

## Building streams

A stream is created as follows:
```scala
Stream[F, O]
```

It is evaluated as follows:
- `F` is the effect type. The stream requests an evaluation of `F` effects
- `O` is the output type. 
- A simple definition of a stream, is that it emits 0...n values of type `A`, where n can be infinite, while requesting effects in F.

Let's consider an example:
```scala
val s1 = Stream.emit(1)
```

This stream has the type `Stream[Pure, Int]`.
- The output is `Int`
- The effect type is `Pure`, which means it does not require the evaluation of any effects to produce its output.

This is called a pure stream, as it does not require the evaluation of any effects. But FS2 streams can also include the evaluation of effects:

```scala
import cats.effect.IO

val eff = Stream.eval(IO { println("BEING RUN!!"); 1 + 1 })
```

Now we have the effect type `IO`. Creating the `IO` in the example above has no side effects and `Stream.eval` doesn't do anything at creation time. It will only run once the stream is interpreted.
Calling `eval` produces a stream that evaluates the given effect, then emits the result. Any stream formed using eval is called *effectful* and can't be run using `toList` or `toVector`. Instead, we need to compile the stream first.

```scala
import cats.effect.unsafe.implicits.global

eff.compile.toVector.unsafeRunSync()
```

An important thing to notice here is that compilation does not perform any of the effects. For the case of the example shown here, nothing will get printed to the console. To run the streams for their effects, we need to use one of the `unsafe*` methods on `IO`.

> NOTE: This evaluation is typically marks the *end of the world*, meaning that we are no longer working with IOs after this scope. Once we evaluate the IO, we get the result of the effect encapsulated within an IO.

## Chunks
- FS2 streams are chunked internally for performance
	- A chunk is a strict, finite sequence of values that supports efficient indexed based lookup of elements
- `Stream.chunk` can be used to create an individual stream chunk

Example of building a stream chunk:
```scala
import fs2.Chunk

val s1c = Stream.chunk(Chunk.array(Array(1.0, 2.0, 3.0)))
```

## Error handling
Raising an error inside a stream can be done explicitly by using `Stream.raiseError`, or implicitly via an exception in pure code or inside an effect passed to `Stream.eval`.

```scala
val err = Stream.raiseError[IO](new Exception("oh noes!"))
// err: Stream[IO, Nothing] = Stream(..)
val err2 = Stream(1,2,3) ++ (throw new Exception("!@#$"))
// err2: Stream[[x]fs2.package.Pure[x], Int] = Stream(..)
val err3 = Stream.eval(IO(throw new Exception("error in effect!!!")))
// err3: Stream[IO, Nothing] = Stream(..)
```

To catch errors, we can use the `handleErrorWith` method. 

```scala
err
	.handleErrorWith { 
		e => Stream.emit(e.getMessage) 
	}
	.compile
	.toList
	.unsafeRunSync()
// res24: List[String] = List("oh noes!")
```

Note that even when using `handleErrorWith` (or attempt) ==the stream will be terminated after the error and no more values will be pulled==. In the following stream, the value `4` is never pulled:

```scala
val err4 = Stream(1,2,3).covary[IO] ++
  Stream.raiseError[IO](new Exception("bad things!")) ++
  Stream.eval(IO(4)) // value is never pulled

err4.handleErrorWith { _ => Stream(0) }.compile.toList.unsafeRunSync()
// res25: List[Int] = List(1, 2, 3, 0)
```


---
# Sources
- https://fs2.io/#/guide
- https://www.youtube.com/watch?v=YSN__0VEsaw

<hr>

Related to: [cats-effect](cats-effect)
