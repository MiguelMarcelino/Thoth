# Transport Layer protocols

The Transport Layer (Layer 4) is one of the most important parts of the OSI model because it’s where data delivery reliability, flow control, and segmentation happen.

It provides the logical communication between applications running on different hosts.
The two main protocols at this layer are TCP and UDP - each suited for different kinds of network communication.

---

## Transport Layer Overview

| Feature           | TCP (Transmission Control Protocol)                                        | UDP (User Datagram Protocol)                                 |
| --------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Type              | Connection-oriented                                                            | Connectionless                                                   |
| Reliability       | Reliable — ensures data is received correctly and in order                     | Unreliable — no guarantee of delivery or order                   |
| Connection Setup  | Requires a 3-way handshake before data transfer                                | No handshake — data sent immediately                             |
| Data Delivery     | Guarantees delivery using acknowledgments (ACKs) and retransmissions           | Best-effort delivery — lost packets are not retransmitted        |
| Ordering          | Ensures packets arrive in sequence                                             | No ordering — packets may arrive out of order                    |
| Flow Control      | Uses sliding window mechanism                                                  | No flow control                                                  |
| Error Checking    | Uses checksums, sequence numbers, and ACKs                                     | Uses checksums only (no correction)                              |
| Speed             | Slower due to reliability mechanisms                                           | Faster due to minimal overhead                                   |
| Header Size       | 20 bytes (minimum)                                                             | 8 bytes                                                          |
| Typical Use Cases | Web browsing (HTTP/HTTPS), Email (SMTP, IMAP, POP3), File Transfer (FTP, SFTP) | Streaming (YouTube, VoIP, Online games, DNS, Video conferencing) |

---

## How TCP Works (Connection-Oriented)

TCP ensures reliable communication through several key mechanisms:

1. Three-Way Handshake (Connection Establishment)

   * SYN → Client requests connection
   * SYN-ACK → Server acknowledges request
   * ACK → Client confirms and connection established

2. Data Transmission

   * Data is broken into segments and numbered.
   * Each segment is acknowledged by the receiver.

3. Flow Control

   * Uses a window size to prevent overwhelming the receiver.

4. Error Control

   * Uses checksums and retransmissions to ensure data integrity.

5. Connection Termination

   * Uses a 4-way handshake to gracefully close the connection.

## How UDP Works (Connectionless)

UDP is simple and fast because it skips all the connection setup and reliability mechanisms.

* Data is sent in datagrams, each independent.
* No handshake, acknowledgment, or retransmission.
* Useful for real-time or time-sensitive applications where speed matters more than reliability.

## Quick Summary

| Feature      | TCP | UDP |
| ---------------- | ------- | ------- |
| Reliable         | ✅       | ❌       |
| Ordered          | ✅       | ❌       |
| Error Correction | ✅       | ❌       |
| Connection Setup | ✅       | ❌       |
| Fast             | ❌       | ✅       |
| Lightweight      | ❌       | ✅       |


## Sources
* N/A


<hr>

Related to: [fundamentals](fundamentals)