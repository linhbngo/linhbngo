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
<script type="text/template">

### What are we returning with void?

- void*: pointer to unknown type (JBOB - just a bunch of bytes)
```
#include <stdlib.h>
...
void *p = malloc(100);
...
```
</script>
</section>


<section data-markdown>
### Hands-on
- Start virtualbox
- Start the *csc-331* VM
</section>


<section data-markdown>
### Setup directory

- If you shutdown your VM properly, you should still have the `intro-c` directory.
- Confirm that you are in your `home` directory by typing `pwd` and confirm that you are in `/home/student`.
- Confirm that you still have `intro-c` using `ls`.
- Change into `intro-c`. 
- If you don't have `intro-c`, create one (take a look at Tuesday's lecture for instruction.) 

```
$ ls
$ cd intro-c
```
</section>


<section data-markdown>
<script type="text/template">
Typecast

Create and save the following code as malloc.c

```
#include <stdlib.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
  void *p = malloc(100);
  int *ip = (int *)p;
  *ip = 98765;
  printf("%d\n", *ip);
  return 0;
}
```
</script>
</section>


<section data-markdown>
### What points to where!!!

- `void *p = malloc(100);`
  - Allocate and assign the address of 100 bytes of unknown type to pointer variable `p`.
- `int *ip = (int *)p;`
  - Assign the address of the 100 bytes above to pointer variable `ip`, and cast `ip` to type int.
  - Now you can use `*ip` to manipulate these 100 bytes. 
</section>


<section data-markdown>
### Compile and Run: Simple Compilation

- Make sure that you are still inside `/home/student/intro-c` using `pwd`.

```
$ pwd
$ gcc malloc.c
$ ./a.out
```
</section>


