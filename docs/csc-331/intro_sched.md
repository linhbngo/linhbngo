---
layout: slide
title: Introduction to Scheduling
category: presentation
---

<section data-markdown>
## <center> CPU Scheduling </center>
</section>


<section data-markdown>
### In a Nutshell

![load_program]({{ "/assets/images/csc-331/intro_sched/diner_dash.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>

<section data-markdown>
### What is processor scheduling?

- The allocation of processors to processes over time
  - Key to **multiprogramming**
  - Increase CPU utilization and job throughput by overlapping I/O and computation
  - Different process queues representing different process states (ready, running, block ...)
- Policies:
  - Given more than one runnable processes, how do we choose which one to run next?
</section>


<section data-markdown>
### Initial set of simple assumptions:

1. Each job (process/thread) runs the **same amount of time**.
2. All jobs **arrive at the same time**.
3. Once started, each job **runs to completion** (no interruption in the middle).
4. All jobs only use the **CPU** (no I/O).
5. The run time of each job is **known**.

These are unrealistic assumptions, and we will relax them gradually to see how it works in a real system. 
</section>


<section data-markdown>
### Minimal list of a modern process API:

- Create: an OS must have methods to create new processes to run the programs.
- Destroy: interface to destroy process forcefully.
- Wait: temporarily pausing the process.
- Miscellaneous Control: suspend and resume processes.
- Status: provide status about the state of the process.
</section>

<section data-markdown>
### Process Creation
When a program is run, the OS performs the following steps:

- Load the program's code and static data into memory (the virtual address space of the process)
- Allocate memory for *run-time stack* (or *stack*).
- Allocate memory for *heap* (used for dynamic memory allocation via *malloc* family).
- Initialization;
  - File descriptor for standard input.
  - File descriptor for standard output.
  - File descriptor for error.
- Begin executing from *main()*.
</section>


<section data-markdown>
### First performance metric

**Average turnaround time of all jobs**

turnaround time = job completion time - job arrival time

</section>


<section data-markdown>
<script type="text/template">
### Algorithm 1: First Come First Serve

| Job | Arrival Time | Service Time |
| A | 0 | 3 |
| B | 0 | 3 |
| B | 0 | 3 |

</script>
</section>


<section data-markdown>
### Algorithm 1: First Come First Serve


|---|---|---|
| Job | Arrival Time | Service Time |
|---|---|---|
| A | 0 | 3 |
| B | 0 | 3 |
| B | 0 | 3 |
|---|---|---|


|---|---|---|---|---|---|---|---|---|---|--- |--- |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|--- |--- | 
| A | A | A |   |   |   |   |   |   |   |    |    |
|---|---|---|---|---|---|---|---|---|---|--- |--- |
| w | w | w | B | B | B |   |   |   |   |    |    |
|---|---|---|---|---|---|---|---|---|---|--- |--- |
| w | w | w | w | w | w | C | C | C |   |    |    |
|---|---|---|---|---|---|---|---|---|---|--- |--- |


</section>


<section data-markdown>
### Process: State Transitions

![state_transition]({{ "/assets/images/csc-331/intro_sched/state_transition.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>





<section data-markdown>
### Hands-on
- Before starting VirtualBox, go to **Settings** of *os-331*, , then **System**, then **Process** and scale the number of processors back down to 1.
</section>


<section data-markdown>
![one-cpu]({{ "/assets/images/csc-331/intro_sched/one_cpu.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
- Start VirtualBox
- Start the *csc-331* VM
</section>


<section data-markdown>
### Github

After log in, if you have not already done so, clone the instructor's Github repository:

```
$ cd ~
$ git clone https://github.com/linhbngo/Operating-Systems.git
```

If you have already cloned the directory, be safe and run a pull on this directory to check for update:

```
$ cd ~/Operating-Systems
$ git pull
```
</section>


<section data-markdown>
### Observing Process State

Change to directory `Operating Systems`, then directory `process`

```
$ cd ~/Operating-Systems/process
$ ls
```
</section>


<section data-markdown>
### Time Sharing

View the source code for `time_sharing.c`, then compile and run. 

```
$ nano time_sharing.c
```
</section>


<section data-markdown>
![time-sharing-code]({{ "/assets/images/csc-331/intro_sched/time_sharing_code.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
After several runs of `a.out`
![time-sharing-code]({{ "/assets/images/csc-331/intro_sched/time_sharing_run.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Time Sharing with Blocked Operation

View the source code for `run_and_wait.c`, then compile and run. 

```
$ nano run_and_wait.c
```
</section>


<section data-markdown>
![time-sharing-code]({{ "/assets/images/csc-331/intro_sched/run_and_wait.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>



<section data-markdown>
### Data Structure

- The OS is a program, thus will use data structures to track different pieces of information. 
- How does the OS track the status of processes?
  - **process list** for all processes.
  - additional information for running process.
  - status of blocked process. 
</section>



<section data-markdown>
### Example: xv6

- Teaching operating system developed by MIT in 2006. 
- https://github.com/mit-pdos/xv6-public

</section>


<section data-markdown>
### Example: xv6

[Register contexts and status definition for a process:](https://github.com/mit-pdos/xv6-public/blob/0754d21c865e97582968fa5d155eac133e5829b0/proc.h)
</section>


<section data-markdown>
### Example: Linux kernal

- [task_struct in sched.h](https://github.com/torvalds/linux/blob/master/include/linux/sched.h)
- [register contexts defined for each process through x86_hw_tss (Hardware Task State Segment)](https://github.com/torvalds/linux/blob/master/arch/x86/include/asm/processor.h)
- [x86 CPU architecture model](https://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture)
</section>

