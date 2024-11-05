# Fiber

- Can be seen as a lightweight thread.
- Represents the pure result of an `Async` data type (e.g. `IO`).
- It can be joined or cancelled, just like a normal thread.

As an example, `IO.start` returns a Fiber

```scala
val io = IO(println("Hello!"))
val fiber: IO[Fiber[IO, Unit]] = io.start
```

The main advantage of fibers, is that a program can spawn thousands of fibers without incurring in the same problems as threads. This implies the following:
- Fibers will suspend themselves when they encounter an async node
	- In cats-effect 3, they are suspended every n `flatMap`s.
- Cats-effect provides semantic blocking over asynchronous operations
	- Operations, such as `IO.sleep`, are not blocking operations (although they feel like blocking operations.)
	- When something is Thread-blocking, it gets moved to another threadpool


TODO: Watch video

---

Sources:
- https://typelevel.org/cats-effect/docs/2.x/datatypes/fiber
- Good old Reddit: https://www.reddit.com/r/scala/comments/l46q83/fibers_in_cats_effect_an_explanation_of_the/
	- Related: https://systemfw.org/talks.html#scala-world-2019
	- Video: https://www.youtube.com/watch?v=x5_MmZVLiSM


<hr>

Related to: [cats-effect](cats-effect)
