---
layout: slide
title: Introduction to OS
category: presentation
---

<section data-markdown>
## <center> Introduction to Operating Systems </center>
</section>

<section data-markdown>
### What happens when a computer program run? (*in a nutshell!*)

- The processor
  - **fetches** an instruction from memory
  - **decodes** the instruction
  - **executes** the instruction
- This is the fundamental **Von Neumann** model of computing
</section>

<section data-markdown>
### Why?

![von-neumann]({{ "/assets/images/csc-331/intro_os/von_neumann.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### How? Virtualization

- **Virtualization**
  - Presents general, powerful, and easy-to-use **virtual** forms of **physical** computing resources to users (*programmers*).
- The linkage between virtual interfaces and physical components are enabled through the OS' **system calls** (or **standard library**).
</section>

<section data-markdown>
### How? Managing Resources
- Each physical component in a computing system is considered a **resource**.
- The OS **manages** these resources so that multiple programs can assess these resources (through the corresponding virtual interface) at the same time (**concurrency**)
</section>

<section data-markdown>
### Hands-on
- Start virtualbox
- Start the *csc-331* VM
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

### Compile and Run

```
$ cd /home/student/ostep-code/intro/
$ gcc -o cpu cpu.c -Wall
$ ./cpu "A"
```

To interrupt a running program, press `Ctrl-C`

</section>

<section data-markdown>

![cpu]({{ "/assets/images/csc-331/intro_os/cpu.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Making things more interesting

Before running the Linux command on this slide, take notes on the following:

- How many CPU did we assign to the VM?

```
$ (./cpu "A" &) ; (./cpu "B" &) ; (./cpu "C" &); (./cpu "D")
```

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
### Making things more interesting

![multi-mem]({{ "/assets/images/csc-331/intro_os/multi-mem.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

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

![threads]({{ "/assets/images/csc-331/intro_os/threads.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

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
### Making things more interesting

![threads-lock]({{ "/assets/images/csc-331/intro_os/thread-lock.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

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

<section data-markdown>
### The Modern Era

- Personal Computer
- **DOS**: The Disk Operating System
- **Mac OS**
- Multics (MIT)/UNIX (Bell Labs)/BSD (Berkeley)/Sun OS/Linux

</section>
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
