# Sliding window

A sliding window is a contiguous subarray of size `k` (or with constraints, e.g., sum ≤ target) that "slides" over the array.

Why it matters:

* Helps compute aggregates efficiently (sum, max, min) over subarrays.
* Models real-world streams, e.g., last N requests, throughput over a time window.
* Often used in rate limiters, moving averages, network monitoring.

## 2. Common Patterns

### A. Fixed-Size Window

* Window has a fixed size `k`.
* Move left and right pointers to maintain the window.
* Example: Max sum of any subarray of size `k`.

```python
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]  # slide window forward
        max_sum = max(max_sum, window_sum)
    return max_sum
```


### B. Variable-Size / Condition Window

* Window size changes depending on a condition (sum ≤ target, at most k distinct elements).
* Use two pointers, sometimes a hash map to track counts.

```python
def longest_subarray_with_k_distinct(nums, k):
    count = {}
    left = 0
    max_len = 0
    for right, val in enumerate(nums):
        count[val] = count.get(val, 0) + 1
        # If adding val made the window have more than k distinct elements, 
        # the while loop runs. This shrinks the window from the left 
        # until len(count) <= k.
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            # left can never bypass the array length because it only increments 
            # while left < right within the for loop.
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
```

With the implementation above, the longest valid subarray we find will always end at the rightmost elements that fit within k distinct values. In other words, it won’t include earlier elements once the window exceeds k, because the while loop removes them.


### C. Real-World Analogy (Rate Limiting / Moving Metrics)

* Treat each request as a timestamp in a queue.
* Maintain a window of size T seconds (or N requests).
* Remove items from the front of the queue that fall outside the window.
* Check if new request can proceed → rate limiting logic.

```python
from collections import deque
import time

class RateLimiter:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window = window_seconds
        self.requests = deque()

    def allow_request(self):
        now = time.time()
        while self.requests and self.requests[0] <= now - self.window:
            self.requests.popleft()
        if len(self.requests) < self.limit:
            self.requests.append(now)
            return True
        return False
```


## 3. Key Points

* Two-pointer / deque pattern → efficient O(n) solution instead of O(n²).
* Edge cases: empty array, k > n, all duplicates.
* Real-world relevance: streaming data, monitoring, rate-limiting.
* Optimizations:
  * Use deque to maintain max/min in sliding window in O(n) (monotonic queue).
  * For variable windows, hash map helps track frequency or counts.

### About Deque
A deque (double-ended queue) is a linear data structure that allows insertion and deletion at both ends in O(1) time. Unlike a standard queue or stack, it supports both FIFO and LIFO operations efficiently. It is often implemented using a doubly linked list or a circular buffer.


<hr>

Related to: [stacks-and-queues](stacks-and-queues)
