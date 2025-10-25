# Presentation Layer

## SSL/TLS

SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are cryptographic protocols that provide security for data transmitted over a network.

TLS is the successor to SSL — SSL is now obsolete. TLS ensures that communication between two devices (like your browser and a web server) is:

- Encrypted (private)
- Authenticated (trustworthy)
- Integrity-protected (unchanged in transit)


## Key Security Features

| Feature        | Description                                                                | Example                                         |
| ------------------ | ------------------------------------------------------------------------------ | --------------------------------------------------- |
| Encryption     | Converts data into unreadable form so only authorized parties can read it.     | AES, ChaCha20                                       |
| Authentication | Verifies the identity of the communicating parties using digital certificates. | X.509 Certificates, Public Key Infrastructure (PKI) |
| Integrity      | Ensures that data is not altered during transmission.                          | Message Authentication Codes (MACs)                 |


## How SSL/TLS Works (Handshake Process)

Here’s a simplified step-by-step of what happens when your browser connects securely to a website (HTTPS):

1. Client Hello

* The client (browser) sends:

  * Supported TLS versions (e.g., TLS 1.2, 1.3)
  * Supported cipher suites (encryption algorithms)
  * A random number (for key generation)

2. Server Hello

* The server responds with:

  * Chosen TLS version and cipher suite
  * Its own random number
  * Its digital certificate (which includes its public key and domain identity, signed by a Certificate Authority)

3. Server Authentication

* The client verifies the server’s certificate (ensures it's valid, trusted, and not expired).
* If valid, it proceeds — if not, you’ll see a browser warning (like *“Connection not secure”*).

4. Key Exchange

* Depending on the TLS version and chosen cipher suite:

  * In older versions (TLS 1.2), a pre-master secret is sent encrypted with the server’s public key.
  * In TLS 1.3, both sides generate a shared key using Elliptic Curve Diffie-Hellman (ECDHE) — faster and more secure.

5. Session Keys Generated

* Both sides independently compute the same session key using the random values and shared secret.
* This key is used to encrypt and decrypt actual data.

6. Handshake Completion

* Both sides send “Finished” messages to confirm that future communication will be encrypted using the negotiated parameters.


## TLS Versions

| Version   | Released | Status          | Notes                                                   |
| ------------- | ------------ | ------------------- | ----------------------------------------------------------- |
| SSL 2.0 / 3.0 | 1990s        | Deprecated        | Insecure — replaced by TLS                                  |
| TLS 1.0 / 1.1 | 1999–2006    | Deprecated        | Vulnerable to attacks                                       |
| TLS 1.2   | 2008         | Still widely used | Supports modern ciphers                                     |
| TLS 1.3   | 2018         | Current version   | Faster handshake, more secure (removes outdated algorithms) |


## Where SSL/TLS Is Used

* HTTPS → Secure web browsing
* FTPS / SFTP → Secure file transfers
* IMAPS / SMTPS → Secure email
* VPNs → Encrypted network tunnels
* VoIP / Messaging apps → End-to-end encrypted communication

<hr>

## Sources
* N/A


<hr>

Related to: [networking](networking)