# Fiber

- Can be seen as a lightweight thread.
- Represents the pure result of an `Async` data type (e.g. `IO`).
- It can be joined or cancelled, just like a normal thread.

As an example, `IO.start` returns a Fiber

```scala
val io = IO(println("Hello!"))
val fiber: IO[Fiber[IO, Unit]] = io.start
```

The main advantage of fibers, is that a program can spawn thousands of them without incurring in the same problems as threads. This implies the following:
- Fibers will suspend themselves when they encounter an async node
	- In cats-effect 3, they are suspended every n `flatMap`s.
- Cats-effect provides semantic blocking over asynchronous operations
	- Operations, such as `IO.sleep`, are not blocking operations (although they feel like blocking operations.)
	- When something is Thread-blocking, it gets moved to another thread pool

## How Fibers work (by Fabio Labella)
### Layers
- fs2: Declarative, high level, safe concurrency
	- Many combinators and a concept of lifetime through Stream
- cats-effect typeclasses: Specification for low-level, foundation primitives
- cats-effect IO: Concrete implementation of the runtime system

### Asynchronicity and Concurrency

- Definition of Asynchronous process:
	- Asynchronous process: process that executes outside the programs main flow
	- Asynchronous process (cats definition): A process that continues its execution in a different place or time than the one it started in.
- Definition of Concurrency
	- A program structuring technique in which there are multiple logical threads of control whose effects are interleaved.
	
Threads are abstractions:
- A logical thread offers a synchronous interface to an asynchronous process.
- A thread's execution looks synchronous from a high-level perspective, but is asynchronous when looking at it from a lower-level (scheduling) perspective.
- Logical threads abstract async processes as synchronous sequences of discrete steps
	- In this context, "discrete step" refers to a distinct, individual action or unit of work within an asynchronous process.
	- Each discrete step can be thought of as a single logical operation that Cats Effect will run, often encapsulated in a data type (like `IO`)
- Blocking means suspending threads one layer down. Logical threads at that layer keep running.

Below is an image showing a the two views of a thread's execution. Notice how the thread execution is asynchronous when it is scheduled.

![asynchronous-thread-execution](resources/images/scala/asynchronous-thread-execution.png)

### Real World Concurrency
- Concurrency: Discrete steps get interleaved
- Parallelism: Discrete steps run simultaneously
- Parallelism and concurrency are independent of each other.

#### Layers
- OS Processes: M:N with processors. Own execution state, own memory space
- OS/JVM Threads: M:N with processes. Own execution state, shared memory space.
- Fibers: M:N with threads. Shared execution state, shared memory space.

#### Cost of Blocking
- JVM threads are a scarce resource
	- Blocking as JVM thread is not ideal if the intent is to scale out
	- We spend too much time on context switching
- Fibers aren't scarce
	- Blocking a Fiber does not block the underlying thread.
	- Blocking a fiber is called semantic blocking. 
		- A fiber is not blocked in the same way a thread is. Instead, fibers are just suspended.
		- We are not actually blocking the underlying thread.

#### Scheduling
- Preemptive: Scheduler suspends tasks
- Cooperative: Tasks suspend themselves.

An overview of the scheduler can be seen below.

![io-run-loop](resources/images/scala/io-run-loop.png)

IO has what is known as a run loop. Fibers cooperate by submitting request to the JVM Thread Pool and yielding back control. This allows an M:N cooperative scheduling (as there are more fibers than threads). 

### The IO API
- An IO produces one value, fails, or never terminates
- Referentially transparent (pure)
- Many algebras (Monad, Concurrent, ...)

We can divide IOs use-cases in three:
- FFI: Wrap side-effects into IO.
- Combinators: Build complex IOs by composing smaller ones.
	- E.g. `IO.pure`, `IO.sleep`, `IO.map`, `IO.flatMap`, 
- Runners: Translate IO to side-effects at the end of the world
	- `IO.run`, `IO.unsafeRunAsync`, `IO.unsafeRunSync`

### Async
The async function is as follows:

```scala
def async[A](k: (Either[Throwable, A] => Unit) => Unit): IO[A]
```

Key things about `async`
- It does not introduce asynchronicity on its own
- It takes an asynchronous process and exposes it as IO
- It builds on the idea of continuation
	- Instead of returning a result, we call the rest of the computation with it
	- In this case, `k` is a callback function. It is called by `async` when the computation completes.

Below is an overview of how fibers are created:

![[fibers-overview.png]]

As mentioned earlier, the first layer (above the dotted line) the execution looks synchronous, as it is just a sequence of `flatMap` operations. However, the real execution is completely asynchronous. As fibers are submitted to the execution context, the scheduler will split each one across multiple threads.

---

Sources:
- https://typelevel.org/cats-effect/docs/2.x/datatypes/fiber
- Good old Reddit: https://www.reddit.com/r/scala/comments/l46q83/fibers_in_cats_effect_an_explanation_of_the/
	- Related: https://systemfw.org/talks.html#scala-world-2019
	- Video: https://www.youtube.com/watch?v=x5_MmZVLiSM


<hr>

Related to: [cats-effect](cats-effect)
