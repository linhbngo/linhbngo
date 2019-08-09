---
layout: slide
title: Introduction to CloudLab
category: presentation
---

<section data-markdown>
## <center> Cloud Infrastructures </center>
</section>


<section data-markdown>
### What constitutes a cloud provider?

- CloudLab: public information on an academic cloud infrastructure
- Google Compute Engine and Amazon Web Services: proprietary cloud provider with limited information. 
</section>


<section data-markdown>
### Recall: Essential Characteristics
- On-demand self-service (C1)
- Broad network access (C2)
- Resource pooling (C3)
- Rapid elasticity (C4)
- Measured service (C5)
</section>

<section data-markdown>
### What is CloudLab?
  - Experimental testbed for future computing research.
  - Allow researchers control to the bare metal.
  - Diverse, distributed resources at large scale.
  - Allow repeatable and scientific design of experiments.
</section>


<section data-markdown>
![cloudlab]({{ "/assets/images/csc-496-2/intro_cloudlab/architecture.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### What is GENI?
- Global Environment for Networking Innovation
- *Combining heterogeneous resource types, each virtualized along one or more suitable dimensions, to produce a single platform for network science researchers*
</section>


<section data-markdown>
### C2 and C3?

![geni]({{ "/assets/images/csc-496-2/intro_cloudlab/geni.jpg" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### C1 and C5?

![geni-lifecycle]({{ "/assets/images/csc-496-2/intro_cloudlab/geni-lifecycle.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### C4 is not available due to the nature of research work and the fact that resources are hosted by academic institutions
</section>


<section data-markdown>
## <center> Enabling Technologies for GENI/CloudLab </center>

- Broadband networks and Internet architecture
- Data center technology
- Virtualization technology
- Web technology
- Multi-tenant technology
</section>


<section data-markdown>
### Broadband networks and Internet architecture

![geni-net]({{ "/assets/images/csc-496-2/intro_cloudlab/geni-networks.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})
</section>


<section data-markdown>
### Data Center Technology

- [GENI-specific Tools](http://groups.geni.net/geni/wiki/GENIDeveloper/Repositories)
</section>


<section data-markdown>
### Virtualization Technology

- GENI racks: virtualized computation and storage resources
- Software-defined networks (SDNs): virtualized, programmable network resources
- WiMAX: virtualized cellular wireless communication
- CloudLab: Provide bare-metal platforms
</section>


<section data-markdown>
### Other key experimental concepts

- Scliceability: the ability to support virtualization while maintaining some degree of isolation for simultaneaous experiments
- Deep programmability: the ability to influence the behavior of computing, storage, routing, and forwarding components deep inside the network, not just at or near the network edge.
</section>


<section data-markdown>
### Utah/HP: Low-power ARM64 (785 compute nodes)

- 315 m400: 1X 8-core ARMv8 at 2.4GHz, 64GB RAM, 120GB flash
- 270 m510: 1X 8-core Intel Xeon D-1548 at 2.0GHz, 64GB RAM, 256GB flash
- 200 xl170: 1X 10-core Intel E5-2640v4 at 2.4Ghz, 64GB RAM, 480GB SSD
</section>


<section data-markdown>
### Suitable for experiments that:

- explore power/performance tradeoff
- want instrumentation of power and temperature
- want large numbers of nodes and cores
- need bare-metal control over switches
- want tight ARM64 platform integration
</section>


<section data-markdown>
### Wisconsin/Cisco (530 nodes)

-  90 c220g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
-  10 c240g1: 2X 8-core Intel Haswell at 2.4GHz, 128GB RAM, 1X 480GB SDD, 1X 1TB HDD, 12X 3TB HDD
- 163 c220g2: 2X 10-core Intel Haswell at 2.6GHz, 160GB RAM, 1X 480GB SDD, 2X 1.2TB HDD
-   7 c240g2: 2X Intel Haswell 10-core at 2.6GHz, 160GB RAM, 2X 480GB SDD, 12X 3TB HDD
- 224 c220g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD
-  32 c240g5: 2X 10-core Intel Skylake at 2.20GHz, 192GB RAM, 1TB HDD, 1 NVIDIA P100 GPU
-   4 c4130: 2X 8-core Intel Broadwell at 3.20GHz, 128GB RAM, 2X 960GB HDD, 4 NVIDIA V100 GPU
</section>


<section data-markdown>
### Suitable for experiments that:

- want large number of nodes/cores, and bare metal control over nodes/switches
- want network I/O performance, intra-cloud routing, and transport
- network virtualization
- in-memory big data frameworks
- cloud-scale resource management and scheduling
</section>


<section data-markdown>
### Clemson/Dell (256 nodes)

- 96 c8220: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 2X 1TB HDD
-  4 c8220x: 2X 10-core Intel Ivy Bridge at 2.2GHz, 256GB RAM, 8X 1TB HDD, 12X 4TB HDD
- 84 c6420: 2X 14-core Intel Haswell at 2.0GHz, 256GB RAM, 2X 1TB HDD
-  2 c4130: 2X 12-core Intel Haswell at 2.5GHz, 256GB RAM, 2X 1TB HDD, 2 NVIDIA K40m GPU
-  2 dss7500: 2X 6-core Intel Haswell at 2.4GHZ, 128GN RAM, 2X 126GB SSD, 45X 6TB HDD
- 72 c6420: 2X 16-core Intel Skylake at 2.6GHZ, 386GB RAM, 2X 1TB HDD
-  6 ibm8335: 2X 10-core IBM POWER8NVL at 2.86GHz, 256GB RAM, 2X 1TB HDD, 1 NVIDIA Tesla P100
</section>


<section data-markdown>
### Suitable for experiments that:

- need large per-core memory
- want to experiment with IB and/or GbE networks
- need bare-metal control over switches
- experiment with PowerPC architecture
</section>


<section data-markdown>
### Hands-on: Get on CloudLab!
</section>