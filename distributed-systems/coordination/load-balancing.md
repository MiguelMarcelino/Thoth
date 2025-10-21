# Load Balancing

Load balancing distributes incoming requests across multiple service instances to ensure efficient resource use, reduce latency, and improve fault tolerance. It can happen:

- Client-side: the client queries the service registry and chooses an instance (used by systems like gRPC + etcd).
- Server-side: a load balancer (like HAProxy, Envoy, or Cloudflare’s edge network) routes traffic to available instances.
- DNS-based: DNS returns multiple IPs with rotation or weighting for balancing.

<hr>

Related to: [distributed-systems](../distributed-systems.md)