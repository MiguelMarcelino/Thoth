# Kubernetes
Kubernetes is a container orchestration tool. As applications migrate to a Microservice architecture, this implies that one must now deploy several services instead of one Monolith application. Managing all these applications using deployment scripts is unfeasible, hence the need for an orchestration service.

Kubernetes provides
* High availability
* Scalability (high performance)
* Disaster recovery

---

## K8s Architecture
Below is the architecture of Kubernetes. This section briefly explains what each term means.

![[kubernetes-revised-architecture.png]]

### Pod
* Abstraction over a container (although one can run multiple containers within a single pod)
	* Creates a running environment/layer over a container
* All applications in a pod share the same resources and local network, easing communications between applications in a pod.
	* Although it is not very common to run multiple containers within a single pod
	* DBs typically run on a separate service (such as AWS)
* Each pod gets its own IP address to communicate with other pods
* Pods are ephemeral
	* New pods get created if old ones go down
	* The new pod gets a new IP address

### Kubelet
* Schedules containers inside a node
* Interface between machine and container node
* It takes the configuration and runs the pods

### Kube Proxy
* Handles requests between nodes

### Node
* Holds multiple pods, along with the Kubelet and Kube proxy
	* E.g Holds an application and its database (in two separate pods)
	* Uses the concept of a Microservice

### Container Runtime
* Is installed on each kubernetes node
* E.g Docker

### Service
- To avoid connection problems, Kubernetes also has services, which allows pods to have a static IP address 
- This service acts as a load balancer
	* Redirects requests to other nodes when a service is busy
	* Allows applications to remain running when pods fail (as IPs do change when pods restart)
* Services route requests between pods that are running in each node
	* This avoids the network overhead of sending requests to pods running on different nodes.

### Deployment
* Is an abstraction on top of pods
* It allows setting a certain number of replicas to optimize uptime
* It manages a replica set
### Ingress
* Proxies incoming requests
* Exposes an internal service through a URL (essentially maps the IP address to an external address)

### Configmap
* Contains the configuration for pods
	* It contains URLs of pods (such as a database) to allow pods to easily communicate with each other
* It is not made to hold credentials

### Secret
* Similar to configmap, but used to store secret data
* Saved in base64 format

### Volumes
* There are two main types of volumes on Kubernetes
	* Ephemeral volumes:
		* On-disk files stored for each pod
		* All data stored in them gets deleted when the pods are stopped.
	* Persistent volumes:
		* Exist beyond the lifetime of a pod

### StatefulSet
* Made for stateful applications (Used for DBs mostly)
* Is an abstraction over pods, similarly to a deployment. However, it is geared towards stateful applications
* These are more difficult to configure than deployments, so it is common to setup databases outside k8s

### Control plane
* Control master state and worker nodes
* API server
	* Clients interact with this server
	* It acts as a cluster gateway (a gateway to the cluster)
	* Is a gatekeeper (ensures that connections coming into the server are authenticated)
* Scheduler
	* Decides whether to create new pods depending on the incoming requests
	* Decides which nodes to add pods too (depending on the current load)
* Controller manager
	* Detect state changes (e.g. pod crashes)
	* Makes a request to the scheduler, which then creates the necessary pods
* etcd
	* Cluster brain
	* Contains a key-value store to keep track of the state of the cluster
	* The stored data is used to make changes to the cluster and adapt the cluster to incoming load


An overview over the layers of abstraction
![[kubernetes_layers_of_abstraction.png]]


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
To avoid using these commands too extensively, one can use deployment configurations. To apply a configuration, use the following command
* kubectl apply -f config-file.yaml

Each configuration file has three main parts, which will be explained in this section.

### Metadata
* Data that helps uniquely identify the object, including a name string, UID, and optional namespace

### Specification
Depends on the ***kind*** of component that is being created. For instance:

* Templates
	* Have their own metadata
	* Applies to a pod. (it is a blueprint for a pod)
* Selector
	* Matches to a deployment label (this is usually set in the metadata)
* Ports
	* The `port` refers to the container port exposed by a pod or deployment
	* The `targetPort` refers to the port on the host machine that traffic is directed to
	* The `nodePort` port sets the port where the pod is listening for external requests (It must be between `30000` and `32767`)
* Type
	* **LoadBalancer**: Exposes the service via the cloud provider’s load balancer.
	* **ClusterIP**: Exposes a service which is only accessible from within the cluster.
	* **NodePort**: Exposes a service via a static port on each node’s IP.
	* **ExternalName**: Maps a service to a predefined `externalName` field by returning a value for the `CNAME` record.

