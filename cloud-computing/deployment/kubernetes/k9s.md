# K9s
K9s is a command line interface to easy up managing [Kubernetes](cloud/deployment/kubernetes/kubernetes.md) clusters.

Core features of k9s are, for instance:
- Editing of resource manifests
- Shell into a Pod / Container
- Manage multiple Kubernetes clusters using one tool

## Installation

### On Linux

1. Find and download the latest release

Check the release page [here](https://github.com/derailed/k9s/releases) and search for the fitting package type (e.g. Linux_x86_64). Copy the link to the archive of your choice. Download and unpack the archive like in this example:

```bash
wget https://github.com/derailed/k9s/releases/download/v0.26.6/k9s_Linux_x86_64.tar.gz
tar -xvf k9s_Linux_x86.tar.gz
```

2. Install k9s
```bash
sudo install -o root -g root -m 0755 k9s /usr/local/bin/k9s
```


## Useful shortcuts and commands

| Command     | Comment                                                                        | Compareable kubectl command                                               |
|-------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `:pod`      | Switches to the pod screen, where you can see all pods on the current cluster. | `kubectl get pods --all-namespaces`                                       |
| `:services` | Switches to the service screen, where you can see all services.                | `kubectl get services --all-namespaces`                                   |
| `ctrl`+`d`  | Delete a resource.                                                             | `kubectl delete <resource> -n <namespace>`                                |
| `ctrl`+`k`  | Kill a resource (no confirmation)                                              |                                                                           |
| `s`         | When on the Pod screen, you then open a shell into the selected pod.           | `kubectl exec -n <namespace> <pod_name> -c <container_name> -- /bin/bash` |
| `l`         | Show the log output of a pod.                                                  | `kubectl logs -n <namespace> <pod_name>`                                  |



<hr>

## Sources
* Shamelessly copied from Christian Lempa's [cheat sheets](https://github.com/christianlempa/cheat-sheets).

<hr>

Related to: [kubernetes](cloud/deployment/kubernetes/kubernetes.md)