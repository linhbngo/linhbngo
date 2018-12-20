---
layout: slide
title: Introduction to OS
category: presentation
---

<section data-markdown>
## <center> Introduction to Operating Systems </center>
</section>

<section data-markdown>
### Linh B. Ngo, Ph.D.

- Email: LNGO at WCUPA dot EDU
- Office: 144 UNA (25 University Avenue)
- Office Hours:
    - MT 2:00PM to  4:00PM
    - W 11:00AM to 12:00PM
</section>

<section data-markdown>
### Course Descriptions

This course will introduce three fundamental concepts in operating system (OS):
Virtualization, Concurrency, and Persistence.

- *Virtualization*: How OS creates abstractions through which programmers can
interact with the underlying hardware
(e.g., *processes*, *memory spaces*, and *CPU scheduling*).

- *Concurrency*: How OS supports sharing of physical resources
among these abstractions (e.g., *thread*, *lock*, and *semaphores*).

- *Persistence*: How OS enables the long term management of information,
produced or required by computer programs, in a manner that persists beyond the scope or the duration
of these programs (e.g., *I/O devices* and *file systems*).

Understanding how operating systems work will facilitate better understanding about how programs are
run by the computer hardware. This will lead to more efficient, stable, and secure programs.
</section>

<section data-markdown>
### Learning Objectives

- Students will be able to apply mathematical foundations, algorithmic principles, and computer science theory.
- Students will be able to to design, implement and evaluate a computer-based system, process, component, or program to meet desired needs.
</section>

<section data-markdown>
### Important Dates
- Tue, Jan 29, 2019: Last Day of Add/Drop
- Mon, Mar 11-17, 2019: Spring Break
- Tue, Mar 26, 2019: Last Day of Course Withdrawal
- Tue, Nov 20, 2019: Reading/Writing Day
- Tue, May 07, 2019: 10:30AM to 12:30PM FINAL EXAM
</section>

<section data-markdown>
### Prerequisites

- CSC 220 - Foundations of Computer Science
- CSC 240 - Computer Science III
- CSC 241 - Data Structures & Algorithms
- CSC 242 - Computer Organization
- Being able to program in **C**. We will cover some background information regarding C programming, but it is important that you take it upon yourself to learn the language.
</section>

<section data-markdown>
### Textbook

- **Operating Systems: Three Easy Pieces** by Remzi H. Arpaci-Dusseau and Andrea C. Arpaci-Dusseau.
- [Free online PDF chapters by the authors](http://pages.cs.wisc.edu/~remzi/OSTEP/)
- If you like it, buy it to support the efforts to produce inexpensive, quality, and free textbooks.
- Reference book (optional): [Operating Systems Design and Implementation](https://www.amazon.com/Operating-Systems-Design-Implementation-3rd/dp/0131429388)
</section>

<section data-markdown>
### Laptop requirements
Having access to a laptop during class time is critical
- Engaging in in-class examples that demonstrate the lectured concepts.
- Working on in-class electronic quizzes on D2L
- Make sure that your laptop is fully charged for the duration of the class (or come in early and get a spot with access to power outlets)
</section>

<section data-markdown>
### Software requirements
As laptop style and model can vary, the following common (and free) software environment will be enforced for all lectures and programming assignments:

- Virtual Enronment: Oracle VirtualBox
- Virtual OS for VirtualBox: Minix
- Other software packages will be specified and installed inside the virtual OS as needed.
</section>

<section data-markdown>
### Course Materials
- Lecture slides and example codes will be available online via links inside the course’ D2L page
- Links to papers on subjects we will be discussing in class will also be listed and/or embedded in the slides.
- West Chester University maintains extensive licensed products to academic publishers such as ACM, IEEE, Elsevier, and Springer, and many of the papers required for this course will be available through the library's online database.
- Google Scholar is another excellent source for downloading preprint or open-source versions of papers.
</section>

<section data-markdown>
### Grading

- Assignments: 50%
- Exam:
    - Exam 1: 15%
    - Exam 2: 10% (Comprehensive)
- Quiz: 20%
- Participation: 5%
</section>

<section data-markdown>
### Letter grades

| Number | 100-93 | 92-90 | 89-87 | 86-83 | 82-80 | 79-77 | 76-73 | 72-70 | 69-67 | 66-63 | 62-60 | <= 59 |
| ------ | ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Letter | A	  | A-    | B+    | B     | B-    | C+    | C     | C-    | D+    | D     | D-    | F     |

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



<section data-markdown>
### Git

- The class materials, including source codes, will be disseminated via Git. Being able to use Git is a critical skill for most, if not all software developers and/or IT professionals. There are many tutorials already available online for Git. Some of the more helpful ones include github's, "the simple guide", and atlassian's);

- It would be a mistke if you just attempt to access the cloass materials via the web browser. "This is a mistake. Just learn Git. The command line interface is faster and more powerful, and you're going to need to learn it at some point in your life. Why not today?" - Dr. Jacob Sorber, Clemson University.
</section>
