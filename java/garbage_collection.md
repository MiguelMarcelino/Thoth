# The Java Garbage Collector
The Java garbage collector is one of the main advantages of Java, allowing for automated memory management in the JVM. This is one of its main differentiating factors when comparing it to low-level languages. Although this is an automated process, some people would still like to know the details about how it manages the heap space and how it deals with dead (also known as unreferenced) objects. This article is intended to give a high-level view of the Java Garbage Collector and its underlying infrastructure and also briefly touch on the history of this technology and changes throughout the years.
This Article References Oracles Official Website on the Java Garbage collector. I highly recommend you also read the official documentation if you intend to experiment with different versions of the Garbage collector yourself.

## Garbage Collector
The garbage collection process happens mainly in two phases: A Marking phase and a Deleting phase. (Oracle, 2016)
The marking phase marks all the unreferenced objects. This is done with a single pass over some area of the memory address space, not necessarily covering the entire heap space (more details on this later). 
The deleting phase deletes all the marked objects. Now deleting can be further divided in two steps: The so-called “Normal Deletion” as stated on Oracle's Official Website, will only delete the objects. This has the drawback of leaving the memory space fragmented, possibly hindering the performance of future memory allocations e.g imagine the case of having very large objects that need to be allocated with not enough contiguous space to allocate them. 
To solve this problem, the second Deletion approach is used, which takes advantage of Compaction. Compaction will copy the objects to new positions in the heap to ensure contiguous memory allocation, making sure to also update all references pointing to them.
But how does the JVM know that objects are unreachable? Is it through reference counting the same way it is done in Python? Actually, the JVM does not use reference counting. Instead, it keeps track of something called the root set, which starts with the set of root references which can then point to several more references, essentially building a graph (Smith & Ravi Nair, 2005). To know if an object is still traceable from the root set or if it has become detached, a trace function is used. If the object is reached from the root set, it is not deleted from the heap, otherwise, it is safe to be deleted.
Now, as mentioned previously, the most efficient way of using the memory space is by not leaving it fragmented. However, running a Compaction algorithm every time we run the Garbage collection algorithm over the entire heap would be very inefficient. This is why the heap space is divided into multiple spaces, distinguished by the “age” of the objects they hold. In the next section, we will go over the details of this implementation.

## Generational Garbage Collection
In order to stay efficient, Java’s garbage collector will divide the heap space according to the age of the different objects. Therefore, it subdivides the heap into many different generations: A Young Generation, a Tenured Generation, and a Permanent Generation. 

The Young Generation is further subdivided into three sections: The eden space, where all objects that have just been created reside, and two survivor spaces.
The garbage collection in the young generation is triggered when this space gets filled up. In this step, the objects that reside in one space and are referenced by any other object can get aged. This happens if their age passes a certain threshold. In the younger generations, the garbage collection process happens quite frequently and it is a so-called “Stop the World Event”. This means that whenever the garbage collection process is performed, all other threads in the JVM get suspended. 
Major garbage collections, performed to all spaces, are also “Stop the World Events”. That is why they should not happen frequently if the intent is to keep the application responsive.

![global_heap](resources/images/global_heap.png)

## Z- Garbage Collector
The Z garbage collector is an optimized Garbage collection algorithm made for real-time Java applications. It guarantees that the “Stop the World Events” as previously mentioned, don’t take more than 10 milliseconds. The number of concurrent threads to be used is decided by a heuristic, although this can be manually set. If you want to learn more about the Z Garbage collector, I will leave a link below to a Baeldung Article that goes into much more detail than I did. I will also leave references for Oracles’ official website on the ZGC.

## Some Interesting Concepts
### Handle Pool
Some Garbage collection algorithms have also added the concept of a handle pool. All objects point to an entry in the pool containing the respective reference for their position in memory. This is useful for the compaction process since some objects might need to be moved and therefore their reference in memory will change. 
Instead of having to change all references to each object, the algorithm simply needs to update the references in the handle pool. While this is useful and saves time when changing objects references, it adds another level of indirection in every memory access made to an object's contents (Smith & Ravi Nair, 2005). 

![hotspot_heap](resources/images/hotspot_heap.png)

## Conclusion
This has been a simple overview of the Java Garbage collector, where we have discussed the basics of the Garbage collection process, the Generational Garbage collector that optimizes the Garbage collection process by subdividing the heap. We have also looked at the Z Garbage Collector and at the concept of Handle Pool.
Below, I have left some references that I recommend you check out. Some are really quick reads and offer great inside into the topic discussed in this Article.


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