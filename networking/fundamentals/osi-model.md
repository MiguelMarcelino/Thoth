# OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and standardize how different networking systems communicate over a network. It divides network communication into seven layers, each with specific functions and protocols.


## The 7 Layers of the OSI Model

| Layer | Name         | Main Function                                                                                                  | Examples of Protocols / Devices                 |
| --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| 1     | Physical     | Transmits raw bits over a physical medium (cables, radio, etc.). Defines hardware specs, voltages, and data rates. | Ethernet cables, Fiber optics, Hubs, Repeaters      |
| 2     | Data Link    | Provides reliable node-to-node data transfer, handles framing, MAC addressing, and error detection.                | Ethernet (IEEE 802.3), PPP, Switches, MAC Addresses |
| 3     | Network      | Determines routing and logical addressing (IP addressing). Moves packets between networks.                         | IP, ICMP, ARP, RIP, OSPF                            |
| 4     | Transport    | Ensures reliable (or fast, if UDP) data delivery between hosts; handles segmentation, flow, and error control.     | TCP, UDP                                            |
| 5     | Session      | Manages sessions or dialogs between applications — establishes, maintains, and terminates connections.             | NetBIOS, RPC, PPTP                                  |
| 6     | Presentation | Translates, encrypts, or compresses data for the application layer. Ensures correct data format.                   | SSL/TLS, JPEG, MPEG, ASCII                          |
| 7     | Application  | Closest to the user — provides network services like web browsing, email, and file transfer.                       | HTTP, HTTPS, FTP, SMTP, DNS                         |


## Key Concepts

* Encapsulation: Data is wrapped with protocol information at each layer before being sent.
* Decapsulation: The reverse process at the receiving end.
* Layer Independence: Each layer provides services to the one above and uses services from the one below.


## In Comparison — TCP/IP Model

The TCP/IP model (used practically on the internet) is simpler - it has 4 layers:

1. Application (OSI 5–7)
2. Transport (OSI 4)
3. Internet (OSI 3)
4. Network Access (OSI 1–2)

<hr>

## Sources
* N/A


<hr>

Related to: [fundamentals](fundamentals)


