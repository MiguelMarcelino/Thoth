# Reverse Tunnel

A reverse tunnel is a network connection initiated from a device inside a private network outward to a public server, allowing external systems to access internal services through that tunnel.

## Why it’s used
- Works through NAT and firewalls that block inbound traffic.
- No need for router configuration or static public IPs.
- Provides secure access using encrypted channels (e.g., SSH, mTLS).
- Enables temporary or dynamic connections without exposing ports.

## How it works
1. The internal client connects to a public relay or edge server.
2. The relay keeps the connection open and listens for external requests.
3. When an external request arrives, the relay forwards it through the existing outbound tunnel back to the client.



---


Related to: [coordination](coordination)
