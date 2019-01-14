---
layout: slide
title: Linux Environment
category: presentation
---

<section data-markdown>
## <center> Introduction to Linux </center>
</section>

<section data-markdown>
### A Brief History

- It is really brief! (see https://www.levenez.com/unix/ for full details)
- 1969: Uniplexed Information and Computing System (Ken Thompson - Assembler)
- 1973: 5th Edition of UNIX (Ken Thompson and Dennis Ritchie - C)
- 1975: UNIX splits into two branches, SYSV (System 5) and BSD (Berkeley Software Distribution)
  - SYSV comes from AT&T and other commercial companies (Solaris, AIX, IRIX, HP-UX, Diginal UNIX ...)
  - BSD comes from Ken Thompson's sabbatical year at UC Berkeley (SunOS 4.x, ULTRIC, NextStep, FreeBSD, NetBSD, OpenBSD ...)
- 1987: Minix (Andrew S. Tanenbaum for teaching operating systems), which inspires ...
- 1991: Linux (Linus Torvald)
</section>

<section data-markdown>
### The Linux Filesystem

- Everything in Linux is a file. 
- The Linux filesystem is used to store all information relevant to the long-term state of the system, including
  - the operating system kernel,
  - the executable files for commands supported by the OS, 
  - configuration information, 
  - temporary work files, 
  - user data, 
  - special files that give controlled access to system hardware and OS functions.
</section>

<section data-markdown>
### The Linux Filesystem

- Start up and login to your VM
- At the terminal, type the following commands (hit Enter after each command)
- *The $ sign represents the prompt at the terminal. you do not retype $*

```{bash}
$ cd /
$ clear
$ ls -l -d */
```

</section>

<section data-markdown>
### The Linux Filesystem (Ubuntu)

- /: The *root* directory
- /dev: Hardware devices
- /bin: Essential low-level system utilities
- /usr: 
  - /usr/bin: Higher-level system utilities and application programs
  - /usr/lib: Program libraries for high-level user programs
- /lib: Program libraries for low-level system utilities
- /sbin: Superuser system utilities (for system administrative tasks)
- /tmp: Temporary file storage space (can be used by any user)
- /home: User home directories containing personal directory for each user
- /etc: Configuration and information files (for both system and user programs )
- /proc: A pseudo-filesystem to be used as an interface to the Linux kernel. It includes a sub-directory for each running process (run `ls /proc` and then `ps aux` to see the process ID matches up with the subdirectories)
</section>

<section data-markdown>
### The Linux File System (Ubuntu)

- /root: The *personal directory space* of the **root** user
- /snap: The directory for Ubuntu's package management utility
- /lost+found: abandoned files recovered by *fsck* but could not be placed into an exact location will be placed into this directory. 
- /lib64: Program libraries (similar to /lib) for 64-bit only programs.
- /media: Contains mount points for removable media
- /srv: Data for services provided by the system
- /opt: Add-on application software packages (usually via manual configuration/installation)
- /sys: Virtual directory for system information
- /run: Run-time variable data
- /boot: Static files of the boot loader
- /mnt: Mount point for mounting a file system temporarily
- /var: Variable data

</section>

<section data-markdown>
### Where are you in a Linux Filesystem?

- `pwd`: print working directory

```{bash}
$ pwd
```

- When login as a normal user, you always start at */home/user_name*
- As you move around the Linux Filesystem, `pwd` lets you know the path from */* to where you currently are.

</section>

<section data-markdown>
### The Linux File System (Ubuntu)

- **Path**: In a file system, a path allows a user/program to access a final location (file or directory) within that file system by following the hierarchical structure of directories leading to that location. 
- **Relative Path**: A path starting from your current location. 
- **Absolute Path**: A path starting from the root directory (`/`)
</section>

<section data-markdown>
### Where are the other stuff in a Linux Filesystem?

- `ls`: list directory

```{bash}
$ ls
```

- `ls` alone prints out the content of the current directory
- `ls` with a path to a directory prints out the content of that directory
- Additional flags (`-l`, `-a`, ...) can be used with `ls` to provide more information
- You can run `man ls` for more information about the command. 

</section>

<section data-markdown>
### How do you get from here to there?

- `cd`: change directory

```{bash}
$ pwd
$ cd /tmp
$ pwd
$ cd
$ pwd
```

- `cd` without target will change to home directory
- `cd` with `..` will move up one directory level

</section>

<section data-markdown>
### Other commands to manage the Linux Filesystem

- `mkdir`: make directory
- `rmdir`: remove directory
- `cp`: copy
- `mv`: rename or move files/directories
- `rm`: remove the specified files or directories

</section>


<section data-markdown>
### Viewing files (ASCII files)

- `cat`: catenate - displays the contents of the target file(s) on the screen. 
- `more` and `less`: `cat` with per-page views. 

</section>
