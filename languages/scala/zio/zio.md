# ZIO

- `ZIO[R, E, A]` is an immutable value that lazily describes a workflow or job. 
    - `R` - Environment Type. If this type parameter is Any, it means the effect has no requirements, because we can run the effect with any value (for example, the unit value ()).
    - `E` - Failure Type. The error type the effect might fail with.
    - `A` - Success Type. The type that the effect returns if it succeeds.
- A value of type `ZIO[R, E, A]` is like an effectful version of the following function type: `R => Either[E, A]`
- Three important properties of ZIO
    - ZIO values are immutable, and all ZIO functions produce new ZIO values
    - ZIO values don't do anything. They just wrap effectful computations
    - ZIO values can be interpreted by the ZIO runtime into effectful interactions with the external world
    

## Converting side effects
- ZIO can convert both synchronous and asynchronous side-effects into ZIO effects (pure values).
    - `ZIO.succeed`: Imports a total synchronous effect
    - `IO.attempt`: Imports a (partial) synchronous side-effect (When we are not sure whether a computation can produce side-effects)

### Blocking synchronous side-effects
By default, all effects will be executed on a default primary thread pool. Running blocking computations on a primary threadpool can quickly starve our resources. Therefore, ZIO has a separate blocking thread pool specially designed for Blocking I/O and, also CPU Work workloads.

- `ZIO.blocking`: Takes a ZIO effect and returns another effect that is going to run on a blocking thread pool.
- `ZIO.attemptBlocking`: Converts a blocking side-effect into a ZIO effect.
- `ZIO.attemptBlockingInterrupt`: Converts blocking side effects that can be interrupted by Thread.interrupt.
- `ZIO.attemptBlockingCancelable`: Converts blocking side-effects that can only be interrupted by invoking a cancellation effect.
- `ZIO.attemptBlockingIO`: ???

## Acquire Release
- The most typical use-case for try / finally is to properly release resources.
- ZIO encapsulates this common pattern with `ZIO#acquireRelease`, where we must specify
    - An acquire effect, which acquires a resource
    - A release effect, which releases it
    - A use effect, which uses the resource

## ZIO Aspect
- Two types of concerns when developing our application
    - Core concerns: 
        - Concerned with what we are doing
    - Cross-cutting concerns: 
        - Shared among different parts of our application.
        - Concerned with how we are doing something than what we are doing
        - Examples: Downloading files sequentially or in parallel, Logging and monitoring the download process, Retrying and timing out the download process
        - This does not affect the return type, but it affects how the program will behave
- The ZIO effect has a data type called `ZIOAspect`
    - Modifies a ZIO effect and converts it into a specialized ZIO effect

As an example, we can consider the following code:

```Scala
import zio._

val myApp: ZIO[Any, Throwable, String] =
  ZIO.attempt("Hello!") @@ ZIOAspect.debug
```

The debugging that was added to the function does not change its return type, but adds a new debugging aspect to it.

## ZIO Type Aliases

### UIO
- `UIO[A]` is a type alias for `ZIO[Any, Nothing, A]`.
- Represents an Unexceptional effect that doesn't require any specific environment, and cannot fail, but can succeed with an A.

### URIO
- `URIO[R, A]` is a type alias for `ZIO[R, Nothing, A]`
- It represents an effect that requires an `R`, and cannot fail, but can succeed with an `A`.

### Task
- `Task[A]` is a type alias for `ZIO[Any, Throwable, A]`
- It represents an effect that has no requirements, and may fail with a `Throwable` value, or succeed with an `A`.
- This is a useful type alias when converting from Future or from IO, as it is an effect that can fail with a throwable and does not require defining any requirements.


### RIO
- `RIO[R, A]` is a type alias for `ZIO[R, Throwable, A]`
- It represents an effect that requires an `R`, and may fail with a `Throwable` value, or succeed with an `A`.

### IO
- `IO[E, A]` is a type alias for `ZIO[Any, E, A]`
- It represents an effect that has no requirements, and may fail with an `E`, or succeed with an `A`.

## Runtime
- A `Runtime[R]` is capable of executing tasks within an environment `R`
- To run an effect, we need a Runtime, which is capable of executing effects
- Runtimes bundle a __thread pool__ together with the __environment__ that effects need
    - Writing a ZIO program is creating ZIO effects with ZIO constructurs
    - A ZIO effect is a blueprint (tree data structure) that describes the execution of a program.
    - The data structure doesn't do anything, it just describes the concurrent program
    - Running `unsafe.run` is what triggers the ZIO Runtime System to execute all the instructions
        - This is an evaluation that happens "at the end of the world"

### Responsibilities of the runtime
- Execute the steps of the blueprint
- Handle unexpected errors
- Spawn concurrent fibers
- Cooperatively yield to other fibers
- Capture execution and stack traces
- Ensure finalizers are run appropriately
- Handle asynchronous callbacks

## Sources
* The main source is the official documentation

---

Related to: [scala](scala)