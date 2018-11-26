---
layout: post
title:  "Setup AutoLab"
date:   2018-11-25 14:45:00 -0500
categories: lecture
---


In an effort to improve efficiency and to provide more detailed feedback to student, 
we are looking into implementation and deployment of autograders. In this post, I describe 
the process of configuring and deploying a test instance of Carnegie Mellon University's 
[Autolab](http://www.autolabproject.com/).

The target operating system is Ubuntu 18.04. Initially, I tried Autolab's 
[OneClick option](https://autolab.github.io/docs/one-click/). However, there are various errors 
happened along the way, and using OneClick doesn't help with the debugging process. In the end, 
I decided to follow the manual installation guide. 

#### Installing AutoLab

The following commands are embedded in Autolab's `setup.sh` script. However, with Ubuntu 18.04, it 
is better to manually run these commands so that you have more control over what is being done. 

```
 $ sudo apt-get -y -qq update
 $ sudo apt-get -y -qq upgrade
 $ sudo apt-get -y install aptitude
 $ sudo aptitude install build-essential git libffi-dev zlib1g-dev autoconf bison libssl1.0-dev libyaml-dev libreadline6-dev libncurses5-dev libgdbm5 libgdbm-dev libmysqlclient-dev
```

*Note: Comparing to the original script, libssl-dev is changed to libssl1.0-dev, and libgdbm3 is changed to 
libgdbm5. To help with the potential dependency issues, I used aptitude instead of apt-get.*

In the original documentation, we have

```
$ AUTOLAB_SCRIPT=`mktemp` && \curl -sSL https://raw.githubusercontent.com/autolab/Autolab/master/bin/setup.sh > $AUTOLAB_SCRIPT && \bash $AUTOLAB_SCRIPT
```

We will need to make several changes the `setup.sh` script. We start by running:

```
$ AUTOLAB_SCRIPT=`mktemp` && \curl -sSL https://raw.githubusercontent.com/autolab/Autolab/master/bin/setup.sh
```

Next, run 

```
$ vim $AUTOLAB_SCRIPT
```

Comment out the lines between After line 104, insert the following line

```
$ bash $AUTOLAB_SCRIPT
```

After the successful installation of Autolab, you will receive the following messages:

```
Autolab installation is now complete. When you start a new login-shell, you may run the following command to start up Autolab server at Port 3000:
                         cd ~/Autolab && bundle exec rails s -p 3000 --binding=0.0.0.0

Top things to do after installation:

- Try out Tango (https://github.com/autolab/Tango), the back-end service for Autolab, and fill in relevant parameters in ./config/autogradeConfig.rb
- Sign up for our mailing list to learn about new features and bug fixes: http://eepurl.com/bTTOiT
- Change MySQL root password (the password we generated is not strong enough for serious use.)
- Change MySQL password for `lngo`, and update it in ./config/database.yml (default password is '<password>')
- Contact us if you have any questions!

Thank you for trying out Autolab! For questions and comments, email us at autolab-dev@andrew.cmu.edu.

As a final reminder, your MySQL root password is: OTE4YjcwZjQ2MTA3YjU2Y2UyNTdlMTE5.
```

Let's hold off on starting Autolab until a bit later. 


### Installing Tango


Install and run [Redis](https://redis.io/topics/quickstart):

```
$ cd ~
$ wget http://download.redis.io/redis-stable.tar.gz
$ tar xvzf redis-stable.tar.gz
$ cd redis-stable
$ make
$ sudo aptitude install tcl tk
$ make test
$ sudo make install
$ redis-server --daemonize yes
```

Install and run [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)

```
$ sudo aptitude install -y apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt-get update
$ sudo apt-get install -y docker-ce
$ sudo usermod -aG docker $USER
```
At this point, log out and log backin to enable group modification so that the user account can runs docker (See
[Linux Postintallation](https://docs.docker.com/install/linux/linux-postinstall/). 

Next, we clone Tango and create the default configuration file. 

```
$ git clone https://github.com/autolab/Tango.git
$ cd Tango
$ cp config.template.py config.py
$ mkdir courselabs
```

We will use Docker to build a default autograder VM for Tango: 

```
$ cd path/to/Tango
$ docker build -t autograding_image vmms/
$ docker images autograding_image    # Check if image built
```

Confirm that the `VMMS_NAME` option in `config.py` is set to `localDocker` as follows:

```{python}
# in config.py
VMMS_NAME = "localDocker"
```

Next, we setup the Python virtual environment for Tango.

```
$ sudo aptitude install virtualenv
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ mkdir volumes
```

Run the following command to start the server (producer). If no port is given, the server will run on the port specified in config.py (default: 3000):

```
$ python restful-tango/server.py <port>
```
Open another terminal window and start the job manager (consumer):


```
$ cd Tango
$ source bin/activate
$ python jobManager.py
```

In yet another terminal, you can test that Tango is running:

```
$ curl localhost:<port>
# Hello, world! RESTful Tango here!
```

#### Running Autolab. 

Now you can configure Autolab to use Tango. Go to your Autolab directory and enter the following commands:

```
$ cp config/autogradeConfig.rb.template config/autogradeConfig.rb
``` 

You can edit the `autogradeConfig.rb` file so that it points to your Tango deployment. In this case, 
we are hosting Tango in the same location as the Autolab web server. 

```
# Hostname for Tango RESTful API
RESTFUL_HOST = "localhost"

# Port for Tango RESTful API
RESTFUL_PORT = "2000"

# Key for Tango RESTful API
RESTFUL_KEY = "test"
```

Now you can start Autolab:

```
$ cd ~/Autolab && bundle exec rails s -p 3000 --binding=0.0.0.0
```

If your host machine has a public IP address, you can open a browser and visit <IP address>:3000. Otherwise, you can open an internal browser on your machine and visit `localhost:3000`. The login and password are admin@foo.bar and *adminfoobar*. 