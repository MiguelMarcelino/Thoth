# Heap/Priority Queue

A heap is a tree-based structure where the smallest (min-heap) or largest (max-heap) element can be accessed in O(1) and inserted/removed in O(log n).
Used to efficiently manage items by priority - such as jobs, requests, or metrics.

## 2. Typical Use Cases

### Scheduling / Rate Control

Used to process tasks based on time or priority.

```python
import heapq, time

def schedule_tasks(tasks):
    # tasks = [(timestamp, task_name)]
    heapq.heapify(tasks)
    while tasks:
        ts, name = heapq.heappop(tasks)
        if ts > time.time():
            time.sleep(ts - time.time())
        print("Running:", name)
```

Why: Lets you handle the next due task efficiently.

### Top-K Metrics (Streaming or Analytics)

Keep track of the K largest (or smallest) items from a stream.

```python
import heapq

def top_k(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

Why: Constantly maintains the top-K elements without sorting the entire stream.

### Merging or Ordering Streams

Used when combining multiple ordered data sources (e.g., logs from several servers).
Leverage a min-heap keyed by timestamp or sequence number.

## Complexity

* Insert: O(log n)
* Pop: O(log n)
* Peek: O(1)

Don't forget that we need to re-heapify after updating items.

<hr>

Related to: [algorithms-and-data-structures](algorithms-and-data-structures)
