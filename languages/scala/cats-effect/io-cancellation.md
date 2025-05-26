# IO cancellation

A topic that keeps resurfacing is cancellation with IO's. IO will not use Java's `Thread.interrupt` to kill the underlying thread, as that is unsafe. There are some computations that are not cancellable and cannot be saved by IO. As an example, let us consider the code excerpt below, which stems from Scala's official documentation

```scala
import java.io._

import cats.effect.IO

import scala.concurrent.ExecutionContext
import scala.util.control.NonFatal

def unsafeFileToString(file: File) = {
  // Scala Docs: Freaking Java :-)
  // Me: You bet!
  val in = new BufferedReader(
    new InputStreamReader(new FileInputStream(file), "utf-8"))
  
  try {
    // Uninterruptible loop
    // This loop is not cancellable, as there is no way to 
    // safely kill this computation. And Thread.interrupt
    // is definitely not an option!
    val sb = new StringBuilder()
    var hasNext = true
    while (hasNext) {
      hasNext = false
      val line = in.readLine()
      if (line != null) {
        hasNext = true
        sb.append(line)
      }
    }
    sb.toString
  } finally {
    in.close()
  }
}

/**
 * A function that reads a file. It uses an unsafe function 
 * that is not cancellable.
 */
def readFile(file: File)(implicit ec: ExecutionContext) =
  IO.async[String] { cb =>
    ec.execute(() => {
      try {
        // Signal completion
        cb(Right(unsafeFileToString(file)))
      } catch {
        case NonFatal(e) =>
          cb(Left(e))
      }
    })
  }
```


This function is not cancellable. IO cannot cancel the loop in the `unsafeFileToString` function and using Java's `Thread.interrupt` is not safe. Even providing cancellation logic would not have an impact in such cases.
One way to go around this is to use something like an `AtomicBoolean` to stop the for loop upon cancellation. Below is an implementation using an `AtomicBoolean` (from Scala's Docs).

```scala
import java.io.File
import java.util.concurrent.atomic.AtomicBoolean

import cats.effect.IO

import scala.concurrent.ExecutionContext
import scala.io.Source
import scala.util.control.NonFatal

def unsafeFileToString(file: File, isActive: AtomicBoolean) = {
  val sc = new StringBuilder
  val linesIterator = Source.fromFile(file).getLines()
  var hasNext = true
  // Atomic Boolean stops the loop. The value is passed as an
  // argument to allow the calling function to control the 
  // loop's stopping condition.
  while (hasNext && isActive.get) {
    sc.append(linesIterator.next())
    hasNext = linesIterator.hasNext
  }
  sc.toString
}

def readFile(file: File)(implicit ec: ExecutionContext) =
  IO.cancelable[String] { cb =>
    val isActive = new AtomicBoolean(true)
    
    ec.execute(() => {
      try {
        // Signal completion
        cb(Right(unsafeFileToString(file, isActive)))
      } catch {
        case NonFatal(e) =>
          cb(Left(e))
      }
    })
 
    // On cancel, signal it
    IO(isActive.set(false)).void
  }
```

The `readFile` function can now successfully cancel the computation, as it has control over the while loop through the `isActive` variable. 


---
# Sources
- https://typelevel.org/cats-effect/docs/2.x/datatypes/io#building-cancelable-io-tasks


<hr>

Related to: [io](io)