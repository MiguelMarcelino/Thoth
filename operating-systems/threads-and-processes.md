# Threrads and Processes

## What is a Process?

A process is an independent execution unit that has:

* its own memory space (address space)
* its own CPU registers and stack
* and resources such as open files, sockets, etc.

Each process runs in isolation - one process cannot directly access another’s memory (the OS enforces that isolation).

### Key properties

| Property      | Description                                                      |
| ------------- | ---------------------------------------------------------------- |
| Memory space  | Unique, isolated                                                 |
| Communication | Inter-process communication (IPC): pipes, sockets, shared memory |
| Failure       | If one process crashes, others continue                          |
| Creation      | Expensive - OS must allocate new memory and resources            |


## What is a Thread?

A thread is a smaller execution unit *within a process*.

All threads in the same process:

* share the same memory and resources
* have their own stack and registers
* can run concurrently on multiple CPU cores

That shared memory allows threads to communicate easily (by reading/writing shared data structures), but it also means you must manage synchronization (locks, semaphores, etc.) to avoid race conditions.

### Key properties

| Property      | Description                                    |
| ------------- | ---------------------------------------------- |
| Memory space  | Shared within process                          |
| Communication | Simple - shared variables                      |
| Failure       | If one thread crashes, process may crash       |
| Creation      | Cheap - no new memory allocation, just a stack |


## Relevant Points

* Processes provide isolation → safer but heavier.
* Threads provide concurrency → faster but riskier (need locks).
* Context switching between threads/processes has overhead (less for threads).
* Synchronization tools: mutexes, semaphores, condition variables.
* CPU-bound vs I/O-bound tasks:
  * CPU-bound → use multiprocessing or async I/O.
  * I/O-bound → threads are fine since they can overlap waiting.

<hr>

Related to: [operating-systems](operating-systems)