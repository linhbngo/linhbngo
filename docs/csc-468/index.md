---
layout: single
title: Applications of Parallel Computers
permalink: /docs/csc-468/
sidebar:
  nav: "docs"
toc: true
---

### Course Description

This course introduces both graduate and advanced undergraduate students from diverse departments to knowledge and techniques regarding efficient and productive usage of parallel computers. In other words, students learn how to write programs that run fast while minimizing programming effort. The latter is increasingly important since essentially all computers are (becoming) parallel, from supercomputers to laptops. So beyond teaching the basics about parallel computer architectures and programming languages, the course emphasizes commonly used patterns that appear in essentially all programs that need to run fast. The patterns include common computations (e.g. linear algebra, graph algorithms, structured grids ...) and ways to easily compose these into larger programs. We show how to recognize these patterns in a variety of practical problems, efficient (sometimes optimal) algorithms for implementing them, how to find existing efficient implementations of these patterns when available, and how to compose these patterns into larger applications. We do this in the context of the most important parallel programming models today: shared memory, distributed memory, GPUs, and cloud computing (eg MapReduce and Hadoop). We also present a variety of useful tools for debugging correctness and performance of parallel programs. Finally, we have a variety of guest lectures by a variety of experts, including parallel climate modeling, astrophysics, and other topics.

### Learning Objectives

- Students will be able to apply mathematical foundations, algorithmic principles, and computer science theory in the modeling and design of computer-based systems in a way that demonstrates comprehension of the tradeoffs involved in design choices.
- Students will be able to analyze a problem, and identify and define the computing requirements appropriate to its solution.
- Students will be able to apply design and development principles in the construction of large-scale computing systems.
- Students will be able to function effectively on teams to accomplish a common goal.

### Course Requirements

**Prerequisites**

The course is intended to be useful for students from many departments and with different backgrounds, and supplemental introductory materials will be provided to introduce students to programming languages and techniques used through the course. Eventually, the course will reach a level where it is assumed that students attain/have reasonable programming skills in a conventional (non-parallel) language, as well as enough mathematical skills to understand the problems and algorithmic solutions presented

**Textbook**

There is no textbook requirement for the course.

### Course Materials

- Lecture slides and example codes will be available online via links inside the course’ D2L page

- Links to papers on subjects we will be discussing in class will also be listed and/or embedded in the slides.

- West Chester University maintains extensive licensed products to academic publishers such as ACM, IEEE, Elsevier, and Springer, and many of the papers required for this course will be available through the library's online database.

- Google Scholar is another excellent source for downloading preprint or open-source versions of papers.


### Tentative Course Outline

- [Introduction]()
- [Single Processor Machines: Memory Hierarchies and Processor Features]()
- [Optimizing Matrix Multiply (cont), Introduction to Data Parallelism]()
- [Shared Memory Parallelism]()
- [Roofline and Performance Modeling]()
- [Sources of Parallelism and Locality (Part 1)]()
- [Sources of Parallelism and Locality (Part 2)]()
- [An Introduction to CUDA/OpenCL and Graphics Processors (GPUs)]()
- [Distributed Memory Machines and Programming]()
- [Advanced MPI and Collective Communication Algorithms]()
- [UPC++: Partitioned Global Address Space Languages]()
- [Cloud and big data]()
- [Parallel Matrix Multiply]()
- [Dense Linear Algebra]()
- [Sparse-Matrix-Vector-Multiplication and Iterative Solvers]()
- [Structured Grids]()
- [Machine Learning Part 1 (Supervised Learning)]()
- [Scaling Deep Neural Network Training]()
- [Machine Learning Part 2 (Unsupervised Learning)]()
- [Graph Partitioning]()
- [Graph Algorithms]()
- [Fast Fourier Transform]()
- [Climate Modeling]()
- [Sorting and Searching]()
- [Dynamic Load Balancing]()
- [Hierarchical Methods for the N-Body Problem]()
- [Computational Biology]()
- [Cosmology]()
- [Supercomputers & Superintelligence]()
- [Quantum Computing]()

### Grading

Grades will be based on the following distribution:

- Assignments: 60%
- Exam:
  - Exam 1: 15%
  - Exam 2: 10% (Comprehensive)
- Quiz: 10%
- Participation: 5%

Letter grades are assigned according to the following scale:

| Number | 100-93 | 92-90 | 89-87 | 86-83 | 82-80 | 79-77 | 76-73 | 72-70 | 69-67 | 66-63 | 62-60 | <= 59 |
| Letter | A	| A- | B+ | B | B- | C+ | C | C- | D+ | D | D- | F |


**Grading Appeals**

Mistakes occasionally happen during the grading process. If you think a mistake has been made regarding your grades, you should send me an email with detailed justification within one week of the date the grades are available. No changes on grades will be made after twenty days from the date the grades are posted.


### Class Policy

**Office Hours**

Office hours are an opportunity to reinforce course topics either one-on-one or in small groups. If you are unable to attend during the posted time slots, I am happy to make an appointment.


