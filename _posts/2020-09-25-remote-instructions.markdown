---
title:  "Setup for remote synchronous instructions"
categories: technical document
tags:
  - remote instructions
  - synchronization
  - Zoom
  - GitHub Classroom
  - Microsoft OneNote
---

My primary goal in delivering remote synchronous lecture is to 
provide students with a learning environment that is at least 
equivalent to a face-to-face (F2F) one. It should be noted that I 
do not want to strive to make RSI to be the same as F2F. Each of 
them has their own strengths and weaknesses. Comparing them would 
be akin to comparing apples to oranges. To accomplish this primary 
goal, I want the followings:

1. Communications between faculty and students are well maintained 
during lectures and office hours. 
2. Class materials are readily accessible. 
3. Students are able to do in-class hands-on activities.
4. Assessments are streamlined with fast turn-around time. 

I have finally arrived at a setting that satisfies the above requirements 
and is fairly well-received by the students. This setting includes the 
following components:

- Communication: Zoom, Microsoft OneNote, D2L (LMS)
- Publication: GitHub, Markdown, Jekyll
- Computing environment: virtual machine, XSEDE
- Assessments: GitHub Classroom

![rsi]({{ "/assets/images/20200925/rsi.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Components supporting remote synchronous instruction*

### Communication

At my institution, [Zoom](https://zoom.us/) is the standard communication tool for RSI. 
Zoom provides clear voice communication and reasonably good video 
streaming for remote synchronous lecturing. In one of my largest sessions, 
I was able to lecture to more than 40 students without any communication 
issue. 

On the other hands, there comes a time when Zoom sharing/video streaming 
is not enough and the traditional white board is needed. I have seen other 
faculty's Zoom setup with camera zooming into a physical white board to 
support their lecture. In my case, white board is extremely useful when it 
is needed, but the frequency is not high enough to justify a large setting. 
In the end, I turned to [Microsoft OneNote](https://www.onenote.com/) as a 
solution. A notebook is created and shared. I used a notepad (iPad in my case 
but any notepad with stylus will work) to draw on the notepad like a whiteboard. 
The main computer with Zoom also view this notepad via a shared link. This 
link is also posted on D2L, our instituional LMS. Students can follow either the 
shared Zoom screen or the shared OneNote link. 

![onenote]({{ "/assets/images/20200925/onenote.jpg" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Sharing of Microsoft OneNote notebook*

With numerous different components, a repository of resource links is needed. I created 
a module inside [D2L](https://www.d2l.com/) for this purpose. Contents of this module 
include passworded links to Zoom lectures, document containing information and link to Zoom 
office hours, and document containing links to Zoom recordings. Links for GitHub Classroom 
assignments are also provided via D2L's assignment page. D2L's Discussion Forum and Class Email 
capabilities are utilized to support out-of-class communication channels between myself 
and the students and also among the students. 

![d2l]({{ "/assets/images/20200925/d2l.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Module containing information links*

### Publication

Publication in this case means the availability of **all** course materials. During 
my first few semesters, I have used the traditional PowerPoint slides. I found this 
approach to be cumbersome due to large amount of source codes accompanying my 
lectures. To overcome this issue, I turned to [Markdown](https://daringfireball.net/projects/markdown/), 
[Jekyll](https://jekyllrb.com/), and the template from 
[Software Carpentry](https://carpentries.github.io/workshop-template/) to create and 
maintain my course materials, including both website and lecture slides. Markdown 
allows me to simply *write* my slide, and the customized template driven by Jekyll 
allows me to quickly rebuild and deploy my course materials. 

![main_page]({{ "/assets/images/20200925/main_page.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Main course website with the front page acts as the syllabus*

Each lesson is contained in a page under the **Episodes** drop-down menu. Within each lesson, *slides* 
are created by modifying the .css and javascript syntax of the original template. 

![slide_1]({{ "/assets/images/20200925/slide_1.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*A lecture (episode) with minimized slides*

The clickable header of slides allows the slides to be expanded/minimized in order to 
resemble the organization of a slide deck. Nested slide structure can be created to form 
Challenge/Solution slides. Source codes are embedded and highlight through [Gist](https://gist.github.com/). 

![slide_2]({{ "/assets/images/20200925/slide_2.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Expanded slide with embedded C source code*

An example course page for Computer System can be found [here](https://www.cs.wcupa.edu/lngo/csc231/). 

### Computing environment

A remote learning environment often means students are cut off from 
on-campus resources. This includes technical support from university IT staff 
and, more importantly, student peers. Given that individual students will have 
their own computing devices with widely varied hardware and software configurations, 
I consider it very important to strive for a common computing platform for learning. 

For this semester, my courses include Computer Systems, Operating Systems, and 
Distributed and Parallel Computing. All three courses are Unix-based and use the C 
programming language. Therefore, all three courses will have their own learning platform. 
For Computer Systems, students access a remote Linux server hosted within the department. 
For Operating Systems, due to the needs to have administrative access, students setup 
[VirtualBox](https://www.virtualbox.org/) and build their own virtual Linux machine. For 
Parallel and Distributed Computing, students utilize the Bridge Supercomputer available 
via [XSEDE](https://www.xsede.org/). These commont platforms allow lecture materials, 
source codes, and technical troubleshooting to be streamlined. The only two issues that 
came up was the software conflict between VirtualBox and older Windows versions on some 
students' laptop and the one time when the departmental server came down. 

### Assessment

The evaluation process of programming assignments in my courses are completely automated. 
This allows for instantaneous feedback upon submission in a manner similar to industry' 
CI/CD pipeline. Previously, we used [Submitty](https://submitty.org/index/overview) as 
our departmental autograder. However, we found the effort to setup and maintain Submitty 
and its corresponding gradeables still significant for our department. In summer 2020, I 
switched to [GitHub Classroom](https://classroom.github.com/classrooms). 

![ghc]({{ "/assets/images/20200925/ghc.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*My Github Classrooms*

GitHub Classroom (GHC) provides the infrastructure to organize students within classes and sections, 
develop assignments and tests, and facilitate automated testing and feedback. GHC's UI to 
create tests is fairly intuitive, and it was straightfoward to transform existing 
assignments and gradeables from Submitty to GHC. GHC turns individual students' assignemnts 
into their own private Git repository, and [GitHub Actions (GHA)](https://github.com/features/actions), 
an workflow automation feature of GitHub, is used for testing purposes. GHA is a cloud 
resource. Any time a student commits and pushes to their repository, a virtual machine is 
spinned up, runs the test scripts, and provides feedback under the form of a `pull request` to 
the student' repository. 

![gha]({{ "/assets/images/20200925/gha.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Students' commit counts and grades for one assignment*

All faculty are qualified for a free GitHub classroom account, which enables a free 2000-minute 
of GHA run time per month. I have learned that this amount will run out **very quickly** near the 
due date of an assignment. Fortunately, GitHub also allows the addition of "self-hosted" runners, 
user-provided compute instances that can be configured to link to the GitHub classroom organization 
and carry out the autograding tasks. For two of my classes (four sections in total), this has to 
be done as my per-class GitHub Action minutes ran out the night before the assignments are due!!!

![runners]({{ "/assets/images/20200925/runners.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
*Two runners ready to grade for one class*

### Conclusion and Lesson Learned

Overall, my RSI setup works well up to date. While there has been no formal students evaluation 
administered since we all went online, this setting has enabled a high level of students engagement 
(verbal/chat questions and discussions), and more importantly, there has been very few instances 
of downtime due to technology failures. The online format actualy lends itself well to hands-on 
activities in computer science. For example, in F2F, hands-on errors are often addressed 
individually and possibly repeatedly (students having the same error sitting far away). In RSI, 
students are asked to share their hands-on errors and helping one means helping many others with 
the same issue. 

Despite my best efforts to anticipate and provide documentation for errors, they still happen. In 
many cases, the issues are with the diversity in hardware and software configurations of students' 
personal computers. This is something that we do not have control over, and we have to keep doing 
our best to prepare. In the end, remote computing resources continue to be the optimal solution for 
all scenario. 