# Availability
- Refers to a property of software that is there and ready to carry out its task when you need it to be (Ability of a system to mask or repair faults such that the cumulative service outage period does not exceed a certain value)
- Builds upon the concept of reliability by adding the notion of recovery
- Dependability is the ability to avoid failures that are more frequent and more severe than is acceptable
- It is closely related to security, as breaches can cause downtime
	- Can be difficult to detect if a system has failed because of an attack or if it is just slo
- Distinction between fault and failure
	- If the source code has a fault and the system is able to recover from it without any observable deviation, then it is not a failure


## Availability general Scenario
- Source of stimulus: Internal or external
- Stimulus: A fault of one of the following classes
	- Omission: Component fails to respond to input
	- Crash: Component repeatedly suffers omission faults
	- Timing: Component responds, but response is early or late
	- Response: Component responds with incorrect value
- Artifact: Resource required to be highly available
- Environment: State of the system when fault/failure occurs
- Response: Reaction to the fault
- Response measure: Availability percentage, time to detect, time to repair, ...

Tactics for availability

![[availability_tactics.png]]



<hr>

Related to: [software-architecture](software-architecture)


