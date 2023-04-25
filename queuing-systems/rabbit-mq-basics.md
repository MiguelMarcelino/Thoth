## Basics First

In RabbitMQ, there are queues and messages. Messages are bound to queues. These bindings consist of two main things:

1.  The type of exchange used to publish the message
2.  The routing key used when publishing the message

There are three types of exchanges that can be used with RabbitMQ:

1.  Direct Exchanges: Require an exact match between the routing key on an exchange's binging and the routing key on a message
2.  Fanout Exchanges: Route every message to every bound exchange.
3.  Topic Exchanges: Provides pattern matching for routing keys.
4.  Header exchanges: Rarely used (they also have a performance impact).

After getting the basic things out of the way, let's start by looking at message sending.

## Sending Messages

### Direct Exchange

Used when one wants to send a message directly to a recipient.

Below is an example of a direct exchange using JavaScript's `wascally` library:

```
// publish a message to the "jobs" queue
```

Note that the key `job-request` is case-sensitive. We must send the exact key for this to work properly.

Direct exchanges also allow publishing messages with an empty routing key (often called the "default" routing key). For such a message to be routed, there must be a binding that matches this empty routing key.

### Fanout exchange

Useful when an application does not need to know about messages that are sent when the application is not connected to the queue

Furthermore, fanout exchanges do not require routing keys, which is useful in scenarios where an application must bind/unbind from different queues as needed

### Topic Exchange

Topic exchanges allow you to specify wild-card matching of “topics” (routing keys) in your bindings. This allows receiving messages from more than one routing key.

The logging example makes this very clear. One can send logging messages with the severity set in the routing key. Debug logging may have a key of `log.debug` while errors may have a key of `log.error` and so-on.

```
wascally.publish("log.ex", {
```

```
wascally.publish("log.ex", {
```

With this configuration, we can assign message queues using pattern matching.

## Routing Keys

-   The dot symbol (.) is used as a word separator.
-   The asterisk symbol (*) is used to match a single word in a specified position.

-   Example: A binding of `log.*` will match routing keys of `log.error` and `log.debug`, but will not match `log.error.app-1` or `log.error.app-2`

-   The pound symbol (#) is used to match zero or more words

-   Example: A binding of `log.#` will match all routing keys that start with `log.` - no matter how many separators are used in the routing key.

-   These rules can be mixed to create more complex rules

-   Example: A binding of `#.error.*` will match any number of words at the beginning, with the word “error” just prior to the final word in the key.

## Drain, Delete or Transfer

Upon introducing some changes in RabbitMQ's layout, one has to take care of the old messages in the queue, as they will not be compatible with the new messages. There are three main strategies to do this:

-   “Drain” the queue: Let all the messages process until the queue is clear.
-   Delete the queue and all the messages: Drop the messages. This can be a solution, if the messages are not critical for the system. If they keep track of ongoing work, this strategy is not ideal.
-   Transfer all the messages to a new queue: Requires one to re-write the current queue handler code, which would transform the messages in to a new message and re-publish them to the new exchange and queue.

<hr>
Related to: [queuing-systems](queuing-systems)