# Load Balancing Strategies
Load balancing distributes incoming traffic across multiple servers to improve performance, availability, and fault tolerance.

## Common strategies

* Round-robin: Requests are sent sequentially to each server in the pool, cycling back to the first server when done
* Least-connections: New requests go to the server with the fewest active connections
* Locality-aware: Requests are routed based on network proximity or latency to minimize response time

## Practical considerations

* Choose strategy based on workload type and server capacity
* Can combine with health checks to avoid sending traffic to unhealthy servers
* Works at different layers: L4 (TCP) or L7 (HTTP)
