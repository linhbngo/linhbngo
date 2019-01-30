---
layout: slide
title: Malloc, Struct, and Function
category: presentation
---

<section data-markdown>
## <center> Memory Allocation </center>
</section>


<section data-markdown>
### Pointers and memory allocation

- How does C request dynamic memory when you don't know at compile-time exactly what you will need?
- How does C allocate memory?
  - Automatic: compile arranges for memory to be allocated and initialized for local variables when it is in scope.
  - Static: memory for static variables are allocated once when program starts.
  - Dynamic: memory is allocated on the fly as needed.
</section>


<section data-markdown>
### Dynamic Memory Allocation in C

- Conceptually, it is similar to Java
- But you have to do everything!
</section>


<section data-markdown>
### malloc, free

https://linux.die.net/man/3/malloc
</section>


<section data-markdown>
### What are we returning with void?

- `void*``: pointer to unknown type (JBOB - just a bunch of bytes)
```
#include <stdlib.h>
...
void *p = malloc(100);
...
```
</section>


<section data-markdown>
<script type="text/template">
Typecast

```
/*
* File: hello.c
*/
#include <stdio.h>
int main(int argc, char *argv[]) {
  printf("Hello world!\n");
}
```
</script>
</section>










<section data-markdown>
### Differences

- No classes or objects
- Arrays are simpler:
  - No boundary checking
  - No knowledge of arrays' own size
- Strings are very limited
- No collections, exceptions, or generics
- No memory management
- Pointer!!!
</section>


<section data-markdown>
### How Java works

![java]({{ "/assets/images/csc-331/intro_c/java.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### How C works

![c]({{ "/assets/images/csc-331/intro_c/c.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Hands-on
- Start virtualbox
- Start the *csc-331* VM
</section>


<section data-markdown>
### Setup directory

- Confirm that you are in your `home` directory by typing `pwd` and confirm that you are in `/home/student`.
- Create a new directory named `intro-c`, and then change into that directory.

```
$ mkdir intro-c
$ cd intro-c
```
</section>


<section data-markdown>
![c]({{ "/assets/images/csc-331/intro_c/hello-0.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Editor: nano

- If you know `vim` or `emacs`, feel free to use them.
- Use `nano` for text editing on Linux (assuming you are still in `intro-c` directory from the previous slide:

```
$ nano hello.c
```
</section>


<section data-markdown>
![nano]({{ "/assets/images/csc-331/intro_c/hello-1.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>





<section data-markdown>
![hello]({{ "/assets/images/csc-331/intro_c/hello-2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Save and Quit from nano

- To save and quit, first press `Ctrl-C` to ask to quit
- You will be asked whether to save recent changes (**Y**) or not (**N**)
- If you enter **Y**, you will next be asked for the file name to write, with the default choice is the current filename. If you don't plan to save your changes to a new file, go a head and press `Enter`.
</section>


<section data-markdown>
### What's in the code?
<script type="text/template">
- `/* .. */`: Comments
- `#include <stdio.h>: Standard C library for I/O
- `int main(int argc, char *argv[])`:
  - `int main`: Entry point to the main function, the first function that all C programs will execute.
  - `int argc`: Number of command line arguments (including the C executable itself).
  - `char *argv[]`: Pointer to array of command line arguments (each command line argument is itself an array of characters).
  - `printf("Hello world!\n");`: `System.out.println("Hello world!");
  - `return 0`: Exit a successfully executed program.
</script>
</section>


<section data-markdown>
### Compile and Run: Simple Compilation

- Make sure that you are still inside `/home/student/intro-c` using `pwd`.

```
$ pwd
$ ls
$ gcc hello.c
$ ls
$ ./a.out
```
</section>


<section data-markdown>
![hello-simple]({{ "/assets/images/csc-331/intro_c/hello-3.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Compile and Run: Specify output files

```
$ ls
$ gcc -o hello hello.c
$ ls
$ ./hello
```
</section>


<section data-markdown>
![hello-specific]({{ "/assets/images/csc-331/intro_c/hello-4.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Compile and Run: I want to see everything

```
$ ls
$ rm hello
$ ls
$ gcc -save-temps -o hello hello.c
$ ls
$ ./hello
```
</section>


<section data-markdown>
![hello-all]({{ "/assets/images/csc-331/intro_c/hello-5.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Compile and Run: What are those?

- `hello.i`: generated by pre-processor
- `hello.s`: generated by compiler
- `hello.o`: generated by assembler
- `hello`: executable, generated by linker

</section>


<section data-markdown>
![c]({{ "/assets/images/csc-331/intro_c/c-hello.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>



<section data-markdown>
### What are in those files?

- `hello.i`:

```
$ more hello.i
```

- You can use the `Space` button to move forward, and `q` to quit.
</section>


<section data-markdown>
### What are in those files?

- `hello.s`:

```
$ more hello.s
```
</section>


<section data-markdown>
### What are in those files?

- `hello.o`: we cannot use `more` since this is not a text file.

```
$ xxd -b hello.o | more
```
</section>


<section data-markdown>
### What are in those files?

- `hello`: we cannot use `more` since this is not a text file.

```
$ xxd -b hello | more
```
</section>


<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------->


<section data-markdown>
### <center> Variables, Addresses, and Pointers </center>

- In Java, you cannot do anything to a variable other than get or set its value.
- In C, you can retrieve the address of the location in memory where the variable is stored.
- The operator **&** (reference of) represents the memory address of a variable.

</section>


<section data-markdown>
<script type="text/template">

Inside your `intro-c` directory, create the following C program, name it `pointer-1.c`, compile, and run.

```
#include <stdio.h>

