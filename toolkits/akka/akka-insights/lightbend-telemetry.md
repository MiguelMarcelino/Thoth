# Lightbend Telemetry
Provides a view into the workings of our distributed platforms. The image below shows a high-level overview of Lightbend Telemetry:

<div align="center">
	<img src="https://developer.lightbend.com/docs/telemetry/current/images/lightbend-monitoring-basic-overview.png" style="height: 250pt;">
</div>

Steps:
* Telemetry makes it possible to gather metric, event and trace information from Akka, Scala, Play, and Lagom based applications.
* The information is transferred to various backends.
* Grafana (a monitoring tool) then helps visualise the results

## Instrumentation
* Hook into the underlying toolkit or framework for our telemetry solution.
* Feature sets:
	* [Akka](https://developer.lightbend.com/docs/telemetry/current/instrumentations/akka/akka.html): captures telemetry (metrics, events, or traces) for Akka Actors, Akka Remoting, Akka Cluster, and Akka Persistence.
	* [Akka Streams](https://developer.lightbend.com/docs/telemetry/current/instrumentations/akka-streams/akka-streams.html): captures telemetry (metrics, events, or traces) for Akka Streams.
	* [Akka HTTP](https://developer.lightbend.com/docs/telemetry/current/instrumentations/akka-http/akka-http.html): captures server, endpoint, and client telemetry (metrics or traces) for Akka HTTP applications.
	* [Play](https://developer.lightbend.com/docs/telemetry/current/instrumentations/play/play.html): captures server, endpoint, and client telemetry (metrics or traces) for Play applications.
	* [Lagom](https://developer.lightbend.com/docs/telemetry/current/instrumentations/lagom/lagom.html): captures server, endpoint, and client telemetry (metrics or traces), as well as circuit breaker metrics, for Lagom services.
	* [Scala Futures](https://developer.lightbend.com/docs/telemetry/current/instrumentations/scala/scala-futures.html): captures telemetry (metrics or traces) for explicitly named Futures.
	* [Java Futures](https://developer.lightbend.com/docs/telemetry/current/instrumentations/java/java-futures.html): captures telemetry (metrics or traces) for explicitly named CompletableFutures.

<hr>

## Sources
* https://developer.lightbend.com/docs/telemetry/current/home.html

<hr>

Related to: [akka-insights](akka-insights)
Tags: #info-review

