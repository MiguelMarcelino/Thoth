# Deadlocks

## Overview

A deadlock occurs when two or more processes wait for each other indefinitely, each holding a resource the other needs.

## Four Conditions (must all hold)

1. Mutual exclusion — resources can’t be shared.
2. Hold and wait — processes hold resources while waiting for others.
3. No preemption — resources can’t be forcibly taken.
4. Circular wait — a cycle of waiting processes exists.

## Handling Methods

| Strategy             | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| Prevention           | Ensure at least one condition above never holds                   |
| Avoidance            | Use algorithms (e.g., Banker's) to check safe states              |
| Detection & recovery | Allow deadlocks, then detect and fix                              |
| Ignorance            | Assume they are rare; restart affected processes (common in OSes) |

<hr>

Related to: [operating-systems](../operating-systems)