int main(int argc, char *argv[]) {
  int i = 123;
  printf("Variable i has addr (%p) and value %d\n", &i, i);
  return 0;
}
```
</script>
</section>


<section data-markdown>
![pointer-0]({{ "/assets/images/csc-331/intro_c/pointer-0.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>

<section data-markdown>
### Pointer definition

- Pointer is a variable that points to a memory location.
- A pointer is denoted by a * character.
- The type of pointer must be the same as that of the value being stored in the memory location (that the pointer points to).
</section>


<section data-markdown>
<script type="text/template">

Inside your `intro-c` directory, make a copy of `pointer-1.c` and name it `pointer-2.c`.
Edit `pointer-2.c` and update it so that the codes look like the codes in the next slide.

```
$ cp pointer-1.c pointer-2.c
$ nano pointer-2.c
```
</script>
</section>


<section data-markdown>
![pointer-1]({{ "/assets/images/csc-331/intro_c/pointer-1.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
<script type="text/template">
Source code of `pointer-2.c`

```
#include <stdio.h>

int main(int argc, char *argv[]) {
  int i = 123;
  int *pointer_to_i = &i;
  printf("Variable i has addr (%p) and value %d\n", &i, i);
  printf("The pointer points to addr (%p) containing value %d\n", pointer_to_i, *pointer_to_i);
  return 0;
}
```
</script>
</section>


<section data-markdown>
![pointer-2]({{ "/assets/images/csc-331/intro_c/pointer-2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### <center> Pass by Value and Pass by References </center>

- Parameters are passed to functions.
- Parameters can be value variables or pointer variables.
- What is the difference?

</section>



<section data-markdown>
<script type="text/template">
Inside your `intro-c` directory, make a copy of `pointer-2.c` and name it `pointer-3.c`.
Edit `pointer-3.c` and update it so that the codes look like following:
```
#include <stdio.h>

int pass_by_value(int i) {
    i = i * 2;
    return i;
}

int main(int argc, char *argv[]) {
    int i = 123;
    printf("Value of i before function call: %d\n", i);
    printf("The function returns: %d\n", pass_by_value(i));
    printf("Value of i after function call: %d\n", i);
    return 0;
}

```
</script>
</section>


<section data-markdown>
![pointer-3]({{ "/assets/images/csc-331/intro_c/pointer-3.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
<script type="text/template">
Inside your `intro-c` directory, make a copy of `pointer-3.c` and name it `pointer-4.c`.
Edit `pointer-4.c` and update it so that the codes look like following:
```
#include <stdio.h>

int pass_by_ref(int *i) {
    *i = (*i) * 2;
    return *i;
}

int main(int argc, char *argv[]) {
    int i = 123;
    printf("Value of i before function call: %d\n", i);
    printf("The function returns: %d\n", pass_by_ref(&i));
    printf("Value of i after function call: %d\n", i);
    return 0;
}

```
</script>
</section>


<section data-markdown>
![pointer-4]({{ "/assets/images/csc-331/intro_c/pointer-4.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>

In Java, do you pass by value or pass by reference?

</section>
