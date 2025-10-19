# Dynamic Programming
Dynamic Programming is about breaking a problem into overlapping subproblems, solving each once, and reusing the results.
You trade time for memory by caching results instead of recomputing them.

## Typical Forms

### Top-Down (Memoization)

Use recursion with a cache.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### Bottom-Up (Tabulation)

Iterate and build results from smaller subproblems.

```python
def fib(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```

## Key Points

* Identify overlapping subproblems and optimal substructure.
* Use a hash map or array for caching results.
* Focus on time–space tradeoffs and scalability under constraints.


<hr>

Related to: [hash-tables-and-sets](hash-tables-and-sets)