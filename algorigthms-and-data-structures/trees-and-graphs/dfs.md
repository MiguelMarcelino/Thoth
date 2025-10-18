
## 3. DFS (Depth-First Search)

Purpose: Explore a graph deeply before backtracking.
Use case in networking:

* Detect cycles, connected components, or vulnerable paths.
* Useful for topology analysis and dependency checks.

Python snippet:

```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

<hr>

Related to: [trees-and-graphs](trees-and-graphs)