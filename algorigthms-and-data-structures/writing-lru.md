# Writing an LRU

Interview-friendly solution is:
- Keep a hash map from key → node (O(1) lookup), and
- a doubly-linked list of nodes ordered by recency (head = most recent, tail = least recent) so you can move nodes to front and evict the tail in O(1).


# Design (brief)

* `get(key)`:
  * if key not in map → return -1 / miss.
  * else move node to head (mark most recently used) and return node.value.
* `put(key, value)`:
  * if key exists → update value, move node to head.
  * else create node, insert at head and add to map.
  * if size > capacity → remove tail node and delete from map.

All operations are O(1). Doubly-linked list allows removal/move in O(1) with node pointers.

# Python implementation (explicit DLL + dict)

```python
class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.map = {}           # key -> Node
        # dummy head and tail to avoid edge cases
        self.head = Node(None, None)  # most recent after head
        self.tail = Node(None, None)  # least recent before tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # internal helpers
    def _add_node_to_head(self, node: Node):
        # insert right after head
        node.prev = self.head
        node.next = self.head.next

        # We need to insert a new node between HEAD and the previous node
        # Example
        #  Before: HEAD -> A
        #  After: HEAD -> Node -> A
        #  But A still thinks prev is HEAD, so we need to update 
        # prev for self.head.next (which is A) 
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        # Essentially, all neighbour nodes skip the node and 
        # we set all references on the node to remove to None.
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = node.next = None

    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node_to_head(node)

    def _pop_tail(self) -> Node:
        # removes and returns the real tail node
        if self.tail.prev is self.head:
            return None
        node = self.tail.prev
        self._remove_node(node)
        return node

    # public API
    def get(self, key):
        node = self.map.get(key)
        if not node:
            return -1
        # move accessed node to head (most recent)
        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        node = self.map.get(key)
        if node:
            # update and move to front
            node.val = value
            self._move_to_head(node)
            return

        # create new
        new_node = Node(key, value)
        self.map[key] = new_node
        self._add_node_to_head(new_node)
        self.size += 1
        if self.size > self.capacity:
            tail = self._pop_tail()
            if tail:
                del self.map[tail.key]
                self.size -= 1

    # optional convenience
    def __len__(self):
        return self.size

    def keys_in_order(self):
        # returns list of keys from most recent to least recent (helpful for tests)
        res = []
        cur = self.head.next
        while cur is not self.tail:
            res.append(cur.key)
            cur = cur.next
        return res
```

### Quick example

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1        # returns 1, order becomes [1,2]
cache.put(3, 3)                 # evicts key 2, order [3,1]
assert cache.get(2) == -1
cache.put(4, 4)                 # evicts key 1, order [4,3]
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
```


# Complexity

* `get` — O(1)
* `put` — O(1)
* Space — O(capacity)

(Assuming hash ops are O(1).)


# Extensions & interview follow-ups to mention

* **Thread-safety / concurrency**: add a lock (coarse-grained) or use concurrent structures + separate eviction logic. In Java, use `ConcurrentHashMap` + a concurrent deque or use `LinkedBlockingDeque` and careful coordination. Or wrap operations with `synchronized`.
* **TTL / expiry**: store timestamps in nodes and lazily evict expired items on access or run background cleanup.
* **Sharding**: for higher throughput, use multiple LRU shards (e.g., N copies) and hash keys to a shard — reduces lock contention.
* **Persistence**: write-through vs write-back behavior if caching DB writes.
* **Memory limits**: base eviction on memory usage instead of item count (store sizes).
* **Cache stampede protection**: use request coalescing or locks per key to avoid many clients regenerating the same value.
* **LFU or segmented LRU (TinyLFU, ARC)**: discuss tradeoffs when frequency matters vs pure recency.
* **Eviction tie-breakers / weighting**: sometimes items have different sizes or priorities.

<hr>

Related to: [algorithms-and-data-structures](algorithms-and-data-structures)