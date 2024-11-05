# IO - Cats Effect

- A data type for encoding side effects as pure values, capable of expressing both synchronous and asynchronous computations
- A value of type `IO[A]` is a computation that performs effects before returning a value of type `A`.
	- IO values are pure, immutable and preserve referential transparency
	- Presents a description of a side-effectful computation
- IO can describe synchronous or asynchronous computations that
	- Yield exactly one result on evaluation
	- Can end in success or failure
		- `flatMap` chains are short-circuited when failures occur
	- Can be cancelled, but the user must provide cancelation logic
- ==Not all IO tasks are cancellable. Cancellation status is only checked after asynchronous boundaries==. See more about cancellation on the section about concurrency and cancellation below.


As an example, below is a program that is referentially transparent:
```scala
import cats.effect.IO

val ioa = IO { println("hey!") }

val program: IO[Unit] =
  for {
     _ <- ioa
     _ <- ioa
  } yield ()
```

Running the program outputs `hey!` twice.

## Referential Transparency and Lazy Evaluation

In comparison to Futures, IO preserves referential transparency and is lazily evaluated. IO yields more control over computations and is more predictable when compared to futures, as it is pure and lazily evaluated. 
As an example, consider two versions of the same program below:

| Version 1                                                                              | Version 2                                                                                           |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| <code>for {<br>  _ <- addToGauge(32)<br>  _ <- addToGauge(32)<br>} yield ()<br></code> | <code>val task = addToGauge(32)<br><br>for {<br>  _ <- task<br>  _ <- task<br>} yield ()<br></code> |


In IO, the behaviour is the same on both. However, with Futures, both programs output different results, as the result is not lazily evaluated.


## Describing Effects

### Pure Values
- Lifting pure values into IO can be done via `IO.pure`.
- `IO.pure` cannot suspend side effects, as it is eagerly evaluated. Don't do the following: `IO.pure(println("THIS IS WRONG!"))`
- `IO.unit` is an alias for `IO.pure(())`.

### Synchronous effects
Evaluates IO operations immediately, on the current thread and call-stack. One can use `IO.apply` or simply `IO` to evaluate values. For example, `IO(println("Hej!))` will evaluate the operation.

### Asynchronous effects

`IO.async` describes an asynchronous process that cannot be cancelled.
- It injects a callback that can be used to signal successful results (`Right(a)`) or failures (`Left(a)`)

`IO.cancelable` allows interrupting IO computations.
- It can possibly release acquired resources, useful in race conditions to prevent leaks.

`IO.never` represents a non-terminating IO and is equivalent to `IO.async(_ => ())`
- For example, doing `IO.race(lh, IO.never) <-> lh.map(Left(_))` ensures non-termination in race conditions

`IO.defer` is used to defer the execution of a computation, The following case would result in a stack overflow error, but with `IO.defer`, it uses IO's run-loop and takes up constant memory due to its lazy evaluation:
```scala
import cats.effect.IO

def fib(n: Int, a: Long, b: Long): IO[Long] =
  // Defers the evaluation, resulting in constant memory alocation
  IO.defer { 
    if (n > 0)
      fib(n - 1, b, a + b)
    else
      IO.pure(a)
  }
```

## Concurrency and Cancellation

There are two very important points to consider about IO's and cancellation.
#### 1. Not all IO tasks are cancellable.
Cancellation status is only checked after asynchronous boundaries. Cancellation can be achieved by:
- Using `IO.cancelable`, `IO.async`, `IO.asyncF`, or `IO.bracket`
- Using `IO.cancelBoundary` or `IO.shift`

> NOTE: `flatMap` chains are only cancellable only if the chain happens after an asynchronous boundary. After an asynchronous boundary, cancellation checks are performed on every N `flatMap`. The value of `N` is hardcoded to 512.

#### 2. `IO` tasks that are cancellable, usually become non-terminating on `cancel`
IO cancellation does not work like `Thread.interrupt` in Java, as that is inherently unsafe, unreliable and not portable 

Read more about cancellation on the [IO Cancellation](io-cancellation) document


### Markers

`IO.start` and `IO.cancel` are equivalent to doing a thread fork and interrupt operations. However, the IO operations return a Fiber, which is a lightweight thread that (similarly to normal threads) can be joined or interrupted.


`IO.runCancelable` & `IO.unsafeRunCancelable` allow us to interrupt tasks (in both safe and unsafe way).

`IO.uncancelable` returns an IO that cannot be cancelled. A good use-case for this is when we want to ensure that a computation is atomic, that is, either all of it executes, or none of it. Cancellable IO's are not atomic.
Below is an example:

```scala
import cats.effect.IO

import scala.concurrent.ExecutionContext
import scala.concurrent.duration._

// Needed for `sleep`
implicit val timer = IO.timer(ExecutionContext.global)

// Our reference from above
val io: IO[Unit] = IO.sleep(10.seconds) *> IO(println("Hello!"))

// This IO can't be canceled, even if we try
io.uncancelable
```


`IO.cancelBoundary` returns a cancellable boundary
- It is an IO task that check for the cancellation status of the run-lop
- It does not allow for the bind continuation to keep executing in case cancellation happened.
- `IO.cancelBoundary` is essentially lighter version of `IO.shift` without ability to shift into different thread pool. It is lighter in the sense that it will avoid doing logical fork.


---
# Sources
- https://typelevel.org/cats-effect/docs/2.x/datatypes/io


<hr>

Related to: [cats-effect](cats-effect)
