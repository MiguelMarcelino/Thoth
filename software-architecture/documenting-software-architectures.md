# Documenting Software Architectures

## Architecture Notations

- Informal Notation (example: PowerPoint)
	- Views depicted using general-purpose diagramming
	- Semantics of the system are described in natural language
- Semiformal Notation (example: UML)
	- Views depicted in standardized notation that prescribes graphical elements and rules of construction
	- Does not provide a complete semantic treatment of the meaning of the elements used
- Formal Notation (example: ADL)
	- Notation has precise semantics
	- Allows for formal analysis of syntax and semantics
	- Architecture Description Language (ADL) can be used to describe the system

## Views

### Module Views
- Definition of "Module": implementation of a unit that provides a coherent set of responsibilities
- Can take the form of a class or a set of classes
- Relations:
	- Is part of: defines a relationship between a module and its submodules
	- Depends on: Defines a dependency relationship between two modules
	- Is a: Defines generalization/specialization relationship between a more specific module (the child) and a more general module (the parent)
- Constraints
	- Module views may impose topological constraints, such as visibility limitations between modules
- Usage
	- Change-impact analysis
	- Planning incremental development
	- Requirements traceability analysis
	- Communicating functionality of the system and structure of a code base
	- ...

**Module's characteristics**
- A module has a name
	- Often suggests what it does
- Responsibilities
	- Identify the role of the module\
- Visibility of Interfaces
	- Which interfaces are private and which ones are not (submodules may be hidden)
- Implementation information
	- Mapping to source-code units
		- Identifies files that constitute the implementation of a module
		- Example of a module `Account` in Java: (`AccountImpal.java` holds the implementation, `IAccount.java` specifies the interface, `AccountBean.java` holds the state of account in memory, ...)
	- Test information
		- Module's test plan, test cases, test scafolding and test data
	- Management information: manager's information (e.g. pointer to location)
	- Implementation constraints
	- Revision history
		- Helps maintenance
		- e.g. Authors of changes

### Component-and-Connector
- Components
	- Principal processing units and data stores
	- Has a set of ports which it uses to interact with other components
- Connectors
	- Pathways of interaction between components
	- Have a set of roles that indicate how components may use a connector in interactions
- Attachments
	- Component ports are associated with connector roles to yield a graph of C&Cs
- Interface delegation
	- Component ports are associated with one or more ports in an internal sub-architecture
- Constraints
	- Components can only be attached to connectors (same for connectors)
	- Attachments are only possible for compatible ports and connections
	- Interface delegation only happens between two compatible ports
	- Connectors do not appear in isolation

C&C are typically used for showing how the system works, guiding the development process by specifying structure and behaviour of runtime elements, and helping one reason about the system's quality attributes.


### Allocation Views
Allocation views describe the mapping of software units to elements of an environment in which the software is developed or in which it executes.
- Software element: Has the properties that are required of the environment
- Environmental element: Has properties that are provided to the software
- Relations
	- Allocated to: A software element is mapped to an environmental element

Allocation views can be used to reason about performance, availability, security, and safety.

### Quality Views
Module, C&C, and allocation views are structural views created to show the engineered structures to satisfy functional and quality requirements. A quality view can be tailored to specific stakeholders to address specific concerns. They extract pieces of structural views to focus on a specific aspect of the system.
Some examples are:
- Security view:
	- Shows components that impact security and how they communicate
	- Shows data repositories that are relevant for security
	- Depicts how humans interact with the system
- Communications view
	- Useful for systems that are globally dispersed and heterogeneous
	- Shows all component-to-component channels, network channels, quality-of-service parameter values, and areas of concurrency
- Exception or Error-handling view
	- Shows how components report, detect, and resolve faults
- Reliability view
	- Models replication and switchover methods
- Performance view
	- Can show network traffic models, maximum latencies for operations, ...


## Combining Views
When a view has a strong association to another view these can be merged to create a new and more convenient way to look at the system
Examples
* Combining various C&C views: C&C views all show runtime relations between components, so they can be combined.
* Deployment view with SOA or communicating-processes view
	* SOA view shows services, and communicating-processes view shows processes
	* Both are deployed onto a system and can be easily combined
* Decomposition view and implementation, uses, or layered view
	* Decomposed modules from units of work


### Building the Documentation Package
* Section 1: The primary presentation
	* Shows elements and relations of the view
	* Conveys information about system and includes its primary elements
	* Most often, it is a graphical representation
	* The goal is to present a summary of the most important information
* Section2 : The element catalog
	* Details at least elements depicted in primary representation. Also explains relations that might have been omitted in the primary view
	* Elements and their properties
		* Names each elements and lists their properties
		* Explains responsibility of each module in the system
	* Relations and their properties
		* Describe relations between a system's elements
	* Element interfaces: Document element interfaces
	* Element behaviour
		* Document behaviour that is not obvious in primary representation
* Section 3: Context Diagram
	* Shows how the system relates to its environment
	* Context diagram depicts scope of a view
* Section 4: Variability Guide
	* Shows how to exercise variation points of an architecture
* Section 5: Rationale
	* Explains why the design came to be
	* Provide arguments that it is sound

<u>Documentation beyond views</u>
* Overview of architecture documentation
	* Tells how documentation is laid out
* Information about architecture
	* Short system overview
	* Overview of rational behind system

Sections
* Section 1: Documentation Roadmap
	* Scope and summary: Explain purpose of document and summarise what is covered.
	* How document is organised
	* View overview
	* How stakeholders can use documentation
* Section 2: How a view is documented
	* Explain standard organisation used to document views
	* Refer to what standard was used
* Section 3: System overview
	* Short description of system's function, users, and constraints
* Section 4: Mapping between views
	* Describe how views are related to each other
* Section 5 Rational
	* Documents architecture decisions that apply to more than one views
	* Document decisions about patterns to use
* Section 6: Directory
	* Reference material


### Documenting behaviour
TBC


<hr>

Related to: [software-architecture](software-architecture)