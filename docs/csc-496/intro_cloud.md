---
layout: slide
title: Introduction to Cloud Computing (cont.)
category: presentation
---

<section data-markdown>
## <center> NIST: Essential Characteristics </center>
</section>


<section data-markdown>
### On-demand self-service (C1)
- Computing capabilities can be automatically and **unilaterally** provisioned by users **without human interaction** with the cloud provider.
- What are computing capabilities
  - server time, network storage, number of servers ...
</section>


<section data-markdown>
### Broad network access (C2)
- Computing capabilities:
  - are made available over the (high speed) network
  - can be accessed through standard mechanisms
- This enables inclusion of heterogeneous computing platforms
</section>


<section data-markdown>
### Resource pooling (C3)
- Computing resources of cloud provider are pooled together to server multiple users.
- Computing resources can be storage, processing power, memory, network bandwidth, and virtual machines.
- Location independence
  - Users have not control over exact location of resources
- Carry significant implications over
  - performance
  - scalability
  - security
</section>


<section data-markdown>
### Rapid elasticity (C4)
- Capabilities (or resources) can be rapidly and elastically provisioned.
- From users' perspective, resources are potentially unlimited.
- Cloud providers should approach users with an understanding that predicting a ceiling of usage is difficult.
</section>


<section data-markdown>
### Measured service (C5)
- Capability of service/resource abstractions are metered:
  - storage
  - processing
  - bandwidth
  - active user accounts
  - ...
</section>


<section data-markdown>
## <center> Enabling Technologies </center>
</section>


<section data-markdown>
### Overview of Enabling Technologies for Cloud Computing (equal order of importance)
- Broadband networks and Internet architecture
- Data center technology
- Virtualization technology
- Web technology
- Multi-tenant technology
</section>


<section data-markdown>
### Broadband networks and Internet architecture
- Everything is connected, with relatively high spped.
</section>


<section data-markdown>
### Broadband networks and Internet architecture

[Durairajan, R., Barford, P., Sommers, J. and Willinger, W., 2015, August. **InterTubes: A study of the US long-haul fiber-optic infrastructure**. In ACM SIGCOMM Computer Communication Review (Vol. 45, No. 4, pp. 565-578). ACM.](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p565.pdf)
</section>


<section data-markdown>
### Broadband networks and Internet architecture

[Internet 2 Timeline](https://www.internet2.edu/about-us/internet2-community-timeline/)
</section>


<section data-markdown>
### Data Center Technology

- Standardization and Modularity
  - Commodity off-the-shelf (Beowulf model)
  - Modular architecture (Linux-based software stacks)
- Automation
  - Orchestration Software (Chef, Ansible, Salt ...)
- Remote Operation and Management
  - On-board controller
  - Network technologies
</section>


<section data-markdown>
### Virtualization Technology

- Converting a physical resource into a virtual resource
- Concept almost as old as the computer itself (Operating System class)
</section>


<section data-markdown>
### Virtualization Technology: Virtual Machine

[Barham, P., Dragovic, B., Fraser, K., Hand, S., Harris, T., Ho, A., Neugebauer, R., Pratt, I. and Warfield, A., 2003, October. **Xen and the art of virtualization.** In ACM SIGOPS operating systems review (Vol. 37, No. 5, pp. 164-177). ACM.).](http://users.ece.cmu.edu/~dawnsong/teaching/s04/papers/xen-sosp.pdf)
</section>


<section data-markdown>
### Virtualization Technology: Virtual Machine

![xen]({{ "/assets/images/csc-496-2/intro_cloud/xen.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Virtualization Technology: Container-based Virtualization

[Soltesz, S., Pötzl, H., Fiuczynski, M.E., Bavier, A. and Peterson, L., 2007, March. **Container-based operating system virtualization: a scalable, high-performance alternative to hypervisors**. In ACM SIGOPS Operating Systems Review (Vol. 41, No. 3, pp. 275-287). ACM.](http://www.cs.toronto.edu/~demke/2227/S.14/Papers/p275-soltesz.pdf)
</section>


<section data-markdown>
### Virtualization Technology: Software-Defined Networking

[Kreutz, D., Ramos, F.M., Verissimo, P.E., Rothenberg, C.E., Azodolmolky, S. and Uhlig, S., 2015. **Software-defined networking: A comprehensive survey**. Proceedings of the IEEE, 103(1), pp.14-76.](https://arxiv.org/pdf/1406.0440)
</section>


<section data-markdown>
### Virtualization Technology: Software-Defined Networking

Conventional Network

![network]({{ "/assets/images/csc-496-2/intro_cloud/network.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Virtualization Technology: Software-Defined Networking

Software-Defined Network

![sdn]({{ "/assets/images/csc-496-2/intro_cloud/software-defined-networking.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Web Technology

- Uniform resource locator (URL)
- Hypertext transfer protocol (HTTP)
- Markup languages (HTML, XML)
- Web applications
</section>


<section data-markdown>
### Multi-tenant Technology

[Bezemer, C.P., Zaidman, A., Platzbeecker, B., Hurkmans, T. and Hart, A.T., 2010, September. Enabling multi-tenancy: An industrial experience report. In Software Maintenance (ICSM), 2010 IEEE International Conference on (pp. 1-8). IEEE.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.176.8005&rep=rep1&type=pdf)

- "Multiple customers - tenants share the same application and database instance. All the while, the tenants enjoy a highly configurable application, making it appear that the application is deployed on a dedicated server."
</section>


<section data-markdown>
### Hands-on

- taz
- CloudLab
</section>


<section data-markdown>
### Getting on taz

- Log into taz.cs.wcup.edu (If you have Windows, [MobaXterm Home Installer Edition](https://mobaxterm.mobatek.net/download-home-edition.html) is recommended. )

```
$ ssh taz.cs.wcupa.edu
```

- If you have not already done so, set up and view your SSH public key (use default answers for all questions).

```
$ ssh-keygen -t rsa
$ cat .ssh/id_rsa.pub
```

- Use this key in your CloudLab project application request form.
- If you already have a CloudLab account, add this key to your CloudLab account.
</section>
