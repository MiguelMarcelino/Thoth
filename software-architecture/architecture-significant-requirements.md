# ASRs (Architecture Significant Requirements)

An ASR is a requirement that will have a profound effect on the architecture. An architecture can be dramatically different without the need to meet one ASR.

## Early decisions that affect ASRs
* Allocation of Responsibilities: Planned evolution of responsibilities, user roles, system modes,...
* Coordination model: 
	* Properties of coordination (timeliness, currency, completeness, correctness, and consistency)
	* Names of external entities, protocols, network configurations, ...
* Data Model: Processing steps, information flows, major domain entities, access rights, persistence, evolution requirements
* Management of resources:
	* Time concurrency, memory footprint, scheduling, multiple users,...
	* Scalability requirements
* Mapping among Architectural elements: Plans for teaming, processors, ...
* Binding time decisions: Extensions of or flexibility of functionality, portability, configurations, ...
* Choice of technology: Named technologies, changes of technologies, ...

## Types of relationship between business goals and Architecture
- Business goals often lead to quality attribute requirements: Every quality attribute requirement must be described in terms of added value
- Business goals may directly affect the architecture without precipitating a quality attribute requirement at all
- No influence at all: No business goals leads to quality attributes (e.g. reduce costs)




<hr>

Related to: [software-architecture](software-architecture)