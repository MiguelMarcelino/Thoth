# Kubernetes
Kubernetes is a container orchestration tool. As applications migrate to a Microservice architecture, this implies that one must now deploy several services instead of one Monolith application. Managing all these applications using deployment scripts is unfeasible, hence the need for an orchestration service.

Kubernetes provides
* High availability
* Scalability (high performance)
* Disaster recovery

---

## Kubernetes Terms
### Pod
* Abstraction over a container
* Creates a running environment/layer over a container
* Meant to run one application container 
* Each pod gets its own IP address to communicate with other pods
* Pods are ephemeral
	* New pods get created if old ones go down
	* The new pod gets a new IP address

### Service
* To avoid connection problems, Kubernetes also has services, which allows pods to have a static IP address
* This allows applications to remain running when pods fail (as IPs do change when pods restarts)
* Acts as a load balancer
	* Redirects requests to other nodes when a service is busy
* Services route requests between pods that are running in each node
	* This avoids the network overhead of sending requests to pods running on different nodes.

### Node
* Holds multiple pods
	* E.g Holds an application and its database (in two sepparate pods)
	* Uses the concept of a Microservice

### Ingress
* Proxies incomming requests
* Exposes an internal service through a URL (essentially maps the IP address to an address)

### Configmap
* Contains thje configuration for pods
	* It contains URLs of pods (such as a database) to allow pods to easily communicate with each other
* It is not made to hold credentials

### Secret
* Similar to configmap, but used to store secret data
* Saved in base64 format

### Volumes
* Storage on a local machine or on remote storage 
* Ensures that data is stored safely when pods are restarted

### Deployment
* Is an abstraction on top of pods
* It allows setting a certain number of replicas to optimize uptime
* It manages a replica set

### StatefulSet
* Made for stateful applications (Used for DBs mostly)
* Is an abstraction over pods, similarly to a deployment. However, this is geared towards stateful applications
* These are more dificult to configure thatn deployments, so it is common to setup databases outside k8s

An overview over the layers of abstraction
![[kubernetes_layers_of_abstraction.png]]

---

## K8s Architecture

![[kubernetes-architecture.png]]

### Container Runtime
* Is installed on each kubernetes node
* E.g Docker

### Kubelet
* Schedules containers inside a node]
* Interface between machine and container node
* It takes the configuration and runs the pods

Kube Proxy
* Handles requests between nodes

Master Nodes
* Control master state and worker nodes
* Have an API server
	* Clients interact with this server
	* It acts as a cluster gateway (a gateway to the cluster)
	* Is a gatekeeper (ensures that connections comming into the server are authenticated)
* Scheduler
	* Decides whether to create new pods depending on the incoming requests
	* Decides which nodes to add pods too (depending on the current load)
* Contoller manager
	* Detect state changes (e.g. pod crashes)
	* Makes a request to the scheduler, which then creates the necessary pods
* etcd
	* Cluster brain
	* Contains a key value store to keep track of the state of the server
	* The stored data is used to make changes to the cluster and adapt the cluster to incoming load

---

## minikube
* Create a virtualbox locally
* Nodes run in the virtual environment

---

## Some commands
* Pod commands
	* kubectl get pod POD_NAME
	* kubectl logs POD_NAME
	* kubectl describe pod POD_NAME
	* kubectl exec -it POD_NAME -- bin/bash 
		* Opens a terminal to a pod
* Manage Replica set (Replica set manages the replicas of a pod. These should be automatically created by kubernetes (typically, we only work on the deployment level))
	* kubectl get replicaset
* Deployment management
	* kubectl get depoyment
	* kubectl get deployment DEPLOYMENT_NAME -o yaml
		* Gets the current deployment information
	* kubectl create deployment NAME --image=IMAGE_NAME
		* Images can be pulled from dockerhub
	* kubectl delete deployment NAME_OF_DEPLOYMENT

---

## Kubernetes configuration file
To avoid using these commands to extensively on larger commands, one can use deployment configurations.
To apply a configuration, use the following command
* kubectl apply -f config-file.yaml

Each configuration file has three main parts, which will be explained in this section.

### Metadata
* Data that helps uniquely identify the object, including a name string, UID , and optional namespace

### Specification
Depends on the ***kind*** of component that is being create. For instance:

* Templates
	* Have their own metadata
	* Applies to a pod. (it is a blooprint for a pod)
* Selector
	* Matches to a deployment label (this is usualy set in the metadata)
* Ports
	* The ***port*** refers to the container port exposed by a pod or deployment
	* The ***targetPort*** refers to the port on the host machine that traffic is directed to
	* The ***nodePort*** port sets the port where the pod is listening for external requests (It must be between 30000 and 32767)
* Type
	* **LoadBalancer**: Exposes the service via the cloud provider’s load balancer.
	* **ClusterIP**: Exposes a service which is only accessible from within the cluster.
	* **NodePort**: Exposes a service via a static port on each node’s IP.
	* **ExternalName**: Maps a service to a predefined ***externalName*** field by returning a value for the CNAME record.

### Status
* Compares the desired state to the actual state
* Ensures that the infrastructure conforms to the specification
* Status is continuously updated
* Information about the cluster is tord in the etcd


An example of a basic config file

```
apiVersion: apps/v1
kind: Deployment
metadata:
	name: nginx-deployment 
	labels:
		app: nginx
spec:
	replicas: 1
	selector:
		matchLabels:
			app: nginx
	template:
		metadata:
			labels:
				app: nginx 
		spec:
			containers:
			- ﻿﻿name: nginx
			  image: nginx:1.16
			  ports:
			  - containerPort: 80
```



---

# Sources
* Concepts: https://kubernetes.io/docs/concepts/overview/components/
* Objects in Kubernetes: https://kubernetes.io/docs/concepts/overview/working-with-objects/
* Amazing video: https://www.youtube.com/watch?v=X48VuDVv0do
