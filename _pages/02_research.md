---
layout: single
title: Distributed Computing Infrastructure Lab
permalink: /research/
author_profile: true
---

The EDGE (DistributED computinG infrastructurE) lab evaluate the design, performance, and security aspects of complex distributed computing infrastructures.  

**Current Research**

*Performance evaluation of message-oriented middleware (MOMS):*

In modern large-scale platforms, MOMS plays an important role in facilitating asynchronous data communications between computing components and computational stages. This study carries out an evaluation of common MOMS frameworks regarding their performance, scalability, and resiliency.

Student: Mahmoud Gudarzi

*Performance evaluation of virtualization platforms:*

Metrics of performance regarding computational speed, memory and network bandwidth, and I/O are measured for popular virtualization platforms, including Docker, KVM, Singularity and benchmarked against bare-metals.

Student: Thomas Boudwin

*Docker-based HPC infrastructures:*

This project develops a Docker profile that contains all relevant components of a high performance computing infrastructures, including
login nodes, scheduler, compute nodes, and parallel file systems. The goal is to create a light-weight cloud-based HPC blueprint that can either be deployed on small platforms (or single PCs) for educational purposes or on large-scale platforms in conjunction with Docker Swarm/Kubernetes for production activities.

Student: Jon Kilgannon

*Developing complex workflows to support data-driven scientific discovery:*

Scientific process includes both computation and data, and nowadays, every discipline is becoming data rich. It is critical for researchers to move beyond the traditional computing model based on Beowulf network of computers (separation of computation and storage) toward a more flexible and dynamic model. This model should be resilient, fault-tolerant, and scalable across distributed resources, support in-situ data analytics, and limit data movement.
There exist several workflow management systems for extreme-scale applications. Most of them are developed from scratch and represent latest advance in computer science research. At the same time, this creates uncertainty for domain scientists to utilize these systems in production environment. The adoption of these systems is often depended upon existing collaborators and institutional relationship, and to date, there has been few efforts to carefully study advantages and disadvantages of each system. I am interested in carrying out in-depth performance evaluations of these workflow management systems using various scientific workflows from different disciplines. Based on this result, I will further extend the ScaFFS framework to support aspects of complex scientific workflows including in-situ analytic. This project will use 1) public national computing resources as a massive experimental testbed for the development and deployment of infrastructures supporting these workflow systems; 2) open-source scientific software to drive the actual workflows.; and 3) hardened computing and big data infrastructures that are utilized in academic and industry production computing environments.  

*Transforming general education through the integration of computational and data literacy into undergraduate curriculum:*

Over the last decade, data-driven research and discovery has moved to the forefront of all academic disciplines, establishing the fourth pillar of scientific discovery: data science. Integral to data-driven research are cyberinfrastructure (CI) resources and users capable of harnessing the potential of these resources.  Previous federal support has enabled the widespread availability of advanced CI resources through large-scale efforts such as XSEDE and OSG, but ultimately the successful and efficient utilization of these resources to advance data-driven science will depend on having knowledgeable end users who understand how to integrate and apply modern high-performance computing to real world problems. Outside of computer science (CS), this type of educational contents is typically not available in undergraduate curriculum of other disciplines and is only achievable through means such as taking additional CS courses, attending non-academic workshops (if available at local institutions), or pursuing MOOC courses. These approaches require extra time and efforts from students. Educational contents in these courses are often generic and do not teach students how to customize and apply what they learned to domain-specific contexts.  Furthermore, except for MOOC, the other two approaches are not scalable for students across all disciplines. For a common solution for computational and data literacy that is sustainable and applicable across all disciplines, it is critical that we no longer think of the acquisition these skills and knowledge as an interdisciplinary effort but rather an integral part within any discipline. To achieve this goal, a comprehensive collaboration among the following key CI stakeholders, CI professionals, faculty, administrators, and students, is needed. I am interested in studying technologies and frameworks through which this collaboration can be facilitated and sustained. At the core of this research activity is the collaborative development of CI training activities combining with student participation and feedback can help to achieve the following goals: 1) identifying a common baseline for CI requirements in general education across different disciplines; 2) creating an extensive collection of CI-enabled modules that can be integrated into general education and upper-level domain-specific courses; and 3) establishing learning outcomes to assess CI-enabled materials to formalize these integrations into existing curriculums.



