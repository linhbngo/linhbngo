
# Docker Compose


## 1. Docker Compose

```{admonition} Why?
:class: dropdown

- Dockerfiles are great for building container images.
- Dockerfiles are not quite satisfactory if you have to link multiple containers 
into a complex infrastructure.
- We want the ability to write custom scripts (program everything!) to automatically build, 
run, and connect containers together. 
- This is possible via Docker Compose.
- For Podman, it is called Buildah. 

```

```{admonition} In a nutshell
:class: dropdown

- External, Python-based tool. 
- Open source.
- Simple deployment workflow
  - Checkout code
  - Run `docker-compose up`
  - Everything is up and running!

```

```{admonition} Overview of compose
:class: dropdown

- Design of a container stack is described in a YAML file called `docker-compose.yml`.
- Run `docker-compose up`.
- Compose automatically pulls images, builds containers, and starts them. 
- Compose can
  - Set up links, volumes, and other Docker options for the container stack. 
  - Run containers in the background or in the foreground.

```


## 2. Demonstration

```{admonition} The ramcoin miner!
:class: dropdown

- Run the following commands:

~~~bash
cd
git clone https://github.com/CSC468-WCU/ram_coin.git
cd ram_coin
~~~

- Each member of a group should talk among yourseves and edit line 17 of the 
`docker-compose.yml` file to an appropriate and non-overlapping port.
- Run

~~~
docker-compose up
~~~

- Visit `YOUR_CLOUDLAB_HEADNODE:YOUR_CHOSEN_PORT` to see the deployed webserver. 
- Does it work?
- Open another terminal, connect to your CloudLab headnode and run `docker ps` to see 
how many containers were deployed by the docker-compose. 
- Press `Ctrl-C` to stop the containers. 

```


```{admonition} Sections of a compose file
:class: dropdown

- Use `cat` or `nano` to view `docker-compose.yaml` file. 
- `version` is mandatory (“2” or later).
  - Version 1 is legacy.
  - Version 2 has support for networks and volumes.
  - Version 3 has support for deployment options.
- `services` is mandatory. A service is one or more replicas of the same 
image running as containers.
- `networks` is optional and indicates to which networks containers should be connected. 
By default, containers will be connected on a private, per-compose-file network.
- `volumes` is optional and can define volumes to be used and/or shared by the containers. 

```

```{admonition} Containers in docker-compose.yaml
:class: dropdown

- Each service in the YAML file must container either `build` or `image`.
- `build` indicates a path containing a Dockerfile.
- `image` indicates an image name (local or on registry).
- If both are specified, an image will be built from the build directory and named `image`
- Other parameters are optional and typically what you would add to docker run
  - command = CMD
  - ports = -p
  - volumes = -v

```

```{admonition} Hands-on: Rerun ram_coin in background
:class: dropdown

~~~bash
docker-compose -d up
docker-compose ps
~~~

```

```{admonition} Hands-on: cleanup
:class: dropdown

~~~bash
docker-compose kill
docker-compose rm
~~~

```

