---
layout: slide
title: Process API
category: presentation
---

<section data-markdown>
## <center> Process API: fork(), exec(), and wait() </center>
</section>

<section data-markdown>
### fork()

- Is a system call.
- Is used to create a new process.
- https://linux.die.net/man/2/fork
</section>


<section data-markdown>
- Start VirtualBox
- Start the *csc-331* VM
</section>


<section data-markdown>
- Change directory to `~/ostep-code/cpu-api` and view `p1.c`

```
$ cd ~/ostep-code/cpu-api
$ nano -c p1.c
```
</section>

<section data-markdown>
### p1.c

- prints out *hello world* and the process identifier (**pid**).
- calls *fork()*, which initiate the creation of a new process.
  - The new process is an almost *exact copy* of the calling process. 
  - The new process does not start at *main()*, but begins immediately after *fork()*.
  - The new process receives a return code of 0 from *fork()*.
  - The calling process receive the **pid** of the new process. 
</section>


<section data-markdown>
Compile and run p1.c

![p1]({{ "/assets/images/csc-331/process_api/p1.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>

<section data-markdown>
### fork() and wait()

- The manual page has a clearer explanation comparing to the book. 
- http://man7.org/linux/man-pages/man2/wait.2.html
</section>


<section data-markdown>
- Inside `~/ostep-code/cpu-api` and view `p2.c`

```
$ cd ~/ostep-code/cpu-api
$ nano -c p2.c
```
</section>


<section data-markdown>
- Compile and run p2.c
- What is the difference?
</section>


<section data-markdown>
![p2]({{ "/assets/images/csc-331/process_api/p2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### exec()

-*fork()* lets you create and run a copy of the original program.
-*exec()* lets you run a different program. 
- https://linux.die.net/man/3/exec
</section>


<section data-markdown>
- Inside `~/ostep-code/cpu-api` and view `p3.c`

```
$ cd ~/ostep-code/cpu-api
$ nano -c p3.c
```
</section>


<section data-markdown>
- Compile and run p3.c
- What seems to be missing?
</section>


<section data-markdown>
![p3]({{ "/assets/images/csc-331/process_api/p3.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Hint: Read the first sentence of the description of exec() in the manual
</section>


<section data-markdown>
### Why fork(), wait(), and exec()

- The separation of fork() and exec() is essential to the building of a UNIX shell. 
- It let the shell run code **after** the call to *fork()*, but **before** the call to *exec()*.
- Facilitate a number of interesting features in the UNIX shell. 
</section>


<section data-markdown>
### The shell?

- What is the shell?
  - https://kb.iu.edu/d/agvf
</section>


<section data-markdown>
### The shell?

**What is the running shell?**

</section>


<section data-markdown>
### The shell?

- In a running shell, if we want to run a program, we are essentially:

**asking a ???? to create and run another ????**
</section>


<section data-markdown>
### The shell?

- In a running shell, if we want to run a program, we are essentially:

**asking a process to create and run another process**
</section>


<section data-markdown>
### When you run a program from the **prompt**, the shell ...

- finds out where the program is in the file system. 
- calls *fork()* to create a new child process to run the command.
- calls one of *exec()* family to run the command. 
- calls *wait()* to wait for the child process to finish before giving user the **prompt** again. 
</section>


<section data-markdown>
### Why don't we just call exec() instead of fork()?
</section>


<section data-markdown>
Run the following command in the terminal:

```
$ cd ~/ostep-code/cpu-api
$ wc p3.c
$ wc p3.c > newfile.txt
$ cat newfile.txt
```
</section>


<section data-markdown>
### What happened?
</section>


<section data-markdown>
### How did it happen?
</section>


<section data-markdown>
### When you run `wc p3.c > newfile.txt` from the **prompt**, the shell ...

- finds out where `wc` is in the file system. 
- prepares `p3.c` as an input to `wc`.
- calls *fork()* to create a new child process to run the command.
- recognizes that `>` represents a **redirection**, thus closes the file descriptor to **standard output** and replaces it with a file descriptor to `newfile.txt`.
- calls one of *exec()* family to run `wc p3.c`. 
  - output of `wc p3.c` are now send to `newfile.txt`.
- calls *wait()* to wait for the child process to finish before giving user the **prompt** again. 
</section>

<section data-markdown>
- Inside `~/ostep-code/cpu-api` and view `p4.c`

```
$ cd ~/ostep-code/cpu-api
$ nano -c p4.c
```
</section>


<section data-markdown>
- Compile and run p4.c
</section>


<section data-markdown>
![p4]({{ "/assets/images/csc-331/process_api/p4.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Similar principle, the UNIX pipe:

How many processes are being run by the `student` account?

```
$ ps aux
$ ps aux | grep student
$ ps aux } grep student | wc -l
```

http://man7.org/linux/man-pages/man2/pipe.2.html
</section>


<section data-markdown>
### Other system calls:

- `kill()`: send **signals** to a process, including directive to pause, die, and other imperatives. 
  - http://man7.org/linux/man-pages/man2/kill.2.html
  - `SIGINT`: signal to terminate a process
  - `SIGTSTP`: pause the process (can be resumed later). 
- `signal()`: to *catch* a signal. 
  - http://man7.org/linux/man-pages/man7/signal.7.html
</section>