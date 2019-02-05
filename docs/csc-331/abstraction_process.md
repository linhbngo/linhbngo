---
layout: slide
title: Process Abstraction
category: presentation
---

<section data-markdown>
## <center> The Abstraction: Process </center>
</section>

<section data-markdown>
### What is a program?

- A program is a static list of instructions and data.
  - When a program runs, the OS takes this list and asks the CPU to execute them.
  - If we only have one CPU, how can we run more than one program at a time?
</section>

<section data-markdown>
### What is a process?

- A process is a **running program**.
- But the program itself is not runnning ...
  - A process is an asbtraction provided by the OS to describe the running of a program.
- what is a process made of?
  - Memory that the process (running program) can address.
  - Memory registers.
  - Programm counter.
  - Stack pointer.
  - Frame pointer.
  - I/O devices
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
### Loading: From Program to Process

![load_program]({{ "/assets/images/csc-331/abstraction_process/load_program.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Process States

- Running: the processor is executing a process' instructions.
- Ready: the process is ready to run, but the OS is not running the process at the moment.
- Blocked: the process has to performed some operation (e.g., I/O request to disk) that makes it not ready to run.
</section>


<section data-markdown>
### Process: State Transitions

![state_transition]({{ "/assets/images/csc-331/abstraction_process/state_transition.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Process: State Transition

- When a process moves from *ready* to *running*, this means that it has been *scheduled* by the OS.
- When a proess is moved from *running* to *ready*, this mean that it has been *descheduled* byt the OS.
- Once the process is *blocked* (initiating I/O), it will be kept from becoming *ready* by the OS, until some events occur (I/O completion signal)
</section>


<section data-markdown>
### Hands-on
- Before starting VirtualBox, go to **Settings** of *os-331*, , then **System**, then **Process** and scale the number of processors back down to 1.
</section>


<section data-markdown>
![one-cpu]({{ "/assets/images/csc-331/abstraction_process/one_cpu.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
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
![time-sharing-code]({{ "/assets/images/csc-331/abstraction_process/time_sharing_code.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
After several runs of `a.out`
![time-sharing-code]({{ "/assets/images/csc-331/abstraction_process/time_sharing_run.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Time Sharing with Blocked Operation

View the source code for `run_and_wait.c`, then compile and run. 

```
$ nano run_and_wait.c
```
</section>


<section data-markdown>
![time-sharing-code]({{ "/assets/images/csc-331/abstraction_process/run_and_wait.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
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

