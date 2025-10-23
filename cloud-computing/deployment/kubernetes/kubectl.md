# Kubectl

Kubectl is a command line tool for communicating with a [Kubernetes](cloud-computing/deployment/kubernetes/kubernetes.md) cluster's control plane, using the Kubernetes API.

---
## Installation

### On Windows (PowerShell)
Install Kubectl with **Chocolatey** ([[chocolatey]]):
```
choco install kubernetes-cli
```

### On Linux
> [!INFO] Installing on WSL2
> On WSL2 it's recommended to install Docker Desktop [[docker-desktop]], which automatically comes with kubectl.
1. Download the latest release
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"  
```

2. Install Kubectl
```bash
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### On mac OS
Install Kubectl with **Homebrew ([[homebrew]])**:
```zsh
brew install kubernetes-cli
```

---
## Commands

### Networking

Connect containers using Kubernetes internal DNS system:
`<service-name>.<namespace>.svc.cluster.local`

Troubleshoot Networking with a netshoot toolkit Container:
`kubectl run tmp-shell --rm -i --tty --image nicolaka/netshoot -- /bin/bash`

### Containers

Restart Deployments (Stops and Restarts all Pods):
`kubectl scale deploy <deployment> --replicas=0`
`kubectl scale deploy <deployment> --replicas=1`

Executing Commands on Pods:
`kubectl exec -it <PODNAME> -- <COMMAND>`
`kubectl exec -it generic-pod -- /bin/bash` 

### Config and Cluster Management
COMMAND | DESCRIPTION
---|---
`kubectl cluster-info` | Display endpoint information about the master and services in the cluster
`kubectl config view` |Get the configuration of the cluster

### Describe commands
COMMAND | DESCRIPTION
---|---
`kubectl describe <resource>` | Describes the state of a resource. 

### Resource Management
COMMAND | DESCRIPTION
---|---
`kubectl get all --all-namespaces` | List all resources in the entire Cluster
`kubectl delete <RESOURCE> <RESOURCENAME> --grace-period=0 --force` | Try to force the deletion of the resource

---
## List of Kubernetes Resources "Short Names"

Short Name | Long Name
---|---
`csr`|`certificatesigningrequests`
`cs`|`componentstatuses`
`cm`|`configmaps`
`ds`|`daemonsets`
`deploy`|`deployments`
`ep`|`endpoints`
`ev`|`events`
`hpa`|`horizontalpodautoscalers`
`ing`|`ingresses`
`limits`|`limitranges`
`ns`|`namespaces`
`no`|`nodes`
`pvc`|`persistentvolumeclaims`
`pv`|`persistentvolumes`
`po`|`pods`
`pdb`|`poddisruptionbudgets`
`psp`|`podsecuritypolicies`
`rs`|`replicasets`
`rc`|`replicationcontrollers`
`quota`|`resourcequotas`
`sa`|`serviceaccounts`
`svc`|`services`


<hr>

## Sources
* Shamelessly copied from Christian Lempa's [cheat sheets](https://github.com/christianlempa/cheat-sheets).
* [Kubectl Reference](https://kubernetes.io/docs/reference/kubectl/)

<hr>

Related to: [kubernetes](cloud-computing/deployment/kubernetes/kubernetes.md)