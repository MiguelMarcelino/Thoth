# Virtual Memory

## Overview

Virtual memory lets processes use more memory than physically available by using disk space as an extension of RAM.
Each process sees a private, continuous address space.

## Key Concepts

* Paging: memory divided into fixed-size pages (commonly 4 KB).
* Page table: maps virtual pages to physical frames.
* Page fault: occurs when required page is not in RAM.
* Swapping: moving pages between disk and RAM.

## Benefits

| Feature     | Description                                 |
| ----------- | ------------------------------------------- |
| Isolation   | Each process has its own address space      |
| Efficiency  | Only active pages stay in RAM               |
| Security    | Processes can’t access each other’s memory  |
| Convenience | Simplifies memory management for developers |

<hr>

Related to: [operating-systems](operating-systems)