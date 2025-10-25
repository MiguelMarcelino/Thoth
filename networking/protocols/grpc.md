# gRPC
gRPC is a high-performance, open-source RPC (Remote Procedure Call) framework developed by Google. It enables services to communicate efficiently across distributed systems using HTTP/2 and Protocol Buffers.

## Key properties

* Uses Protocol Buffers (binary serialization) for compact messages
* Built on HTTP/2 for multiplexing, streaming, and lower latency
* Strongly typed contracts defined in .proto files
* Supports automatic code generation for server and client
* Bi-directional streaming supported
* Load balancing, authentication, retry policies built-in

## How gRPC calls work

1. Client calls a method on a generated stub
2. Stub serializes request into Protocol Buffers
3. Data transmitted over HTTP/2 to server
4. Server deserializes, executes logic, sends response

## API types

* Unary RPC: one request, one response
* Server streaming: one request, multiple responses
* Client streaming: multiple requests, one response
* Bidirectional streaming: both sides stream

## When to use gRPC

* Low-latency microservice-to-microservice communication
* Internal service communication in large distributed systems
* High throughput data streaming

<hr>

Related to: [protocols](protocols)