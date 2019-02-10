---
layout: single
title: Operating Systems
permalink: /docs/csc-331/
sidebar:
  nav: "docs"
toc: true
---

### Course Description

This course will introduce three fundamental concepts in operating system (OS):
Virtualization, Concurrency, and Persistence.

- In *Virtualization*, we learn how OS creates abstractions through which programmers can
interact with the underlying hardware. Examples of these abstractions include *processes*,
*memory spaces*, and *CPU scheduling*.

- In *Concurrency*, we learn about how OS supports sharing of physical resources
among these abstractions. These include *thread*, *lock*, and *semaphores*.

- In *Persistence*, we learn about how OS enables the long term management of information,
produced or required by computer programs, in a manner that persists beyond the scope or the duration
of these programs.

Understanding how operating systems work will facilitate better understanding about how programs are
run by the computer hardware. This will lead to more efficient, stable, and secure programs.

**Learning Objectives**

- Students will be able to apply mathematical foundations, algorithmic principles, and computer science theory.

- Students will be able to to design, implement and evaluate a computer-based system, process, component, or program to meet desired needs.


### Important Dates

- Tue, Jan 29, 2019: Last Day of Add/Drop
- Mon, Mar 11-17, 2019: Spring Break
- Tue, Mar 26, 2019: Last Day of Course Withdrawal
- Tue, May 07, 2019: 10:30AM to 12:30PM FINAL EXAM

### Course Requirements

**Prerequisites**

- Foundations of Computer Science (CSC 220)
- Computer Science III (CSC 240)
- Fundamental understanding of computer architecture and hardware design (CSC 242)
- Knowledge of core data structures and algorithms (CSC 241)

**Textbook**

