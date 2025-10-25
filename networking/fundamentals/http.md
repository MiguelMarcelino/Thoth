# HTTP

Overview:
HTTP (Hypertext Transfer Protocol) is a stateless application-layer protocol used for communication between clients and servers on the web.

## Key properties

* Request/response driven
* Stateless (each request independent)
* Methods define action (GET, POST, PUT, DELETE, etc.)
* Headers provide metadata for requests and responses
* Status codes indicate the result (200 OK, 404 Not Found, etc.)

## HTTP versions

* HTTP/1.1: persistent connections, head-of-line blocking
* HTTP/2: multiplexing multiple requests over one TCP connection
* HTTP/3: runs over QUIC (UDP) to avoid TCP head-of-line blocking

## Performance considerations

* Keep-alive connections reduce handshake overhead
* Compression (gzip, brotli) for smaller payloads
* Caching controlled by headers like Cache-Control and ETag

## Security

* HTTPS = HTTP over TLS
* Provides encryption, integrity, and authentication

## When to use HTTP

* Browsers and public APIs
* Human-readable network communication
