#microservices 

# Scale Cube

<div align="center">
	<img src="https://miro.medium.com/max/732/1*0DpDxw5yaA6eFqiIk2gFkw.png" style="height: 200pt;">
</div>

## X-axis scaling
* Consists of running multiple copies of an application behind a load balancer. 
* With N copies, each copy handles 1/N of the load.

### Drawbacks 
* Caches require more memory to be effective, as each copy potentially accesses all of the data
* Does not tackle the problems of increasing development and application complexity.


## Y-axis scaling
* splits the application into multiple services. 
* Each service deals with one or more closely related functions. 
* Decomposition (approaches can be combined):
	* verb-based decomposition: define services that implement a single use case
	* noun-based decomposition: create services responsible for all operations of an entity


## Z-axis scaling
* Each server runs an identical copy of the code. 
* Difference to X-Axis Scaling: Each server is responsible for only a subset of the data.
* Z-axis splits are commonly used to scale databases (a.k.a. sharded data)
* Z-axis scaling can also be applied to applications.
	* Requires a query aggregator to sends each query to all of the partitions and combine the results from each of them.

### Benefits
- Each server only deals with a subset of the data.
	- Reduces traffic
- Improves transaction scalability
	- Requests are distributed across multiple servers.
- Improves fault isolation
	- A failure only makes part of the data inaccessible.

### Drawbacks.
- Increased application complexity.

<hr>

## Sources
* https://microservices.io/articles/scalecube.html