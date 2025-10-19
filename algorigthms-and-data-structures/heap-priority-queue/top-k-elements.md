# Top K elements
Top K Frequent Elements is a classic heap problem. It tests whether you can balance hash maps (for counting) with heaps (for prioritization) efficiently.

## Problem

Given an array of integers `nums` and an integer `k`, return the `k` most frequent elements.

Example:

```python
nums = [1,1,1,2,2,3], k = 2
# Output: [1, 2]
```


## Intuition

We need to:

1. Count occurrences of each number.
2. Retrieve the top `k` with the highest frequencies.

Sorting all elements by frequency is O(n log n),
but a heap can give O(n log k) — faster for large `n`.


## Solution (Using Min-Heap)

```python
# Notice that heapq in Python is a min-heap so we need to, 
# pop the smallest frequency when the heap exceeds `k`.
import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)  # Step 1: Count frequencies
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))  # Push (freq, num)
        if len(heap) > k:                  # Keep only k most frequent
            heapq.heappop(heap)

    return [num for (freq, num) in heap]
```

## Step-by-Step Example

`nums = [1,1,1,2,2,3], k = 2`

1. Frequency map → `{1: 3, 2: 2, 3: 1}`
2. Push `(3,1)` → heap = `[(3,1)]`
   Push `(2,2)` → heap = `[(2,2),(3,1)]`
   Push `(1,3)` → heap = `[(2,2),(3,1),(1,3)]` → pop `(1,3)` → heap = `[(2,2),(3,1)]`
3. Final heap → contains the 2 most frequent elements → `[2,1]`


## 4. Key Points

* Time complexity: O(n log k)
* Space complexity: O(n)
* It is advantageous to chose a heap over sorting, as it is more efficiency for larger inputs

<hr>

Related to: [heap-priority-queue](heap-priority-queue)
