# DNS

DNS (Domain Name System) is the distributed system that translates human-readable domain names (like `example.com`) into IP addresses that computers use to communicate over the internet.

Here’s how it works step by step:

1. User request: You type a domain name into a browser.
2. Local cache lookup: The system first checks the local DNS cache (your OS or browser) to see if it already knows the IP.
3. Recursive resolver query: If not cached, the query goes to a recursive resolver (usually provided by your ISP or a public DNS like Cloudflare’s 1.1.1.1 or Google’s 8.8.8.8).
4. Root servers: The resolver asks a root DNS server where to find information about the top-level domain (TLD) - for `.com`, `.net`, etc.
5. TLD servers: The resolver then queries the TLD name server, which responds with the address of the authoritative name server for that domain.
6. Authoritative server: This server contains the actual DNS records (A, AAAA, CNAME, MX, etc.) and returns the IP address associated with the domain.
7. Response: The resolver returns the IP to your computer, which then connects directly to the web server at that address.
8. Caching: The result is cached at multiple layers (OS, browser, resolver) for a time defined by the record’s TTL (Time To Live) to speed up future lookups.

DNS effectively acts as the "phone book" of the internet, mapping domain names to IP addresses in a distributed, fault-tolerant hierarchy.


<hr>

Related to: [coordination](coordination)