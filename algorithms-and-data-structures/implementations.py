
###########################################
# K-sum
###########################################

# 2-sum
def two_sum(nums, target):
    seen = set()
    for n in nums:
        if target - n in seen:
            return [n, target - n]
        seen.add(n)

# 3-sum
# Find all unique triplets in an integer array whose sum equals zero, 
# It is used to demonstrate how to efficiently handle pair searching
# and duplicate elimination, and relies on:
# - how to use sorting 
# - two-pointer technique
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l =+ 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

###########################################
# LRU cache
###########################################

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Essentially refresh the node (Goes back to LRU first position)
        self._remove(node)
        self._add(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

###########################################
# Logger rate limiter
###########################################

class Logger:
    def __init__(self):
        self.last_log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_log or timestamp - self.last_log[message] >= 10:
            self.last_log[message] = timestamp
            return True
        return False


###########################################
# Rate Limiting System
###########################################

from collections import deque, defaultdict
import time

class RateLimiter:
    def __init__(self, limit_per_sec: int):
        self.limit = limit_per_sec
        self.requests = defaultdict(deque) # key -> timestamp

    def allow(self, key: str) -> bool:
        now = time.time()
        window = self.requests[key]

        # Remove timestamps older than 1 second
        while window and now - window[0] > 1:
            window.popleft()

        if len(window) < self.limit:
            window.append(now)
            return True

        return False
    
class HierarchicalRateLimiter:
    def __init__(self):
        self.global_limiter = RateLimiter(100)
        self.path_limiter = defaultdict(lambda: RateLimiter(20))
        self.user_path_limiter = defaultdict(lambda: RateLimiter(20))

    def is_rate_limited(self, user_id, path):
        key_user_path = f"{user_id}:{path}"

        if not self.global_limiter.allow("global"):
            return True
        if not self.path_limiter[path].allow(path):
            return True
        if not self.user_path_limiter[key_user_path].allow(key_user_path):
            return True

        return False


###########################################
# Top K Frequent Elements (with heapq)
###########################################

import heapq

def topKFrequent(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    heap = [(-count, num) for num, count in freq.items]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]

# Top K Frequent Elements (without heapq)

def topKFrequentV2(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    
    max_freq = max(freq.values())
    buckets = [[] for _ in range(max_freq + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    res = []
    for i in range(max_freq, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res


###########################################
# Merge K Sorted Lists
###########################################

import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    # We use enumerate here, since we want to use i as a tie-breaker
    # in case there are any duplicates. This is because heapq cannot
    # compare ListNode objects directly
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            # If there is a next, we push that into the queue.
            # Python's heap is implemented as a binary tree, so
            # the next element we get from heappop above will
            # respect ordering.
            heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


###########################################
# Sliding Window Maximum
###########################################

# Problem:
# Given an array nums and a window size k, return an array of the maximum values in each sliding window of size k.
from collections import deque

def maxSlidingWindow(nums, k):
    # While the deque keeps track of the largest elements in the queue,
    # res is what keeps track of the max elements. We use deque to then 
    # extract the largest elements from its first position.
    dq = deque()
    res = []

    for i, n in enumerate(nums):
        # Remove indices outside the window (we always keep k)
        # Example: i = 3, window = [3, -1, -3]
        # Deque dq = [1,2] (indices of 3 and -1)
        # dq[0] = 1 → 1 ≤ 3-3 (false)
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Remove smaller values from the end
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        # Append max of current window
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

###########################################
# URL shortener
###########################################

import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {} # short -> original
        self.reverse_map = {} # original -> short
        self.chars = string.ascii_letters + string.digits
        self.length = 6

    def _generate_short_key(self):
        return ''.join(random.choice(self.chars) for _ in range(self.length))

    def shorten(self, long_url: str) -> str:
        if long_url in self.reverse_map:
            return self.reverse_map[long_url]

        short_key = self._generate_short_key()
        while short_key in self.url_map:
            short_key = self._generate_short_key()

        self.url_map[short_key] = long_url
        self.reverse_map[long_url] = short_key
        return short_key

    def expand(self, short_key: str) -> str:
        return self.url_map.get(short_key, None)

###########################################
# Hit counter
###########################################

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        # If last hit has same timestamp, just increment
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        while self.hits and timestamp - self.hits[0][0] >= 300:
            self.hits.popleft()
        return sum(count for _, count in self.hits)


###########################################
# Move zeroes
###########################################

# Given an integer array nums, move all zeros to the end while maintaining the relative order of the non-zero elements.
# You must do this in place with O(1) extra space.

# The trick here is to not move anything at all. We simply 
# override whatever zeroes we have in the sequence an insert
# them back at the end.

def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

###########################################
# DFS
###########################################

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, node)

###########################################
# BFS
###########################################

def bfs(graph, node):
    visited = set()
    queue = deque([node])
    visited.add(node)

    while queue:
        # deque.popleft() always removes elements from the front,
        # so nodes are processed in the same order they were discovered.
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
