---
layout: slide
title: Limited Direct Execution
category: presentation
---

<section data-markdown>
## <center> Limited Direct Execution  </center>
</section>

<section data-markdown>
### CPU Virtualization Recall

- A single physical CPU can support the illusion of having multiple processes running concurrently.
- The sharing of the CPU among these processes is *time-sharing*.
</section>


<section data-markdown>
### Design Goals of CPU Virtualization

- Performance
  - The process can be itself and run as fast as possible without frequent interaction with the OS.
- Control
  - We want to avoid the scenario where a process can run forever and take over all the machine's resources or a process performs unauthorized actions. This requires interaction with the OS.
</section>


<section data-markdown>
### How to efficiently virtualize the CPU with control, that is the question.

- Efficiently
- Control
</section>

<section data-markdown>
### Efficient

- The most efficient way to execute a process is through direct execution.

</section>


<section data-markdown>
![dm]({{ "/assets/images/csc-331/limited_direct_execution/direct_execution.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>

<section data-markdown>
### Problem with direct execution

- Once the program begins to run, the OS becomes a complete outsider
  - No control over the running program.
  - The program can access anything it wants to, including **restricted operations** (direct access to hardware devices, especially I/O for unauthorized purposes - think *sudo for all*).
  - The program may never **switch** to a different process without explicit. instructions in **main()**, thus defeating the purposes of **time-sharing**.
</section>


<section data-markdown>
### Problem with direct execution: Restricted Operations

- The process should be able to perform restricted operations, such as disk I/O, open network connections, etc.
- But we should **not** give the process **complete control** of the system.
- Reiteration: The process should be able to have its restricted operations performed.
- Solution: hardware support via processor modes:
  - User mode
  - Kernel mode
</section>


<section data-markdown>
### Process modes

- A **mode bit** is added to hardware to support distinguishing between user mode and kernel mode.
- Some instructions are designated as **privileged instructions** that cannot be run in user mode (only in kernel mode).
  - A user-mode process trying to perform privileged instructions will raise a *protection-=fault* and be killed.
- How can these instructions be called by a process in user-mode?
  - **System call**
</section>


<section data-markdown>
### System calls

- A **small** set of APIs for restricted operations
  - [XV6 system calls](https://github.com/mit-pdos/xv6-public/blob/master/syscall.h)
  - Linux x86_64 has 335 systems called (0 to 334) - Spring 2019
  - Linux uses a sys_call_table to keep the syscall handlers.
  - [syscall_64.tbl](https://github.com/torvalds/linux/blob/6f0d349d922ba44e4348a17a78ea51b7135965b1/arch/x86/entry/syscalls/syscall_64.tbl)
- These system calls enable user-mode process to have restricted operations performed without having to gain complete control over the system.
</section>


<section data-markdown>
### How does a system call happen?

- To make a system call, the process need to switch form user mode to kernel mode, do the privileged operation, and then switch back.
- This is done through hardware support
  - Require assembly instructions
  - **trap**: go from user mode to kernel mode.
  - **return-from-trap**: go back from kernel mode to user mode.

</section>


<section data-markdown>
![de2]({{ "/assets/images/csc-331/limited_direct_execution/de2.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Example: Linux write system call
</section>


<section data-markdown>
![write]({{ "/assets/images/csc-331/limited_direct_execution/write.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### System calls versus normal C calls

- Function declarations are the same.
- System calls
  - have **trap instruction** in them.
  - have extra level of indirection (movements between modes).
  - perform restricted operations
  - have bigger overhead and are slower than equivalent function calls.
  - can use kernel stack.
</section>


<section data-markdown>
### System call naming:

- User space definition:
  - [libc's definition for *write()*](https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=io/write.c;hb=HEAD)
- Kernel definition:
  - [Linux definition for *write()*](https://github.com/torvalds/linux/blob/74673fc50babc9be22b32c4ce697fceb51c7671a/include/linux/syscalls.h)
- The user space definition will eventually call the kernel definition.
</section>


<section data-markdown>
### Problem with direct execution: Switching process

- A free running process may never stop or switch to another process.
- OS needs to control the process, but how?
  - Once a process is running, OS is NOT running (OS is but another process)
- The question: How can OS **regain control** of the CPU from a process so that it can switch to another process?
</section>


<section data-markdown>
### First approach: Cooperative processes

- The OS trusts the processes to behave cooperatively
  - A process that runs for too long would voluntarily give up the CPU and hand control to the OS.
  - This is done by the process making a **yield()** system call periodically.
  - When process performs an invalid/illegal operation (Exception raised).
</section>


<section data-markdown>
### First approach: Cooperative processes

- All programmers promise to insert **yield()** into their code to give up CPU resources to other people's program.
  - We have solved the second problem and achieved eternal world peace.
- Even in a perfect world, what happens if a process falls into an infinite loop prior to calling **yield()**?
  - [Collaborative multitasking (Windows 3.1X, Mac PowerPC)](https://en.wikipedia.org/wiki/Cooperative_multitasking)
</section>


<section data-markdown>
### When you run a program from the **prompt**, the shell ...

- finds out where the program is in the file system.
- calls *fork()* to create a new child process to run the command.
- calls one of *exec()* family to run the command.
- calls *wait()* to wait for the child process to finish before giving user the **prompt** again.
</section>


<section data-markdown>
### Second approach: Non-cooperative Processes

- Similar to processor modes, the hardware once again provided assistance via **Timer Interrupt**.
- A timer device can be programmed to raise an interrupt periodically.
- When the interrupt is raised, the running process stops, a pre-configured interrupt handler in the OS runs.
- The OS regains control.
</section>


<section data-markdown>
### Second approach: Non-cooperative Processes

- The OS first decides which process to switch to (with the help from the **scheduler**)
- The OS executes a piece of assemble code (context switch.
  - Save register values of the **currenlty running** process into its kernel stack.
  - Restore register values of the **soon running** process from its kernel stack.
</section>


<section data-markdown>
![cw]({{ "/assets/images/csc-331/limited_direct_execution/cw.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>

<section data-markdown>
### Getting down and dirty

We will be working with MIT's XV6 operating system in the future. Perform the following commands in your VM to set up the neccessary infrastructure:

```
$ cd ~
$ sudo apt-get update
$ sudo apt-get install -y qemu
$ sudo apt-get install -y tmux
$ git clone git://github.com/mit-pdos/xv6-public.github
$ cd xv6-public
$ make
$ make qemu-nox
```
To exit from XV6, hit `Ctrl-A` then `X`
</section>
