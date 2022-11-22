# Performance Tips
* Be careful with any operations performed on immutable collections, such as the ones discussed in the [First Class Functions](first-class-functions) note, as these create new lists for every operation that changes the immutable types. This might result in a lot of garbage generation. 

<hr>

Related to: [scala](scala)