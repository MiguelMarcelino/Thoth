# Attribute Driven Design

Iterative method that, at each iteration, helps the architect do the following
* Choose a part of the system to design
* Identify all the architecturally significant requirements for that part
* Create and test a design for that part
* Inventory remaining requirements and select the input for the next iteration

The output is an architecture in which the main components have been selected and vetted.

## Inputs to ADD
* Functional, Quality, and constraint requirements should be known
	* Requirements are never finalised and are continuously arriving from the stakeholders. So we will never have the full list of requirements when starting a project
	* ADD can begin when a set of Architecturally Significant Requirements is known (See [Architecture Significant Requirements](architecture-significant-requirements))
* The boundaries of the system should be known
	* Establish scope of architecture
* External devices, users and environmental conditions should be known (A.k.a the system's running environment)

## Output of ADD
* Set of sketches and architectural views
	* These identify architectural elements and their relationships or interactions
	* One of the views will be a module decomposition view, where each element will have its responsibilities listed
* 