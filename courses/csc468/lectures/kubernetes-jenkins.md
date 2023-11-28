
# Kubernetes Application: CI/CD pipeline

## 0. CloudLab 

```{admonition} Setup
:class: dropdown

- Each student should launch one instance of the **k8s-helm** branch (9eb0508e) from my 
profile **csc468ngo**.
- When it gets to the `Parameterize` stage, set the following options
  - `Number of nodes`: 2
  - `CloudLab user ID to deploy K8s from (should be your CloudLab ID. Defaulted to none)`: 
  This should be your CloudLab user ID. 
  - `Number of cores in each node`: 4
  - `MB of RAM in each node`: 4096
- For cluster selection, go with `Emulab` 

```

## 1. Setup local private registry

```{admonition} Setup certifications
:class: dropdown

- After the experiment is fully deployed, SSH into the head node and 
run the following:

~~~bash
bash /local/repository/registry/setup_registry.sh
cp /local/repository/registry/docker-compose.yml .
docker-compose up -d
docker container ps
~~~

- You should see a registy container running with port mapping to 5000. 

``` 

```{admonition} Setup and test certificates from nodes
:class: dropdown

- SSH to **each node** of the experiment (including the head node) and 
run the followings

~~~bash
sudo cp -R /opt/keys/certs.d /etc/docker/
~~~

- Get the IP address from the head node using the following command

~~~bash
ip addr | grep eth0| awk -F ' ' '{print $2}' | awk -F '/' '{print $1'} | tail -n 1
~~~

- On each node, test that the certificates are working by login 
to the local docker registry using the following command
  - You should see a "Login Suceeded" message. 

~~~bash
docker login -u admin -p registry https://IP_ADDRESS_FROM_ABOVE:443
~~~

```

```{admonition} Setup Docker access for k8s
:class: dropdown

- On the head node, run the following
  - **Assume that you already run docker login to the private local registry on head node**
  - If your app is deployed inside a namespace, the `regcred` generic secret 
  creation command needs to be specified with that specific namespace as well. 

~~~bash
ip_addr=$(ip addr | grep eth0| awk -F ' ' '{print $2}' | awk -F '/' '{print $1'} | tail -n 1)
kubectl create secret generic registry-ca --namespace kube-system --from-file=registry-ca=/opt/keys/certs.d/${ip_addr}\:443/ca.crt
kubectl create -f /local/repository/registry/registry-ca-ds.yaml
kubectl create secret generic regcred --from-file=.dockerconfigjson=/users/${USER}/.docker/config.json --type=kubernetes.io/dockerconfigjson
~~~

```


## 2. Introduction to Jenkins

```{admonition} Introduction to Jenkins
:class: dropdown

- [Jenkins](https://www.jenkins.io/)
- Open-source automation server that allows continuous integration:
  - Recognized whenever source code is changed and/or updated. 
  - Automatic building and testing of updated codes.  
``` 

```{admonition} Deploy Jenkins on Kubernetes via Helm
:class: dropdown

- SSH to the headnode of your Kubernetes cluster. 

~~~bash
bash /local/repository/jenkins/deploy_jenkins.sh
bash /local/repository/jenkins/enable_sa.sh
~~~

- What did we just deploy: 
  - Configuration for Jenkins (Configuration-as-Code): [values.yaml](https://github.com/linhbngo/cloudlab/blob/k8s-helm/jenkins/values.yaml).
  - Enable the ClusterRoleBinding for **jenkins service account**.

- To get the URL to Jenkins, run the followings

~~~bash
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services jenkins)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT/login
~~~

- The login and password are: `pokemon`/`pikachu`.

```

## 2. Configure Jenkins


```{admonition} Configure Jenkins: SSH credentials
:class: dropdown

- On the CloudLab head node, run `ssh-keygen` (do not enter any password when asked). 
- Run `cat .ssh/id_rsa.pub >> .ssh/authorized_keys`
- Run `cat ~/.ssh/id_rsa` and copy the displayed text, including the starting 
and ending dashes without any extra spaces.  
- On Jenkins Dashboard, go to `Manage Jenkins`/`Manage Credentials`.
  - Click on domains `(global`) under `Stores scoped to Jenkins`.
  - Click on `Add Credentials`. 
- Fill in the boxes as follows:
  - `Kind`: SSH Username with private name
  - `Scope`: Global (Jenkins, nodes, items, all child items, etc)
  - `ID`: cloudlab
  - `Username`: Enter your CloudLab login username here. 
  - `Private Key`: Check `Enter directly`, click `Add`, then paster the previously
  copied private key to this box. 
  - Click `Create`. 

```

```{admonition} Configure Jenkins: Single executor
:class: dropdown

- On Jenkins Dashboard, go to `Manage Jenkins`/`Manage Nodes and Clouds`.
  - Click on the gear icon for `Built-In Node` 
- Fill in the boxes as follows:
  - `Number of executors`: 1
  - `Labels`: deploy
  - `Usage`: Only build jobs with label expressions matching this node

```


## 3. Launch pipelines

```{admonition} Setup a CI/CD application
:class: dropdown

- Fork the [`hello` repository](https://github.com/CSC603-WCU/hello) to your Git account
- Setup the API Token for `pikachu`:
  - On Jenkins main page, Go to `People`, then select `pokemon`, then go to `Configure`.
  - Scroll to `API Token`, `Add new Token` and generate one. You can name it `github`. 
  - Copy and store this token for today's class (`JENKINS_TOKEN`). 
- Setup the `webhook` for your repository. 
  - Go to your Git repository's `Settings`, and scroll to `Webhooks` 
  - Add a new webhook with the following configurations:
    - The Payload URL is of the following format: `http://pokemon:JENKINS_TOKEN@IP_ADDRESS:30000/github-webhook/` 
    - The Content type is `application/x-www-form-urlencoded`
- The composition of the files in the `go_app` branch includes:
  - `main.go`: The Go file that serves as the web server (the application to be deployed).
  - `main_test.go`: The Go file that serves as the test file (part of the CD process).
  - `Jenkinsfile`: Setup the pipeline for Jenkins to build, test, and push and deploy (if test is passed) the Go app. 
    - Edit the `registry` (line 6) to be the IP address of the `head` node. 
    - Change the `userid` value from `lngo` to your CloudLab username. 
    - **Be careful of capitalization in your CloudLab username. It has to match exactly**.
  - `Dockerfile`: The Docker image that will package the web server. 
  - `deployment.yml` and `service.yml`: K8 configuration files. 

```


```{admonition} Setup the CI/CD pipeline
:class: dropdown

- Login to the Jenkins server. 
- Select `New Item`, and create a new `Pipeline`named `go_server`.
- Scroll down to `Build Triggers`, select `GitHub hook trigger for GITScm polling`,
- Scroll down to `Pipeline`, select the followings: 
  - `Definition`: Pipeline script from SCM (*this will open new options*)
  - `Repository URL`: URL of the `hello` repository
  - `SCM`: Git
  - `Branches to build`: `go_app` 
- Click `Save`
- Click `Build Now` to activate the first build
- Open a new browser tab and visit the IP address of `head` at port 32000 to see the running server

```

```{admonition} CI/CD in action
:class: dropdown

- Edit `main.go` in `go_app` to introduce and error.
- Observe that the build failed, but the web server is still running. 
- Change `main.go` and also `main_test.go` so that the build and test can pass. 
- Observe the webserver updated after the build completes successfully. 

```
