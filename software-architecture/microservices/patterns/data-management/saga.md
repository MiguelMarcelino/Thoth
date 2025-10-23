# Saga
* Business transaction that spans multiple services
* It is a sequence of local transactions, where each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga.
* If a local transaction fails because it violates a business rule then the saga executes a series of compensating transactions that undo the changes that were made by the preceding local transactions.

There are two ways of coordination sagas:
1. Choreography - each local transaction publishes domain events that trigger local transactions in other services

<div align="center">
	<img src="https://chrisrichardson.net/i/sagas/Create_Order_Saga.png" style="width: 400pt">
</div>

In this first mode, each service publishes an event. The response of that service to the event is entirely up to the receiving service. After executing the behaviour triggered by the received event, it then sends a resulting event with the outcome of execution.

2. Orchestration - an orchestrator (object) tells the participants what local transactions to execute

<div align="center">
	<img src="https://chrisrichardson.net/i/sagas/Create_Order_Saga_Orchestration.png" style="width: 400pt">
</div>

In the second mode, the OrderService starts by receiving a request with a new order. This then gets parsed by the OrderService, until reaching the `Create Order Saga`, which creates the order and sends a new `Reserve Credit` command to the Customer Service. This request arrives to the Customer service's `Command Hander`, which parses this request and sends the response with the result of running that event. Upon receiving the event, the `OrderService` approves the order using the `approve` operation.


<hr>

## Sources
* https://microservices.io/patterns/data/saga.html

<hr>

Related to: [data-management](data-management)