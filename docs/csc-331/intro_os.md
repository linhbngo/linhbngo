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

![cpu]({{ "/assets/images/csc-331/intro_os/cpu.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

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

![multi-cpu]({{ "/assets/images/csc-331/intro_os/multi-cpu.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

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
### Grading Appeals

Mistakes occasionally happen during the grading process. If you think a mistake has been made regarding your grades, you should send me an email with detailed justification within one week of the date the grades are available. No changes on grades will be made after one week from the date the grades are posted.
</section>

<section data-markdown>
### Participation

- Participation accounts for 5% of your grade.
- This part of your grade will be determined by:
    - whether or not you show up to class and office hours, and
    - how actively you participate (ask questions, make comments, contribute to activities) during class.
- Participation grades will be assigned in a coarsely manner:
    - 100% to students who are fully engaged active participants,
    - 50% to students who are nominally engaged (physically there and willing to participate when asked to), and
    - 0% for students who really aren't engaged (trying to hide).
</section>

<section data-markdown>
### Office Hours

- Office hours are an opportunity to reinforce course topics either one-on-one or in small groups. If you are unable to attend during the posted time slots, I am happy to make an appointment.

</section>

<section data-markdown>
### Attendance Policy

- Attendance is critical to the success of students in this class.
- We will take note of who attends, including occasionally using attendance check in place of a quiz score.
- If you miss a class, you are responsible for obtaining lecture notes, handouts, and homework assignments from fellow students.
- If the instructor is late for class, please wait 20 minutes before leaving.
</section>

<section data-markdown>
### Excused Absences Policy for University-Sanctioned Event

- Students are advised to carefully read and comply with the excused absences policy for university-sanctioned events contained in the WCU Undergraduate Catalog.
- In particular, please note that the “responsibility for meeting academic requirements rests with the student,” that this policy does not excuse students from completing required academic work, and that professors can require a “fair alternative” to attendance on those days that students must be absent from class in order to participate in a University-Sanctioned Event.
</section>

<section data-markdown>
### Late Work
- Without prior approval from the instructors, late homework assignments will not be accepted but will be assigned a grade of zero.
- Unless accompanied with a valid medical or University excuse, all late submissions will be penalized.
- A make-up for the exams will be given only with a valid medical or University excuse.
</section>


<section data-markdown>
### Academic Integrity

It is the responsibility of each student to adhere to the university's standards for academic integrity. Violations of academic integrity include any act that violates the rights of another student in academic work, that involves misrepresentation of your own work, or that disrupts the instruction of the course.

</section>

<section data-markdown>
### Academic Integrity
Other violations include (but are not limited to):

- cheating on assignments or examinations;
- plagiarizing, which means copying any part of another's work and/or using ideas of another and presenting them as one's own without giving proper credit to the source;
- selling, purchasing, or exchanging of term papers;
- falsifying of information; and
- using your own work from one class to fulfill the assignment for another class without significant modification.

Proof of academic misconduct can result in the automatic failure and removal from this course.
</section>

<section data-markdown>
### Academic Integrity
For questions regarding Academic Integrity, Sexual Harassment, or the Student Code of Conduct, students are encouraged to refer to the “Other” Menu of the Computer Science web page www.cs.wcupa.edu/, the Undergraduate Catalog, the Ram’s Eye View, and the University website at www.wcupa.edu.
</section>


<section data-markdown>
### Disability Accommodations
- To know more about West Chester University’s Services for Students with Disabilities (OSSD), contact the OSSD which is located at 223 Lawrence Center. The OSSD hours of Operation are Monday  Friday 8:30 a.m.  4:30 p.m. Their phone number is 610-436-2564, their fax number is 610-436-2600, their email address is ossd@wcupa.edu, and their website is at www.wcupa.edu/ussss/ossd.
- If you have a disability that requires accommodations under the Americans with Disabilities Act (ADA), please present your letter of accommodations to OSSD as soon as possible so that OSSD can support your success in an informed manner. Accommodations cannot be granted retroactively.
</section>

<section data-markdown>
### Title IX Statement

- West Chester University and its faculty are committed to assuring a safe and productive educational environment for all students. In order to meet this commitment and to comply with Title IX of the Education Amendments of 1972 and guidance from the Office for Civil Rights, the University requires faculty members to report incidents of sexual violence shared by students to the University's Title IX Coordinator, Ms. Lynn Klingensmith.
- The only exceptions to the faculty member's reporting obligation are when incidents of sexual violence are communicated by a student during a classroom discussion, in a writing assignment for a class, or as part of a University-approved research project. Faculty members are obligated to report sexual violence or any other abuse of a student who was, or is, a child (a person under 18 years of age) when the abuse allegedly occurred to the person designated in the University protection of minors policy. Information regarding the reporting of sexual violence and the resources that are available to victims of sexual violence is set forth at the webpage for the Office of Social Equity at http://www.wcupa.edu/_admin/social.equity/.
</section>

<section data-markdown>
### Title IX Statement

- Ms. Lynn Klingensmith is the West Chester University Title IX Coordinator and is also the Director of Social Equity. She can be reached at 610-436-2433 or by email at LKlingensmith@wcupa.edu and can connect you to resources both on and on campus, as well as provide information about the processes related to cases of sexual misconduct.

- West Chester University community members also have a right to report acts of sexual misconduct to the Office of Civil Rights. They can be contacted at: The Wanamaker Building, 100 Penn Square East, Suite 515, Philadelphia, PA 19107-3323, (215) 656-8541, OCR.Philadelphia@ed.gov
</section>

<section data-markdown>
### Emergency Preparedness
- All students are encouraged to sign up for the University’s free WCU ALERT service, which delivers official WCU emergency text messages directly to your cell phone.
- For more information, visit www.wcupa.edu/wcualert. To report an emergency, call the Department of Public Safety at 610-436-3311.
</section>

<section data-markdown>
### Electronic Mail Policy

- It is expected that faculty, staff, and students activate and maintain regular access to University provided e-mail accounts.
- Official university communications, including those from your instructor, will be sent through your university e-mail account.
- You are responsible for accessing that mail to be sure to obtain official University communications.
Failure to access will not exempt individuals from the responsibilities associated with this course.
</section>

<section data-markdown>
### Instructor Email Policy

- For individual issue, it is best to contact me via email. I check my email frequently during normal working hours (9-5) on weekdays, and I will try to respond quickly (hopefully the same day). I do also check email on weekends and evenings, but not nearly as frequently (almost never on Sundays). As a result, you should expect longer delays during these times.

- If you send me an assignment-related email right before a deadline, I may not answer it in time to be helpful.
</section>
