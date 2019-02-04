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
### C Codes

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


















<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->

<section data-markdown>
<script type="text/template">
### CPU Virtualization

Code location: `/home/student/ostep-code/intro/cpu.c`

```
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

int main(int argc, char *argv[])
{
  if (argc != 2) {
	  fprintf(stderr, "usage: cpu <string>\n");
	  exit(1);
  }
  char *str = argv[1];

  while (1) {
	  printf("%s\n", str);
	  Spin(1);
  }
  return 0;
}
```
</script>
</section>


<section data-markdown>
### Making things more interesting

After running the command, how many programs do you see being run concurrently?

![multi-cpu]({{ "/assets/images/csc-331/intro_os/multi-cpu.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### The illusion of infinite CPU Resources

- A limited number of physical CPUs can still be represented as infinite number of CPUs through **virtualization**
- The OS will **manage** the scheduling and allocation of the actual run on physical resources.
-
</section>

<section data-markdown>
### How to stop the programs ...

- First, hit `Ctrl-C`
- Ignore the scrolling text, and type `ps aux | grep cpu`
- Identify the process IDs associated with the corresponding runs for A, B, and C
- Enter `kill process_ID`

</section>

<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->

<section data-markdown>
<script type="text/template">
### Memory Virtualization

Code location: `/home/student/ostep-code/intro/mem.c`

```
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"

int main(int argc, char *argv[]) {
  if (argc != 2) {
	  fprintf(stderr, "usage: mem <value>\n");
	  exit(1);
  }
  int *p;
  p = malloc(sizeof(int));
  assert(p != NULL);
  printf("(%d) addr pointed to by p: %p\n", (int) getpid(), p);
  *p = atoi(argv[1]); // assign value to addr stored in p
  while (1) {
	  Spin(1);
	  *p = *p + 1;
	  printf("(%d) value of p: %d\n", getpid(), *p);
  }
  return 0;
}
```
</script>
</section>

<section data-markdown>

### Compile and Run

```
$ cd /home/student/ostep-code/intro/
$ gcc -o mem mem.c -Wall
$ ./mem 100
```

To interrupt a running program, press `Ctrl-C`

</section>

<section data-markdown>

![mem]({{ "/assets/images/csc-331/intro_os/mem.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Making things more interesting

Before running the Linux command on this slide, consider the following:

- Will the addresses pointed to by two different running instances of `mem` be the same or different?

```
$ sudo sysctl -w kernel.randomize_va_space=0
$ (./mem 100 &) ; (./mem 200)
```

</section>

<section data-markdown>
### The illusion of dedicated memory resources

- Many running programs share the physical memory space
- From the perspective of each individual program, they access their own **private virtual address space**, which the OS maps onto the physical memory space.
- Memory references within one running program does not affect the address space of others (*except for deliberate memory manipulation*)
</section>

<section data-markdown>
### How to stop the programs ...

- First, hit `Ctrl-C`
- Identify the process ID as they are being printed out
- Enter `kill process_ID`

</section>

<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->


<section data-markdown>
### Concurrency

- As shown in previous examples, the OS needs to manage many running programs at the same time.
- This is called **concurrency**, and it leads to a number of interesting challenges in designing and implementing various management mechanisms within the OS.

</section>

<section data-markdown>
<script type="text/template">
### Concurrency

Code location: `/home/student/ostep-code/intro/threads.c`

```
#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "common_threads.h"

volatile int counter = 0;
int loops;

void *worker(void *arg) {
    int i;
    for (i = 0; i < loops; i++) {
      counter++;
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
      fprintf(stderr, "usage: threads <loops>\n");
      exit(1);
    }
    loops = atoi(argv[1]);
    pthread_t p1, p2;
    printf("Initial value : %d\n", counter);
    Pthread_create(&p1, NULL, worker, NULL);
    Pthread_create(&p2, NULL, worker, NULL);
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("Final value   : %d\n", counter);
    return 0;
}

```
</script>
</section>

<section data-markdown>

### Compile and Run

- `threads.c` creates two functions running at the same time, within the same memory space of the main program.
- A single global variable named `counter` is being increased by both functions, thus the final value of `counter` should be twice that of the command line argument.

```
$ cd /home/student/ostep-code/intro/
$ gcc -o threads threads.c -Wall -pthread
$ ./threads 2000
```

</section>

<section data-markdown>

![threads]({{ "/assets/images/csc-331/intro_os/thread.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Making things more interesting

Before running the Linux command on this slide, consider the following:

- Will the addresses pointed to by two different running instances of `mem` be the same or different?

```
$ sudo sysctl -w kernel.randomize_va_space=0
$ (./mem 100 &) ; (./mem 200)
```

</section>

<section data-markdown>
### What is happening ...

- Concurrency gives you wrong results.
- Concurrency gives you wrong and inconsistent results.

</section>

<section data-markdown>
### Why does this happen?

- At machine level, incrementing `counter` involves three steps:
  - Load value of counter from memory into register,
  - Increment this value in the register, and
  - Write the value of counter back to memory.
- What should have happened:
  - One thread increments `counter` (all three steps), then the other thread increments `counter`, now with the updated value.
- What really happened:
  - One thread increments `counter`.
  - While this thread has not done with all three steps, the other thread steps in and attempt to increment the *stale* content of `counter` in memory.
</section>

<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->

<section data-markdown>
### Persistence

- When the programs stop, everything in memory goes away: `counter`, `p`, `str`.
- Physical components to store information **persistently** are needed.
- **Input/output** or **I/O** devices:
   - Hard drives
   - Solid-state drives
- Software managing these storage devices is called the **file system**.
- Examples of **system calls/standard libraries** supporting the file system:
  - open()
  - write()
  - close()
</section>

<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->

<section data-markdown>
## <center> Some History </center>

- [The Evolution of Operating Systems](https://pdfs.semanticscholar.org/969e/ffe7509150634b2c9cd74157bb6804a8d438.pdf)

</section>

<section data-markdown>
### Early Operating Systems: Just Libraries

- Include only library for commonly used functions.
- One program runs at a time.
- Manual loading of programs by operator.
</section>


<section data-markdown>
### Beyond Libraries: Protection

- System call
- Hardware privilege level
- User mode/kernel mode
- **trap**: the initiation of a system call to raise privilege from user mode to kernel mode
</section>

<section data-markdown>
### The Era of Multiprogramming

- Minicomputer
- **multiprogramming**: multiple jobs being run with the OS switching among them
- Memory protection
- Concurrency

</section>
