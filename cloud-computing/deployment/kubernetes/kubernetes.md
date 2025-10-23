# Kubernetes
* Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit.
* The abstractions in Kubernetes allow you to deploy containerized applications to a cluster without tying them specifically to individual machines.
* Kubernetes automates the distribution and scheduling of application containers across a cluster in a more efficient way.


## Cluster
* The Control Plane is responsible for managing the cluster.
	* Schedules applications, maintains applications' desired state, scales applications, and rolles out new updates.
* A node is a VM or a physical computer that serves as a worker machine in a Kubernetes cluster.
	* Each node has a Kubelet, which is an agent for managing the node and communicating with the Kubernetes control plane.
* The nodes communicate with the control plane using the Kubernetes API

### Cluster Overview
<div align="center">
	<img src="https://d33wubrfki0l68.cloudfront.net/283cc20bb49089cb2ca54d51b4ac27720c1a7902/34424/docs/tutorials/kubernetes-basics/public/images/module_01_cluster.svg" style="height: 250pt;filter: invert(1);">
</div>


## Pods
* A Pod hosts an application's instance
* A Pod is a Kubernetes abstraction that represents a group of one or more application containers
* Includes some shared resources
	* Shared storage, as Volumes
	* Networking, as a unique cluster IP address
	* Information about how to run each container, such as the container image version or specific ports to use

### Pod Overview
<div align="center">
	<img src="https://d33wubrfki0l68.cloudfront.net/fe03f68d8ede9815184852ca2a4fd30325e5d15a/98064/docs/tutorials/kubernetes-basics/public/images/module_03_pods.svg" style="height: 250pt;filter: invert(1);">
</div>


## Nodes
* A Node is a worker machine in Kubernetes and may be either a virtual or a physical machine, depending on the cluster.
* Each Node is managed by the control plane.
* Pods run on nodes, where a node can have multiple pods
* Nodes run, at least:
	* Kubelet: a process responsible for communication between the Kubernetes control plane and the Node (manages the Pods and the containers running on a machine).
	* A container runtime: puls container image from a registry, unpacks it, and runs the application

### Node Overview
<div align="center">
	<img src="https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg" style="height: 250pt;filter: invert(1);">
</div>

## Services
* Abstraction which defines a logical set of Pods and a policy by which to access them.
* Enable a loose coupling between dependent Pods.
* Although each Pod has a unique IP address, those IPs are not exposed outside the cluster without a Service. (**Services allow your applications to receive traffic**).
* Services can be exposed in different ways by specifying a type in the ServiceSpec:
	* ClusterIP (default) - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
	* NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`. 
		* Superset of ClusterIP.
	* LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. 
		* Superset of NodePort.
	* ExternalName - Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. 
		* No proxying of any kind is set up. 

---

## Sources
* https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/
* https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/

<hr>

Related to: [deployment](deployment)