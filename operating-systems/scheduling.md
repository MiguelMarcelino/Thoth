# Scheduling

## Overview

Scheduling is how the operating system decides which process or thread runs on the CPU at a given time.
Since there are usually more runnable tasks than CPU cores, the scheduler allocates time fairly and efficiently.

## Key Concepts

* CPU burst: time a process spends running before yielding or waiting.
* I/O burst: time spent waiting for I/O (disk, network).
* Preemptive scheduling: OS can interrupt and switch tasks.
* Non-preemptive scheduling: process runs until it finishes or blocks.

## Common Algorithms

| Algorithm                      | Description                     | Use Case                     |
| ------------------------------ | ------------------------------- | ---------------------------- |
| FCFS (First Come First Served) | Run in arrival order            | Simple, can cause long waits |
| SJF (Shortest Job First)       | Shortest burst first            | Minimizes average wait time  |
| Priority Scheduling            | Higher priority first           | Used in real-time systems    |
| Round Robin                    | Fixed time slice (quantum)      | Fair sharing among tasks     |
| Multilevel Queue               | Different queues for priorities | Used in modern OS schedulers |

## Metrics

* Throughput: processes completed per unit time
* Turnaround time: total time from submission to completion
* Waiting time: time spent in ready queue
* Response time: time until first CPU response

<hr>

Related to: [operating-systems](operating-systems)