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
- The linkage between virtual interfaces and physical components are enabled through the OS' **system calls** (or **standrad library**).
</section>

<section data-markdown>
### How? Managing Resources
- Each physical component in a computing system is considered a **resource**.
- The OS **manages** these resources so that multiple programms can assess these resources (through the corresponding virtual interface) at the same time (**concurrency**)
</section>

<section data-markdown>
### Hands-on
- Start virtualbox
- Start the *csc-331* VM
</section>

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

To interrup a running program, press `Ctrl-C`

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

- A limated number of physical CPUs can still be represented as infinite number of CPUs through **virtualization**
- The OS will **manage** the scheduling and allocation of the actual run on physical resources.
-
</section>

<section data-markdown>
### How to stop the programs ...

- First, hit `Ctrl-C`
- Ignore the scrolling text, and type `ps aux | grep cpu`
- Identify the process numbers associated with the corresponding runs for A, B, and C
- Enter `kill <process_number`

</section>

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

To interrup a running program, press `Ctrl-C`

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
