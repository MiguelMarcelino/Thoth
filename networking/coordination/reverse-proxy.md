## Reverse Proxy
A reverse proxy is a server that sits between clients and backend servers, forwarding client requests to the appropriate server and returning the server’s responses. It helps improve performance, security, and reliability by handling tasks such as load balancing, caching, and SSL termination.


### Key Concepts

* Main Function: It acts on behalf of servers, hiding their identity and helping manage client requests efficiently.

* Direction of Flow: In a forward proxy, the proxy serves the *client*; in a reverse proxy, it serves the *server*.



### Functions of a Reverse Proxy

* Load Balancing:
  Distributes incoming network traffic across multiple backend servers to improve speed and reliability.

* Caching:
  Stores copies of frequently requested resources to reduce server load and speed up responses.

* Security and Anonymity:
  Protects backend servers by masking their IP addresses and filtering malicious requests.

* SSL Termination:
  Handles encryption and decryption of HTTPS traffic, offloading that task from backend servers.

* Compression and Optimization:
  Compresses responses and optimizes content delivery for faster performance.



### Common Use Cases

* High-traffic websites that need load balancing and caching.
* Applications requiring an additional layer of security.
* API gateways and microservices architectures.
* Content Delivery Networks (CDNs) — which often use reverse proxies to deliver content efficiently.



### Examples of Reverse Proxy Software

* NGINX
* Apache HTTP Server (mod_proxy)
* HAProxy
* Traefik
* Cloudflare (as a managed reverse proxy service)



### Sources

* N/A

<hr>

Related to: [coordination](coordination)