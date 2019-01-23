---
layout: slide
title: Introduction to Cloud Computing
category: presentation
---

<section data-markdown>
## <center> Introduction to Cloud Computing </center>
</section>

<section data-markdown>
### Cluster Computing

- Prior to 1996, to achieve better computing performance (better speed, more memory, more storage ...), people relied on special-purpose computers (Cray, AIX).
- In 1996, the Beowulf model was developed, enabling construction of **computing clusters**:
  - Provide better overall performance than average computers,
  - Are designed by connecting individual standard computers (commodity off-the-shelves).
- Highly scalable (potentially infinite)
</section>

<section data-markdown>
### The Building is the Limit

- **Scaling out**: Adding additional computers of similar performance to an existing cluster of computers.
- Simple, inexpensive approach
- Limited by how much space available
- Limited by AC and power capacity

</section>

<section data-markdown>
### The Funding is the Limit

- **Scaling up**: Replacing existing computers in a cluster with better, fast computers
- More expensive
- More technical challenge to ensure stable performance

</section>

<section data-markdown>
### Difference in perspectives

- Academic: How can I get more performance with little funding that I have?
- Industry: How can I avoid investing money into fixed cost when I only need bursts of performance?

</section>

<section data-markdown>
### Next generations of cluster computing

- Grid Computing
- Cloud Computing

</section>

<section data-markdown>
### Grid Computing

- Bring together computing resources (clusters of computers) from geographically distributed locations.
- Individual resources are under separate administrative domains.
- Computing resources are highly heterogeneous (and the users have to take this into account).
- Keywords: sharing, collaboration, fine-grained access control, delegation ...

</section>

<section data-markdown>
### Grid Computing

- Started out as academic research project (U Chicago + U Southern California).
- Enables sharing of geographically different reources through **virtual organizations**.
- Computing resources are highly heterogeneous (and the users have to take this into account).
- A computing job with individual disjoint and asynchronous tasks can send these tasks over different resources in a grid computing federation.
- Suitable for academic research, not suitable for industry.

</section>


<section data-markdown>
### Cloud Computing

- Bring together computing resources from geographically distributed locations.
- Difference in administrative domains should be transparent to users.
- The heterogeneity of computing resources should be transparent to users.
- Any type of computing job should be executable in a cloud computing environment.

</section>

<section data-markdown>
### Grid and Cloud

![grid-cloud]({{ "/assets/images/csc-496-2/syllabus_slide/grid-cloud.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Cloud Computing: Early Definition

*A computing cloud is a set of network enabled services, providing scalable, QoS guaranteed, normally personalized, inexpensive computing infrastructures on demand, which could be accessed in a simple and pervasive way*

Wang L, Von Laszewski G, Younge A, He X, Kunze M, Tao J, Fu C. Cloud computing: a perspective study. New Generation Computing. 2010 Apr 1;28(2):137-46.

Cloud computing is too complex to be defined by just a sentence.

</section>


<section data-markdown>
### Cloud Computing: Formal Definition by NIST

- Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.
- https://csrc.nist.gov/publications/detail/sp/800-145/final
- How do we read this definition?

</section>

<section data-markdown>
### Cloud Computing: Formal Definition by NIST

Cloud computing is a model for enabling ubiquitous, convenient, **on-demand** network **access** to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.

</section>

<section data-markdown>
### Cloud Computing: Formal Definition by NIST

Cloud computing is a model for enabling ubiquitous, convenient, **on-demand** network **access** to a **shared pool** of **configurable** computing **resources** (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.

</section>

<section data-markdown>
### Cloud Computing: Formal Definition by NIST

Cloud computing is a model for enabling ubiquitous, convenient, **on-demand** network **access** to a **shared pool** of **configurable** computing **resources** (e.g., networks, servers, storage, applications, and services) that can be **rapidly provisioned** and released with **minimal management** effort or service provider interaction. This cloud model is composed of five essential characteristics, three service models, and four deployment models.

</section>

<section data-markdown>
### Cloud Computing: Five Essential Characteristics

- On-demand self-service
- Broad network access
- Resource pooling
- Rapid elasticity
- Measured service

</section>

<section data-markdown>
### Cloud Trend

![grid-cloud]({{ "/assets/images/csc-496-2/syllabus_slide/cloud-trend.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Cloud Computing: Three Service Models

- Software as a Service (SaaS)
- Platform as a Service (PaaS)
- Infrastructure as a Service (IaaS)

</section>

<section data-markdown>
### Cloud Providers

![grid-cloud]({{ "/assets/images/csc-496-2/syllabus_slide/cloud-major-providers.PNG" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

</section>

<section data-markdown>
### Cloud Computing: Four Deployment Models

- Private Cloud
- Community Cloud
- Public Cloud
- Hybrid Cloud

</section>

<section data-markdown>
## <center> NIST: Essential Characteristics </center>
</section>

<section data-markdown>
### On-demand self-service
- Computing capabilities can be automatically and **unilaterally** provisioned by users **without human interaction** with the cloud provider.
- What are computing capabilities
  - server time, network storage, number of servers ...
</section>

<section data-markdown>
### Broad network access
- Computing capabilities:
  - are made available over the (high speed) network
  - can be accessed through standard mechanisms
- This enables inclusion of henetogeneous computing platforms
</section>

<section data-markdown>
### Resource pooling
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
### Rapid elasticity
- Capabilities (or resources) can be rapidly and elastically provisioned.
- From users' perspective, resources are potentially unlimited.
- Cloud providers should approach users with an understanding that predicting a ceiling of usage is difficult.
</section>

<section data-markdown>
### Measured service
- Capability of service/resource abstractions are metered:
  - storage
  - processing
  - bandwidth
  - active user accounts
  - ...
</section>