<section data-markdown>
![malloc]({{ "/assets/images/csc-331/malloc_struct_function/malloc.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### So wasteful!!!

- An `int` is only 4 to 8 bytes. 
- How do we know how much to ask for? 
</section>


<section data-markdown>
<script type="text/template">
Create a copy of `malloc.c` and name it `malloc-2.c`. Edit `malloc-2.c` as follows:

```
#include <stdlib.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
  int *ip = (int *)malloc(sizeof(int));
  *ip = 98765;
  printf("%d\n", *ip);
  return 0;
}
```
</script>
</section>


<section data-markdown>
![malloc-2]({{ "/assets/images/csc-331/malloc_struct_function/malloc-2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
<script type="text/template">
Free up memory after you are done with the pointer. To be extra careful, also set the pointer to NULL. 

```
#include <stdlib.h>
#include <stdio.h>
int main(int argc, char *argv[]) {
  int *ip = (int *)malloc(sizeof(int));
  *ip = 98765;
  printf("%d\n", *ip);
  free(ip);
  ip=NULL;
  return 0;
}
```
</script>
</section>


<section data-markdown>
## <center> Dynamic Array </center>
</section>


<section data-markdown>
### Array size determination

- In Java, you can allocate storage for an array at any time in the program, not just when a variable is first initialized. 
- In C, you need to specify the array size upfront when using the standard [] notation (*rare exception* with C99 standards).
- What to do?
</section>


<section data-markdown>
### What is an array in C?

- In Java, you can allocate storage for an array at any time in the program, not just when a variable is first initialized. 
- In C, you need to specify the array size upfront when using the standard [] notation (*rare exception* with C99 standards).
- What to do?
</section>


<section data-markdown>
<script type="text/template">
What does an array in C look like?

Create and save the following code as array.c

```
#include <stdio.h>
int main(int argc, char *argv[]) {
  int numbers[5];
  int i;
  for (i = 0; i < 5; i++){
    numbers[i] = i * 2;
    printf("Index %d has value %d at address (%p)\n", i, numbers[i], (numbers + i))
  }
  return 0;
}
```
</script>
</section>


<section data-markdown>
![array]({{ "/assets/images/csc-331/malloc_struct_function/array.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Exercise

- Create a copy of `array.c` called `array-2.c`
- Change type of `numbers` to `double`. 
- What is the address step now?
</section>


<section data-markdown>
![array-2]({{ "/assets/images/csc-331/malloc_struct_function/array-2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### An array variable ...

- ... is in fact pointing to an address containing a value. 
- ... without the bracket notation and with an index points to the corresponding address of the value at the index. 
</section>


<section data-markdown>
### An array variable ...

- ... is quite similar to a pointer.
</section>


<section data-markdown>
<script type="text/template">

Make a copy of `array.c` and call it  `array-3.c`. Compile and run.

```
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
  int i, size;
  int *p; 

  size = 5;
  for (i = 0; i < size; i++){
    printf("Before init, index %d has value %d at addr (%p)\n", i, p[i], p + i);
    p[i] = i * 2;
    printf("After init, index %d has value %d at addr (%p)\n", i, p[i], p + i);
  }
  return 0;
}
```
</script>
</section>


<section data-markdown>
![array-3]({{ "/assets/images/csc-331/malloc_struct_function/array-3.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Array of Strings

- String is an array of characters. 
- What then is an array of strings?
</section>


<section data-markdown>
<script type="text/template">
```
char **s_array = (char **)calloc(array_len, sizeof(char*));
for (int i = 0; i < array_len; i++) {
  s_array[i] = (char *)calloc(this_str_len, sizeof(char));
}
```
</script>
</section>


<section data-markdown>
### Draw It!!!
</section>


<section data-markdown>
<script type="text/template">

Complete the following codes and save it to a file called `array-4.c`. The goal is to echo the two strings **Golden** and **Ram** to screen using an array of strings. 

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[]){ 
  int i, word_count;
  int str_len[2] = {6, ____};
  char **s_array;

  word_count = ___;
  s_array = (char**)calloc(word_count, sizeof(char *));
  for (i = 0; i < word_count; i++){
    s_array[i] = (char *)calloc(_____, sizeof(char));
  }
  strcpy(s_array[0], "Golden");
  strcpy(s_array[1], "Ram");
  printf("%s %s\n", s_array[0], s_array[1]);
  return 0;
}
```
</script>
</section>


<section data-markdown>
![array-4]({{ "/assets/images/csc-331/malloc_struct_function/array-4.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
![array-4-sol]({{ "/assets/images/csc-331/malloc_struct_function/array-4-solution.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
## <center> Structured Types </center>
</section>


<section data-markdown>
### Object in C

- C has no classes or objects
</section>


<section data-markdown>
### Object in C

- C has **struct** type (think ancestor of object)
</section>


<section data-markdown>
<script type="text/template">
Create a file named `struct.c`. Compile and run. 

```
#include <stdio.h>

struct point {
  int x; 
  int y;
};

int main(int argc, char *argv[]) {
  struct point origin;
  origin.x = 0;
  origin.y = 0;
  printf ("The coordinates of origin is %d and %d", origin.x, origin.y);
  return 0;
}
```
</script>
</section>


<section data-markdown>
![struct]({{ "/assets/images/csc-331/malloc_struct_function/struct.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Composite struct

Just like Java

```
struct line {
  struct point start;
  struct point end;
};

....

struct line line1;
line1.start.x = 1;
line1.start.y = 2;
line1.end.x = 3;
line1.end.y = 4;
```
</section>


<section data-markdown>
## <center> Functions </center>
</section>


<section data-markdown>
### Almost the same as methods in Java, except for one tiny difference ...
</section>


<section data-markdown>
<script type="text/template">
Create a file named `function.c` with the following content. Compile and run. 
```
#include <stdio.h>

int times2(int x) {
  return x * 2;
}

int times4(int x) {
  return times2(x) * 2;
}

int main(int argc, char *argv[]) {
    int x = 100;
    printf("Result: %d\n", times4(x);
    return 0;
}

```
</script>
</section>


<section data-markdown>
<script type="text/template">
Create a file named `function-2.c` with the following content. Compile and run. 
```
#include <stdio.h>

int times4(int x) {
  return times2(x) * 2;
}

int times2(int x) {
  return x * 2;
}

int main(int argc, char *argv[]) {
    int x = 100;
    printf("Result: %d\n", times4(x);
    return 0;
}

```
</script>
</section>


<section data-markdown>
![function]({{ "/assets/images/csc-331/malloc_struct_function/function.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
<script type="text/template">
### Function Declaration

Create a file named `function-3.c` with the following content. Compile and run. 
```
#include <stdio.h>
int times2(int x);
int times4(int x);

int times4(int x) {
  return times2(x) * 2;
}

int times2(int x) {
  return x * 2;
}

int main(int argc, char *argv[]) {
    int x = 100;
    printf("Result: %d\n", times4(x);
    return 0;
}

```
</script>
</section>


<section data-markdown>
![function-3]({{ "/assets/images/csc-331/malloc_struct_function/function-3.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
## <center> Everything is a pointer!!! </center>
</section>


<section data-markdown>
<script type="text/template">
Create a file named `struct-2.c`. Compile and run. 

```
#include <stdio.h>
#include <stdlib.h>
struct point {
  int x; 
  int y;
};

int main(int argc, char *argv[]) {
  struct point* p = (struct point *)malloc(sizeof(struct point));
  (*p).x = 0;
  (*p).y = 0;
  printf ("The coordinates of origin is %d and %d", (*p).x, (*p).y);
  return 0;
}
```
</script>
</section>


<section data-markdown>
<script type="text/template">
Create a file named `struct-3.c`. Compile and run. 

```
#include <stdio.h>
#include <stdlib.h>
struct point {
  int x; 
  int y;
};

int main(int argc, char *argv[]) {
  struct point* p = (struct point *)malloc(sizeof(struct point));
  p->x = 0;
  p->y = 0;
  printf ("The coordinates of origin is %d and %d", p->x, p->y);
  return 0;
}
```
</script>
</section>


<section data-markdown>
<script type="text/template">
### Function Declaration

Create a file named `function-4.c` with the following content. Compile and run. 
```
#include <stdio.h>
int times2(int x);
int times5(int x);
void array_apply(int a[], int alen, int (*fp)(int));

int times5(int x) {
  return x * 5;
}

int times2(int x) {
  return x * 2;
}

void array_apply(int a[], int alen, int (*fp)(int)) {
  int i;
  for (i = 0; i <alen; i++) {
    a[i] = (*fp)(a[i]);
    printf("New value at index %d is %d\n", i, a[i]);
  }
}

int main(int argc, char *argv[]) {
    int numbers[] = {1, 2, 3};
    array_apply(numbers, 3, times2);
    array_apply(numbers, 3, times5);
    return 0;
}

```
</script>
</section>


<section data-markdown>
## <center> How do you replicate the fundamental behavior of object and methods in Java with struct, function, and pointer in C? </center>
</section>


<section data-markdown>
## <center> Assignment !!! </center>
</section>