- **Operating Systems: Three Easy Pieces** by Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau.
- [Free online PDF chapters by the authors](http://pages.cs.wisc.edu/~remzi/OSTEP/)
- If you like it, buy it to support the efforts to produce inexpensive, quality, and free textbooks.
- Reference book (optional): [Operating Systems Design and Implementation](https://www.amazon.com/Operating-Systems-Design-Implementation-3rd/dp/0131429388)

**Software requirements**

As laptop style and model can vary, the following common (and free) software environment will be enforced for all lectures and programming assignments:

- Virtual Environment: Oracle VirtualBox
- Other software packages will be specified and installed inside the CentOS virtual machine as needed.


### Course Materials

- Lecture slides and example codes will be available online via links inside the course' D2L page

- Links to papers on subjects we will be discussing in class will also be listed and/or embedded in the slides.

- West Chester University maintains extensive licensed products to academic publishers such as ACM, IEEE, Elsevier, and Springer, and many of the papers required for this course will be available through the library's online database.
- Google Scholar is another excellent source for downloading preprint or open-source versions of papers.


### Git

- The class materials, including source codes, will be disseminated via Git. Being able to use Git is a critical skill for most, if not all software developers and/or IT professionals. There are many tutorials already available online for Git. Some of the more helpful ones include Github's, "the simple guide", and Atlassian's);

- It would be a mistake if you just attempt to access the class materials via the web browser. "This is a mistake. Just learn Git. The command line interface is faster and more powerful, and you're going to need to learn it at some point in your life. Why not today?" - Dr. Jacob Sorber, Clemson University.


### Tentative Course Outline


- [Syllabus]({{ "/docs/csc-331/syllabus_slide/" | relative_url }}) (**Week 1**)
- [Introduction to Linux]({{ "docs/csc-331/linux_slide/" | relative_url }})
- [Introduction to Operating Systems]({{ "/docs/csc-331/intro_os/" | relative_url }})
- [Introduction to C Programming]({{ "/docs/csc-331/intro_c/" | relative_url }}) (**Week 2**)
- [Malloc, Struct, Function]({{ "/docs/csc-331/malloc_struct_function/" | relative_url }}) 
- Virtualization
  - Processes (**Week 3**)
    - [Abstraction: Process]({{ "/docs/csc-331/abstraction_process/" | relative_url }})
    - [Process API]({{ "/docs/csc-331/process_api/" | relative_url }})
    - [Limited Direct Execution]({{ "/docs/csc-331/limited_direct_execution/" | relative_url }})
  - CPU Scheduling (**Week 4**)
  - Memory Management (**Week 5**)
  - Paging (**Week 6**)
- Concurrency
  - Threads (**Week 7**)
  - Locks,
  - Condition Variables (**Week 8**)
  - Semaphores (**Week 9**)
  - Deadlock (**Week 10**)
- Persistence
  - I/O and Disks, Disk Scheduling (**Week 11**)
  - RAID, File Systems (**Week 12**)
  - File System Implementation (**Week 13**)
  - Journaling (**Week 14**)
  - LFS, SSD (**Week 15**)


### Grading

Grades will be based on the following distribution:

- Assignments: 50%
- Exam:
  - Exam 1: 15%
  - Exam 2: 10% (Comprehensive)
- Quiz: 20%
- Participation: 5%

Letter grades are assigned according to the following scale:

| Number | 100-93 | 92-90 | 89-87 | 86-83 | 82-80 | 79-77 | 76-73 | 72-70 | 69-67 | 66-63 | 62-60 | <= 59 |
| Letter | A	| A- | B+ | B | B- | C+ | C | C- | D+ | D | D- | F |


**Grading Appeals**

Mistakes occasionally happen during the grading process. If you think a mistake has been made regarding your grades, you should send me an email with detailed justification within one week of the date the grades are available. No changes on grades will be made after one week from the date the grades are posted.



### Class Policy

**Office Hours**

Office hours are an opportunity to reinforce course topics either one-on-one or in small groups. If you are unable to attend during the posted time slots, I am happy to make an appointment.


**Attendance**

- Attendance is critical to the success of students in.
- We will take note of who attends, including occasionally using attendance check in place of a quiz score.
- If you miss a class, you are responsible for obtaining lecture notes, handouts, and homework assignments from fellow students.
- If the instructor is late for class, please wait 20 minutes before leaving.


**Excused Absences Policy for University-Sanctioned Event**

- Students are advised to carefully read and comply with the excused absences policy for university-sanctioned events contained in the WCU Undergraduate Catalog.
- In particular, please note that the “responsibility for meeting academic requirements rests with the student,” that this policy does not excuse students from completing required academic work, and that professors can require a “fair alternative” to attendance on those days that students must be absent from class in order to participate in a University-Sanctioned Event.


**Late Work**

- Without prior approval from the instructors, late homework assignments will not be accepted but will be assigned a grade of zero.

- Unless accompanied with a valid medical or University excuse, all late submissions will be penalized.
A make-up for the exams will be given only with a valid medical or University excuse.

**Electronic Mail Policy**

- It is expected that faculty, staff, and students activate and maintain regular access to University provided e-mail accounts.

- Official university communications, including those from your instructor, will be sent through your university e-mail account.

- You are responsible for accessing that mail to be sure to obtain official University communications.
Failure to access will not exempt individuals from the responsibilities associated with this course.
Instructor Email Policy

- For individual issue, it is best to contact me via email. I check my email frequently during normal working hours (9-5) on weekdays, and I will try to respond quickly (hopefully the same day). I do also check email on weekends and evenings, but not nearly as frequently (almost never on Sundays). As a result, you should expect longer delays during these times.

- If you send me an assignment-related email right before a deadline, I may not answer it in time to be helpful.


### Academic Integrity

It is the responsibility of each student to adhere to the university’s standards for academic integrity. Violations of academic integrity include any act that violates the rights of another student in academic work, that involves misrepresentation of your own work, or that disrupts the instruction of the course. Other violations include (but are not limited to): cheating on assignments or examinations; plagiarizing, which means copying any part of another’s work and/or using ideas of another and presenting them as one’s own without giving proper credit to the source; selling, purchasing, or exchanging of term papers; falsifying of information; and using your own work from one class to fulfill the assignment for another class without significant modification. Proof of academic misconduct can result in the automatic failure and removal from this course.

For questions regarding Academic Integrity, Sexual Harassment, or the Student Code of Conduct, students are encouraged to refer to the "Other" Menu of the Computer Science web page www.cs.wcupa.edu/, the Undergraduate Catalog, the Ram's Eye View, and the University website at www.wcupa.edu.

### Disability Accommodations
To know more about West Chester University's Services for Students with Disabilities (OSSD), contact the OSSD which is located at 223 Lawrence Center. The OSSD hours of Operation are Monday  Friday 8:30 a.m.  4:30 p.m. Their phone number is 610-436-2564, their fax number is 610-436-2600, their email address is ossd@wcupa.edu, and their website is at www.wcupa.edu/ussss/ossd.
If you have a disability that requires accommodations under the Americans with Disabilities Act (ADA), please present your letter of accommodations to OSSD as soon as possible so that OSSD can support your success in an informed manner. Accommodations cannot be granted retroactively.


### Title IX Statement

- West Chester University and its faculty are committed to assuring a safe and productive educational environment for all students. In order to meet this commitment and to comply with Title IX of the Education Amendments of 1972 and guidance from the Office for Civil Rights, the University requires faculty members to report incidents of sexual violence shared by students to the University's Title IX Coordinator, Ms. Lynn Klingensmith.

- The only exceptions to the faculty member's reporting obligation are when incidents of sexual violence are communicated by a student during a classroom discussion, in a writing assignment for a class, or as part of a University-approved research project. Faculty members are obligated to report sexual violence or any other abuse of a student who was, or is, a child (a person under 18 years of age) when the abuse allegedly occurred to the person designated in the University protection of minors policy. Information regarding the reporting of sexual violence and the resources that are available to victims of sexual violence is set forth at the web page for the Office of Social Equity at http://www.wcupa.edu/_admin/social.equity/.

- Ms. Lynn Klingensmith is the West Chester University Title IX Coordinator and is also the Director of Social Equity. She can be reached at 610-436-2433 or by email at LKlingensmith@wcupa.edu and can connect you to resources both on and on campus, as well as provide information about the processes related to cases of sexual misconduct.

- West Chester University community members also have a right to report acts of sexual misconduct to the Office of Civil Rights. They can be contacted at: The Wanamaker Building, 100 Penn Square East, Suite 515, Philadelphia, PA 19107-3323, (215) 656-8541, OCR.Philadelphia@ed.gov


### Emergency Preparedness

- All students are encouraged to sign up for the University’s free WCU ALERT service, which delivers official WCU emergency text messages directly to your cell phone.

- For more information, visit www.wcupa.edu/wcualert. To report an emergency, call the Department of Public Safety at 610-436-3311.
