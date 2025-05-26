# Java Garbage Collector
Java's garbage collector was one of its major advantages when the language was first released. Automated memory management set Java apart from other popular languages of the time, like C, which required manual memory handling. 
Although garbage collection is an automatic process, it is still interesting to study how Java manages the heap space and how it deals with dead (also known as unreferenced) objects. In this blog post, I will provide a high-level view of the Java Garbage Collector and its underlying infrastructure> I will also touch on the history of this technology and how it changed throughout the years.
This Article References Oracles Official Website on the Java Garbage collector. All sources are available at the end of the blog post.

## How does it work
The garbage collection process consists of two phases:
- A marking phase, which marks all the unreferenced objects. This is done with a single pass over some area of the memory address space, not necessarily covering the entire heap space
- A deleting phase, which deletes all the marked objects. 
Deleting can further be divided in two steps:
- _Normal Deletion_ frees up memory by deleting objects, but it can leave memory fragmented. This fragmentation may slow down future allocations, especially for large objects that require contiguous memory space. 
- _Compaction_ follows up on the first deletion step and copies the objects to new positions in the heap to ensure contiguous memory allocation, making sure to also update all references pointing to them.
But how does the JVM determine which objects are still reachable? It maintains a root set - a collection of root references that may link to other objects, forming a reference graph. A trace function is used to check if an object is accessible from the root set. If an object can be reached, it remains in memory; if not, it is safe to delete.
Although compaction is more efficient than just freeing up memory, it is also more costly. Running such an algorithm over the entire heap space would be unfeasible. This is why Java creates several divisions for its heap space. These are distinguished by the age of the objects they hold. In the next section, we will go over the details of this implementation.

![[global_heap.png]]

## Generational Garbage Collection
To maintain efficiency, Java’s garbage collector will divide the heap space based on object lifespans. The heap is split into several generations: A Young Generation, a Tenured Generation, and a Permanent Generation. Below is an image that allows us to visualize this partitioning.

![[hotspot_heap.png]]

The Young Generation is further divided into three sections: the Eden space, where newly created objects reside, and two survivor spaces. The garbage collection in the young generation is triggered when this space gets filled up. In this step, references objects can age once they surpass a certain threshold. Garbage collection in the younger generations occurs frequently and is considered a 'Stop-the-World' event, meaning all other JVM threads are paused during the process.
Such 'Stop-the-World' events need to be kept to a minimum, as they affect application performance. As such, a new mechanism called the Z Garbage collector was developed to reduce the time of such events. It guarantees that the clean-up process does not exceed 10 milliseconds. The number of concurrent threads to be used is decided by a heuristic, although this can be set manually.

## Handle Pool
Another key concept is the Handle Pool, where each object points to an entry containing its memory reference. This is useful during compaction, as objects may need to be moved, causing their memory locations to change. Instead of having to change all references to each object, the algorithm simply needs to update the references in the handle pool. While this is useful and saves time when changing objects references, it adds another level of indirection in every memory access made to an object's contents.
## Conclusion
This has been a simple overview of the Java Garbage collector, where we have discussed the basics of the Garbage collection process, including Generational Garbage collection and the concept of a Handle Pool.
## Sources
- Java Garbage Collection Basics: https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html
- JVM Garbage Collectors: https://www.baeldung.com/jvm-garbage-collectors
- Visual VM: https://visualvm.github.io/
- G1 Garbage collector: https://docs.oracle.com/javase/9/gctuning/garbage-first-garbage-collector.htm#JSGCT-GUID-ED3AB6D3-FD9B-4447-9EDF-983ED2F7A573
- The Z Garbage Collector: https://docs.oracle.com/en/java/javase/15/gctuning/z-garbage-collector.html#GUID-9957D441-A99A-4CF5-9522-393E6DE7D898
- An Introduction to ZGC: https://www.baeldung.com/jvm-zgc-garbage-collector
- Smith, J. E., & Ravi Nair. (2005). Virtual machines: versatile platforms for systems and processes. Morgan Kaufmann Publishers.

<hr>

Related to: [java](java)