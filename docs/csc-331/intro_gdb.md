---
layout: slide
title: Introduction to GNU Debugger
category: presentation
---

<section data-markdown>
## <center> GNU Debugger </center>
</section>


<section data-markdown>
### In a Nutshell

- Developed in 1986 by Richard Stallman at MIT
- Richard Stallman:
  - Father of emacs
  - Father of the GNU Project (GNU's Not Unix) and the original author behind the first GNU General Public License for open source software
</section>

<section data-markdown>
### Brief technical details

- Allows programmers to see inside and interact/modify with all components of a programs, including information inside the registers. 
- Allows programmers to walk through the program step by step, including down to instruction level, to debug the program. 
</section>


<section data-markdown>
### Cheat Sheet

[GDB Cheat Sheet by Dr. Doeppner at Brown University](https://cs.brown.edu/courses/cs033/docs/guides/gdb.pdf)

</section>


<section data-markdown>
### We are using an enhanced interface of gdb, called [gdb-peda](https://github.com/longld/peda)

```
$ sudo apt-get install -y libncurses5-dev
$ git clone https://github.com/longld/peda.git
$ echo "source ~/peda/peda.py" >> ~/.gbdinit
```

When you run `gdb`, you will see a red `gdb-peda` prompt. 
</section>

<section data-markdown>
### Tmux (terminal multiplexer) Quickstart

- Start new: `tmux`
- Start new with a session name: `tmux new -s myname`
- List sessions: `tmux ls`
- Kill session: `tmux kill-session -t myname`

- Splits terminal into vertical panels: `Ctrl-B then %`  
- Splits terminal into horizontal panels: `Ctrl-B then "`
- Toggle between panels: `Ctrl-B then Space`
- Move from one panel to other directionally: `Ctrl-B then corresponding arrow key`
</section>


<section data-markdown>
### Tmux (terminal multiplexer) Quickstart

- Open tmux command by typing `Ctrl-B then :`
- Use the following commands for resizing:
  - resize-pane -D 20 (Resizes the current pane down by 20 cells)
  - resize-pane -U 20 (Resizes the current pane upward by 20 cells)
  - resize-pane -L 20 (Resizes the current pane left by 20 cells)
  - resize-pane -R 20 (Resizes the current pane right by 20 cells)
</section>


<section data-markdown>
### Exercise

Use tmux, create a layout that looks like the figure below:
![tmux]({{ "/assets/images/csc-331/intro_gdb/tmux.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Setup an application with gdb

- To use gdb, typically we compile the program with `-g` flag. 
- In the left tmux pane, cd into `Operating-Systems/intro-c` and compile hello.c with `-g` flag:

```
$ gcc -g hello.c
``` 
</section>


<section data-markdown>
### Run gdb
- In the right tmux pane:

```
$ cd Operating-Systems/intro-c
$ gdb a.out
gdb-peda$ run
```

The program runs, and that's that. 
</section>


<section data-markdown>
![gdb1]({{ "/assets/images/csc-331/intro_gdb/gdb1.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>

We need to set a breakpoint (a line number or a function name)

```
gdb-peda$ b main
gdb-peda$ run
```
</section>

<section data-markdown>
![gdb2]({{ "/assets/images/csc-331/intro_gdb/gdb2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
![gdb2]({{ "/assets/images/csc-331/intro_gdb/gdb2.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>

Oops, it scrolled away ... 

- To enable scrolling mode in tmux, type `Ctrl-B [` and then use the Up and Down arrow to scroll 
- To quit, type `q`

</section>


<section data-markdown>
![gdb4]({{ "/assets/images/csc-331/intro_gdb/gdb4.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### At a glance

- Registers' contents
- Code
- Stack contents
- ...

gdb is stopping at our break point, set at function *main*. 
</section>


<section data-markdown>
### Exercise

- Run `n` to step through the executing program. Examine the register contents along the way. 

- Run `quit` to quit gdb when you are done. 
</section>





<section data-markdown>
### Identify local variables' information:

- Compile `pointer-1.c` with `-g` flag. 
- Step through the function and use the following commands to examine the variable's contents:

```
gdb-peda$ p i
gdb-peda$ p &i
gdb-peda$ x/dh &i
```
</section>


<section data-markdown>
### Array and gdb

- Compile `array.c` with `-g` flag. 
- Step through the function until you get to the `for` statement.
- Examine the address and contents of the array

```
gdb-peda$ i locals
gdb-peda$ p &numbers
gdb-peda$ p &numbers+1
gdb-peda$ p &numbers+2
gdb-peda$ p &numbers+3
gdb-peda$ p &numbers+4
```
</section>


<section data-markdown>
![gdb5]({{ "/assets/images/csc-331/intro_gdb/gdb5.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### After a few iterations of the loop

- Examine the contents of local variables using `i locals`
- Examine the contents and addresses of `numbers` using `p`
- Examine the contents at addresses of `numbers` using `x/dh`
</section>