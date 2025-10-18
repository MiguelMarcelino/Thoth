# Union Find

Purpose: Quickly determine whether nodes are in the same connected component.
Use case in networking: Detect cycles, check connectivity between machines or routers, or merge network segments.

Core idea:

* Each node points to a parent; connected nodes share the same root.
* Supports two operations efficiently (almost O(1) with path compression and union by rank):

  * `find(x)` → find root of node `x`
  * `union(x, y)` → merge two components


```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        # If x has higher rank, it is the parent of y (and vice-versa)
        # If they are in the same rank, we arbitrarily choose one as the new root.
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
```


<hr>

Related to: [trees-and-graphs](trees-and-graphs)
