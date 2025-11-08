# Docker
Docker is a containerization platform that packages applications and their dependencies into isolated units called containers.

## Docker Fundamentals

- **Images**  
	- Immutable blueprints built from a `Dockerfile`.  
	- Each image contains the OS layer, dependencies, and the app itself.  
	- Think of it as a class - containers are instances of it.
    
- **Containers**  
	- Running instances of images.  
	- Lightweight, isolated processes that share the host OS kernel.  
	- They can be started, stopped, and removed easily.
    
- **Networking**  
	- Docker creates virtual networks for container communication. We can configure networking using the following modes:
		- _bridge_: default, isolates containers but allows interconnection.
		- _host_: shares the host’s network stack.
		- _overlay_: connects containers across multiple hosts (e.g., Swarm).
- **Volumes** 
	- Persistent storage that exists outside container lifecycles.
	- Used to store data (like databases or logs) that must survive container restarts.


**In short:** Images define _what_ runs, containers run it, networking connects them, and volumes persist their data.

---

Related to: [containers](../containers.md)