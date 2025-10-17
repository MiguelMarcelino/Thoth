# Synchronization

## Overview

Synchronization ensures that when multiple threads access shared data, results remain correct.
Without it, race conditions can occur.

## Key Concepts

* Critical section: code that accesses shared resources.
* Mutual exclusion: only one thread executes a critical section at a time.
* Race condition: outcome depends on timing of threads.

## Common Mechanisms

| Mechanism          | Description                                       |
| ------------------ | ------------------------------------------------- |
| Mutex (lock)       | Ensures one thread accesses resource at a time    |
| Semaphore          | Counter-based locking; can control limited access |
| Monitor            | Object-based locking (e.g., Java `synchronized`)  |
| Condition variable | Allows threads to wait for a condition to be met  |
| Atomic operations  | Hardware-level synchronization for simple updates |

<hr>

Related to: [operating-systems](operating-systems)