**Past Research**

*A Distributed Message Delivery Infrastructure for Connected Vehicle Technology Applications (2016 - 2017):*

This project presents a strategy for creating an efficient and low-latency distributed message delivery system for CV applications using a distributed message delivery platform. This strategy enables large-scale ingestion, curation, and transformation of unstructured data (roadway traffic-related and roadway non-traffic-related data) into labeled and customized topics for a large number of subscribers or consumers, such as CVs, mobile devices, and data centers. The performance of this strategy is evaluated by developing a prototype infrastructure using Apache Kafka, an open source message delivery system, and compared its performance with the latency requirements of CV applications. The experiments of the message delivery infrastructure are performed on two different distributed computing testbeds at Clemson University: the Holocron cluster and the Palmetto cluster to measure the latency of the message delivery system for a variety of testing scenarios. These experiments reveal that measured latencies are less than the U.S. Department of Transportation recommended latency requirements for CV applications, which prove the efficacy of the system for CV related data distribution and management tasks.


*Scalable Forward Flux Sampling, ScaFFS: Software platform to study rare events in molecular simulations (2015-2016):*

This project develops a novel software platform called Scalable Forward Flux Sampling (ScaFFS) to perform large scale forward flux sampling (FFS) calculations. FFS is an advanced sampling technique developed to enhance the sampling of rare events in molecular simulations. Rare events, by definition, are events that have very low probability of occurring in the typical observation timescales. They often mark an important transition and are processes of considerable interest. In materials science, several important processes such as nucleation driven phase transitions are rare events. Studying such processes through molecular simulations tools is challenging since the waiting time for them to occur is longer than the common timescales spanned through straightforward simulations. Consequently, majority of the computational effort is wasted on the uninteresting part of waiting for the event to occur. ScaFFS represents a collaboration of state-of-the-art techniques in molecular simulations with those from Big Data to enable rare event simulations at massive scales. ScaFFS is designed to be adaptive, data-intensive, high-performance. ScaFFS is actively used for current research in molecular modeling and computer simulations at Clemson University.

*Synthetic data generation for the internet of things (2014-2015):*

The concept of Internet of Things (IoT) is rapidly moving from a vision to being pervasive in our everyday lives. This can be observed in the integration of connected sensors from a multitude of devices such as mobile phones, healthcare equipment, and vehicles. There is a need for the development of infrastructure support and analytical tools to handle IoT data, which are naturally big and complex. But, research on IoT data can be constrained by concerns about the release of privately owned data. In this project, funded by our industry partner, we designed and implemented of a synthetic IoT data generation framework. The framework enabled research on synthetic data that exhibit the complex characteristics of original data without compromising proprietary information and personal privacy.


*Evaluating the effect of cyberinfrastructure on universities' production process (2012-2015):*

This project undertakes an interdisciplinary and novel approach to the problem of measuring the effects of investment in cyberinfrastructure to universities' production processes of research outputs and vital educational services. A decision to support funding of the infrastructure that supports research, or a decision to support funding of focused research activities, is an increasingly critical decision with far-reaching impacts not only to the institutions receiving those funds, but also to national competitiveness. While it is generally agreed that cyberinfrastructure is essential to scholarly inquiry in some science fields, the scope of cyberinfrastructure's broad effects on the growth of knowledge, to the academic enterprise, and to areas of science has not been explicitly quantified. Using new central limit theorems and hypothesis testing techniques, we applied frontier efficiency analysis to examine the impact of policy about cyber infrastructure on the efficiency of institutional research performance. During the project, we have utilized HPCC, an alternative data infrastructure, to ingest, curate, and integrate large amount of higher education data from various sources. We have also proposed the adoption of social media paradigm onto academic research publication environment. The outcomes of the project have been presented and well received at professional venues such as Birds-of-a-Feather Sessions in Supercomputer 2013 and 2014, and at the annual Coalition for Academic Scientific Computation meeting.
