# Concurrency

## Threads
### Threading on JVM
- Threading in JVM maps 1:1 to the operating system's native threads
- Only one thread can be executed on a core at each time
- Running too many JVM threads can cause too many context switches.
	- Creating a thread and possible context switches can have higher cost than the task itself

### Thread Pools
- Consists of a work queue and a pool of running threads.
- Every task (in Java, it is an instance of `Runnable`) to execute is placed in the work queue
	- Scala avoids working with `Runnable`. Abstractions, such as `Future` and `IO` do that under the hood
- Thread pools can re-use and cache threads
	- Avoids the context-switching overhead

There are two main types of thread pools:
- Bounded
	- Limits number of available threads to a fixed amount
	- This can be useful to limit the number of threads to the number of CPUs in the machine
- Unbounded
	- No thread limit is imposed
	- This could make the system run out of memory
	- Cached thread pools allow us to re-use threads


### Blocking Threads
- In general, we should never block threads. However, we might have to work with an interface that does it.
- `Blocker[IO]` can be used to safely handle blocking operations in an explicit way.

```scala
import cats.effect.{Blocker, ContextShift, IO}
import scala.concurrent.ExecutionContext

implicit val contextShift: ContextShift[IO] = 
	IO.contextShift(ExecutionContext.global)

def blockingOp: IO[Unit] = IO(/* blocking op*/ ())
def doSth(): IO[Unit] = IO(/* do something */ ())

val prog = Blocker[IO].use { blocker =>
  for {
    _ <- blocker.blockOn(blockingOp) // executes on blocker, backed by cached thread pool
    _ <- doSth()                     // executes on contextShift
  } yield ()
}
```

### Green Threads
- Green threads are not scheduled on an OS level
- They are lightweight threads. 
	- We can create many green threads without the issues of OS-level threads
- Characterized by cooperative multitasking
	- Thread decides when it gives up control instead of being forcefully pre-empted like JVM threads.
- `Fiber` and `shift` have a lot of similarities with this model

### Thread Scheduling
- `IO.shift` shifts a computation to a different thread pool
	- It introduces an asynchronous boundary
- Thread pools are in charge of scheduling threads
	- If there is one thread running, it won't change until it terminates or a higher priority thread is ready to start doing work
- IO executes synchronously until `IO.shift` or a function like `parSequence` is called.
	- IO's can be treated like green threads
	- Calling `IO.shift` schedules the work again, so other pending IO's have their chance of running.
- When `IO.shift` is called, the following happens:
	- Fiber is removed from its current thread and put in the pool of pending fibers.
	- For each available thread, assign it one of the pending fibers from the pool (allows for fairness).


#### Examples

To demonstrate the effects of execution contexts in Scala, lets create two single-threaded execution contexts and a function that will run an IO forever.

```scala
import java.util.concurrent.Executors
import cats.effect.{ContextShift, Fiber, IO}
import scala.concurrent.ExecutionContext

val ecOne = ExecutionContext.fromExecutor(Executors.newSingleThreadExecutor())
val ecTwo = ExecutionContext.fromExecutor(Executors.newSingleThreadExecutor())

val csOne: ContextShift[IO] = IO.contextShift(ecOne)
val csTwo: ContextShift[IO] = IO.contextShift(ecTwo)

def infiniteIO(id: Int)(cs: ContextShift[IO]): IO[Fiber[IO, Unit]] = {
  def repeat: IO[Unit] = IO(println(id)).flatMap(_ => repeat)

  repeat.start(cs)
}
```

The function `infiniteIO` runs the IO computation in the background on the provided thread pool. Lets try to run the code above using only the first execution context:

```scala
val prog =
  for {
    _ <- infiniteIO(1)(csOne)
    _ <- infiniteIO(11)(csOne)
    _ <- infiniteIO(2)(csTwo)
    _ <- infiniteIO(22)(csTwo)
  } yield ()

prog.unsafeRunSync()
```

This computation will never print `11` nor `22`, as it is waiting for the first computation to finish. Since we are dealing with single thread pools, the second task will end up never getting scheduled.
Lets now change the `repeat` function in `infiniteIO` to use `IO.shift`.

```scala
def infiniteIO(id: Int)(implicit cs: ContextShift[IO]): IO[Fiber[IO, Unit]] = {
  def repeat: IO[Unit] = IO(println(id)).flatMap(_ => IO.shift *> repeat)

  repeat.start
}
```

By calling `*>` we execute the first operation, ignore its result, and then call `repeat`. This implies we will now be able to see all the numbers being printed on the screen. `IO.shift` essentially allowed the currently running IO to be rescheduled, giving the opportunity to execute the other one.

### Asynchronous / Semantic blocking
- This is different from blocking a thread
- It means we suspend an IO/Task waiting for some action to happen (e.g. `Deferred.get`) without blocking threads
- Other IO's are free to execute on the thread while another IO is suspended.

