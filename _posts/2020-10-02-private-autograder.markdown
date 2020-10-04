---
title:  "Docker-based runners for GitHub Autograding"
categories: technical document
tags:
  - GitHub Actions
  - Docker
---

In [Setup for remote synchronous instructions](https://www.cs.wcupa.edu/lngo/technical/document/remote-instructions/), 
I mentioned how my free Github Actions (GHA) minutes ran out the night before an assignment is due and I scrambled to 
setup `self-hosted` runners on our department's Linux server. I also acknowledge GitHub's gracious offer to refund all 
of my costs should I try to put credit card in and set a spending limit for the remainder of the month (when the free 
minutes are refreshed). In the end, both of these solutions do not seem adequate for the following reasons:

1. GitHub Classroom is becoming more and more popular, and I anticipate the amount of free minutes to be reduced 
futher (understandable).  
2. There is only one physical server for several runners from different classes. Should it come down (and it did!), 
students will not be able to submit their work for testing and grading purposes. 
3. Direct installation of runners limits runners' configurations (and therefore grading potential) to that particular 
server's setup. 

In the end, I want to to quickly deploy and scale multiple runners across different locations  (servers) dynamically. 
The solution is to leverage Docker to build runner image templates. When these templates are run as containers, the 
instructor can quickly add the final step of configuring the container runner to autheticate against the GitHub 
organization. In the remainer of this post, I describe the steps to setup a template to become an official runner. 


### Software descriptions

My setup runs on a Windows 10 desktop machine with the following software:

- [Docker Desktop 2.4.0](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
- [Windows Terminal App](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)
- [Windows Linux Subsystem 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (this is for driving Docker)

I will not discuss the setup of Docker Desktop and Windows Linux Subsystem 2 here, as there are many other excellent 
articles online regarding this specific topic. For Mac and Linux users, only Docker would be needed.

### Setup base runner image

- At the bottom of `Settings`/`Actions` menu of your GitHub organization/repository, you will see a section 
called **Self-hosted runners**. 
- Click `Add New`/`New Runner`. 

![new_runner]({{ "/assets/images/20201002/01.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

- We are going to use the commands in the `Download` section to setup our Docker image. 

![download_runner]({{ "/assets/images/20201002/01.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

- In your Windows Terminal, launch a baseline `Ubuntu` container using the following command:

~~~
$ docker run -it ubuntu bash
~~~

- Next, run the following commands as root inside the container

~~~
$ apt update
$ apt install -y curl tar build-essential
~~~

*I use this runner to autograde C programming assignments, so only gcc (part of `build-essential`) is needed. If you 
want other programming language supports, you need to run additional setup commands as needed.*

- GHA does not want the runner to be run as root, so we will need to create a non-root account called `grader`. 

~~~
$ adduser grader
~~~

- Since I do not anticipate this container being accessible from outside, I am fairly relaxed in selected a simple 
password for `grader` and keep all other options empty for the account creation process. 
- Next, change into `grader` and run the setup commands from GitHub Actions page. 

~~~
$ su grader
$ cd
$ mkdir actions-runner && cd actions-runner
$ curl -O -L https://github.com/actions/runner/releases/download/v2.273.4/actions-runner-linux-x64-2.273.4.tar.gz
$ tar xzf ./actions-runner-linux-x64-2.273.4.tar.gz
$ mv actions-runner-linux-x64-2.273.4.tar.gz ..
~~~

*I move downloaded tar file out of actions-runner after the decompression process for organizaitonal purposes*. 

- One additional step is needed, as the original Docker image lacks a number of supporting software that the GitHub 
runner needs. We need to turn back into root and run this steps. 

~~~
$ exit
$ cd /home/grader/actions-runner
$ bin/installdepedencies.sh
~~~

- Once this is done (you will need to interact with the installation process at the end to select timezones), exit 
out of the container. Remember the first four characters of your container ID. In this case, my container ID is 
`2311xxxxxxxxxx`.
- Turn the container into an image and push it to your DockerHub repository for storage purposes. 

~~~
$ docker commit 2311 linhbngo/csc331runner:0.1
$ docker push linbhngo/csc331runner:0.1
~~~

The runner template is now available online, and I can quickly pull and deploy them anywhere as needed. 

![dockerhub]({{ "/assets/images/20201002/03.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

### Deploying a runner

- First, we need to launch the runner container and change into the grader user.
- In a Windows Terminal, run the follwoings

~~~
$ docker run -it linhbngo/csc331runner:0.1 bash
$ su grader
$ cd actions-runner
~~~

- On the same GitHub page where you have the installation instruction for the runner, you will find the 
configuration information. 

![gha_config]({{ "/assets/images/20201002/04.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

- Copy and run the two commands in the `Configure` section. Congratulations, you now have a runner on your 
personal computer. From the figure below, you can see the runner has all ready accepts two jobs after one hour. 
The students are working hard!

![runner]({{ "/assets/images/20201002/05.png" | prepend: site.baseurl | prepend: '/' | prepend: site.url }})