### Status
* Compares the desired state to the actual state
* Ensures that the infrastructure conforms to the specification
* Status is continuously updated
* Information about the cluster is stored in the etcd


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

## Namespaces
4 Default namespaces
* kube-system
	* System processes from master and `kubectl`
	* This is reserved for Kubernetes and cannot be used for deploying applications
* kube-public
	* Contains publicly accessible information
	* Accessible via: `kubectl` cluster-info
* kube-node-leads
	* Contains information about the node's heartbeats
* default
	* Created resources are located in this namespace

The first use of namespaces is to create groups for different kinds of applications. The picture below illustrates this scenario.

![[kubernetes_namespace_example.png]]

Another scenario where multiple namespace are necessary, is in a scenario where multiple teams are working in the same cluster. This way, multiple teams can be deploying different versions of the same application without disrupting each others flow.

![[kubernetes_namespaces_multipe_teams.png]]


Another strategy is called Blue/Green deployment. This allows us to deploy a newer version to production much faster and switch to the new deployment when that is ready. This reduces downtime (hence, it increases availability) and avoids having to setup a separate cluster.

![[kubernetes_blue_green_deployment.png]]


Finally, it is also possible to limit the amount of resources per namespace level. This avoids having one team that consumes all the resources, leaving other teams without resources for scheduling new pods.

![[kubernetes_limit_resources.png]]


Things to consider about namespaces
* Each namespace defines its own `ConfigMap`
	* One cannot access resources from other namespaces
	* Services allow using pods from other namespaces
* Some components can't be created within namespaces
	* Volumes are accessible throughout the whole cluster
	* Nodes are not within a specific namespace
	* Find these resources using the following command
		* kubectl api-resources --namespaced=false


---
## Ingress
* Entrypoint to the cluster
* Evaluates all the rules
* Manages redirections

![[kubernetes_ingress.png]]

The image above also shows a Cloud Load Balancer, which will be used if Kubernetes is deployed to a cloud provider.

Ingress also allows setting up a TLS connection. This requires us to provide the certificate and key files for authentication and encryption. An important aspect is that the secret component must be in the same namespace as the ingress component. Below is an example config file that supplies a TLS certificate and key file.

```
apiVersion: v1
kind: Secret
metadata:
	name: myapp-secret-tls
	namespace: default
data:
	tls.crt: base64 encoded cert
	tls.key: base64 encoded key
type: kubernetes.io/tls
```

---

## Helm
* Package manager for kubernetes
	* Packages yaml files and distributes them in a private/public registry
* Helm Chart
	* Bundle of YAML files held by helm repositories
	* Can be shared in public repositories
* Templating engine
	* helm allows creating configuration templates to be used to deploy multiple services
	* A values file defines a set of values that can be used in template files (accessed with `{{.Values.VALUE_NAME}}`)
* Directory structure consists of 4 main things
	* `chart.yaml`: Meta information about charts
	* `values.yaml`: Values for the template files
	* `charts/`: Folder that contains chart dependencies
	* `templates/`: Folder that stores template files
* helm allows overriding the default values for a specific deployment using the following command
	* `helm install --values=new_values.yaml CHART_NAME`
	* The values stored in `new_values.yaml` will override the values stored in `values.yaml`.


---

## Stateful vs stateless applications
### Stateless application
* Any pod can be deleted/restarted, as it does not store state
* Pods are interchangeable
	* They get random hashes
	* Load balancer can send requests to any of the pods

### Stateful application
* Pods cannot be deleted randomly and cannot be addressed randomly, as they store state
* Cannot be created/deleted at the same time
	* Replica pods are not identical
* Created from the same specification, but are not identical
* With stateful pods, there is one pod that writes to the database (called the master). All other pods can only read from the database (called the slaves, although this term is old and should no longer be used, due to its implications)
	* Masters and slaves do not have access to the same physical storage
	* Slave Pods must be synchronised with master
	* Stateful set pods get fixed names, where each new pod is assigned an ordinal number in increasing order (e.g mysql-0, mysql-1). The first pod is the master pod.
	* Pods get deleted in reverse order to their sequence numbers


---

# Sources
* Concepts: https://kubernetes.io/docs/concepts/overview/components/
* Objects in Kubernetes: https://kubernetes.io/docs/concepts/overview/working-with-objects/
* Amazing video: https://www.youtube.com/watch?v=X48VuDVv0do