**Attendance**

- Attendance is critical to the success of students in.
- Attendance will be taken at random, and count toward your participation score.
- If you miss a class, you are responsible for obtaining lecture notes, handouts, and homework assignments from fellow students.
- If the instructor is late for class, please wait 20 minutes before leaving.


**Excused Absences Policy for University-Sanctioned Event**

- Students are advised to carefully read and comply with the excused absences policy for university-sanctioned events contained in the WCU Undergraduate Catalog.
- In particular, please note that the "responsibility for meeting academic requirements rests with the student," that this policy does not excuse students from completing required academic work, and that professors can require a “fair alternative” to attendance on those days that students must be absent from class in order to participate in a University-Sanctioned Event.


**Late Work**

- Without prior approval from the instructors, late homework assignments will not be accepted but will be assigned a grade of zero.

- Unless accompanied with a valid medical or University excuse, all late submissions will be penalized.
A make-up for the exams will be given only with a valid medical or University excuse.

**Electronic Mail Policy**

- It is expected that faculty, staff, and students activate and maintain regular access to University provided e-mail accounts.

- Official university communications, including those from your instructor, will be sent through your university e-mail account.

- You are responsible for accessing that mail to be sure to obtain official University communications. Failure to access will not exempt individuals from the responsibilities associated with this course.
Instructor Email Policy

- For individual issue, it is best to contact me via email. I check my email frequently during normal working hours (9-5) on weekdays, and I will try to respond quickly (hopefully the same day). I do also check email on weekends and evenings, but not nearly as frequently (almost never on Sundays). As a result, you should expect longer delays during these times.

- If you send me an assignment-related email right before a deadline, I may not answer it in time to be helpful.


### Academic Integrity

It is the responsibility of each student to adhere to the university’s standards for academic integrity. Violations of academic integrity include any act that violates the rights of another student in academic work, that involves misrepresentation of your own work, or that disrupts the instruction of the course. Other violations include (but are not limited to): cheating on assignments or examinations; plagiarizing, which means copying any part of another’s work and/or using ideas of another and presenting them as one’s own without giving proper credit to the source; selling, purchasing, or exchanging of term papers; falsifying of information; and using your own work from one class to fulfill the assignment for another class without significant modification. Proof of academic misconduct can result in the automatic failure and removal from this course.

For questions regarding Academic Integrity, Sexual Harassment, or the Student Code of Conduct, students are encouraged to refer to the “Other” Menu of the Computer Science web page www.cs.wcupa.edu/, the Undergraduate Catalog, the Ram’s Eye View, and the University website at www.wcupa.edu.

### Disability Accommodations
To know more about West Chester University’s Services for Students with Disabilities (OSSD), contact the OSSD which is located at 223 Lawrence Center. The OSSD hours of Operation are Monday  Friday 8:30 a.m.  4:30 p.m. Their phone number is 610-436-2564, their fax number is 610-436-2600, their email address is ossd@wcupa.edu, and their website is at www.wcupa.edu/ussss/ossd.
If you have a disability that requires accommodations under the Americans with Disabilities Act (ADA), please present your letter of accommodations to OSSD as soon as possible so that OSSD can support your success in an informed manner. Accommodations cannot be granted retroactively.


### Title IX Statement

- West Chester University and its faculty are committed to assuring a safe and productive educational environment for all students. In order to meet this commitment and to comply with Title IX of the Education Amendments of 1972 and guidance from the Office for Civil Rights, the University requires faculty members to report incidents of sexual violence shared by students to the University's Title IX Coordinator, Ms. Lynn Klingensmith.

- The only exceptions to the faculty member's reporting obligation are when incidents of sexual violence are communicated by a student during a classroom discussion, in a writing assignment for a class, or as part of a University-approved research project. Faculty members are obligated to report sexual violence or any other abuse of a student who was, or is, a child (a person under 18 years of age) when the abuse allegedly occurred to the person designated in the University protection of minors policy. Information regarding the reporting of sexual violence and the resources that are available to victims of sexual violence is set forth at the webpage for the Office of Social Equity at http://www.wcupa.edu/_admin/social.equity/.

- Ms. Lynn Klingensmith is the West Chester University Title IX Coordinator and is also the Director of Social Equity. She can be reached at 610-436-2433 or by email at LKlingensmith@wcupa.edu and can connect you to resources both on and on campus, as well as provide information about the processes related to cases of sexual misconduct.

- West Chester University community members also have a right to report acts of sexual misconduct to the Office of Civil Rights. They can be contacted at: The Wanamaker Building, 100 Penn Square East, Suite 515, Philadelphia, PA 19107-3323, (215) 656-8541, OCR.Philadelphia@ed.gov


### Emergency Preparedness

- All students are encouraged to sign up for the University’s free WCU ALERT service, which delivers official WCU emergency text messages directly to your cell phone.

- For more information, visit www.wcupa.edu/wcualert. To report an emergency, call the Department of Public Safety at 610-436-3311.
