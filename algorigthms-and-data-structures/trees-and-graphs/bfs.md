# BFS (Breadth-First Search)

Purpose: Explore a graph layer by layer (shortest path in unweighted graphs).
Use case in networking:

* Find the shortest route between two nodes (machines, routers).
* Discover all nodes reachable from a starting point.

Python snippet:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

<hr>

Related to: [trees-and-graphs](trees-and-graphs)
