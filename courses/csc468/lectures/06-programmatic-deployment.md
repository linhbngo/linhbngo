
# Programmatic Deployment of Infrastructures
 
```{admonition} 1. Find CloudLab profile for OpenStack
:class: dropdown

- Log into [CloudLab](https://www.cloudlab.us/)
- Under **Experiments** drop down box, select **Start Experiment**.

![Start Experiment](../fig/05-programmatic/01.png)

- Click **Change Profile**. 

![Change Profile](../fig/05-programmatic/02.png)

- Type **OpenStack** in the search box, and select the profile **OpenStack** 
as shown in the figure below. 
  - Created By: `johnsond`
  - Last Updated: `2017-12-20 10:05:21`
  - Click **Select Profile** when done. 

![OpenStack profile created by johnsond](../fig/05-programmatic/03.png)

- Click **Next**. 

![OpenStack select profile](../fig/05-programmatic/04.png)

- Select the options similar to the figure below. 
- If the **Parameterize** tab does not look like this, click **Previous** to 
go back one step, and then click **Next** again.

![Patameterization options](../fig/05-programmatic/05.png)

- Only **Utah**, **Wisconsin**, and **Clemson** have been known to work with this 
profile. 
- I will use **Utah** for the remaining steps. 

![Resource selections](../fig/05-programmatic/06.png)

- Do not change anything on the **Schedule** step and click **Finish**. 

![Provisioning resources](../fig/05-programmatic/07.png)

- The startup scripts of this profile will take sometimes to run, approximately 
**thirty minutes to one hour**. 
- You will receive an email from CloudLab (to the registered) to inform you when 
the experiment is ready. 

![Waiting for email confirmations](../fig/05-programmatic/08.png)

- Go to the experiment, and open the blue *Profile Instructions** box. 

![Profile Instructions](../fig/05-programmatic/09.png)

- Follow the instructions to login to OpenStack dashboard. Your passwords 
will be randomly generated and unique to each experiment. 

![Domain, User Name, Password](../fig/05-programmatic/10.png)

- You will see a Dashboard on a successful deployment as follows.

![Administrative Dashboard](../fig/05-programmatic/11.png)

```

```{admonition} 2. Deploying compute resources from OpenStack    
:class: dropdown

- In the next sequence of hands-on, we will look at how OpenStack can 
support the deployment of a virtual machine inside its Nova compute 
components. 

```

```{admonition} 3. Hands-on: Download Linux distribution
:class: dropdown

- We will use Alpine Linux, a light-weight distribution that was created
for containerization/cloud deployment. 
- From [Alpine Download Page](https://alpinelinux.org/downloads/), select the 
x86_64 Virtual version. 

![Select correct x86_64 download](../fig/05-programmatic/12.png)

```

```{admonition} 4. Hands-on: Create cloud image
:class: dropdown

- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Images**, then click on **Create Image**.  

![List of compute images](../fig/05-programmatic/13.png)

- Click **Browse** and find and select the downloaded ISO file from the
the previous slide. 
- Set the other parameters as shown in the figure below. 
- Click **Create Image** when done. 

![Create image](../fig/05-programmatic/14.png)

- The image will show up in the **Images** tab. 

![Newly added image](../fig/05-programmatic/15.png)

```

```{admonition} 5. Hands-on: Create volumes
:class: dropdown

- Go to your CloudLab Dashboard. 
- Go to **Volumes**/**Volumes**, then click on **Create Volume**.  

![Create Volumes](../fig/05-programmatic/16.png)

- Set the other parameters as shown in the figure below. 
- Alpine takes up a small amount of storage, so 2GB is more than enough 
for a simple installation.
- Click **Create Volume** when done. 

![Options to create a new volume](../fig/05-programmatic/17.png)

- The volume will show up in the **Volumes** tab. 

![New volume is added](../fig/05-programmatic/18.png)

```

```{admonition} 6. Hands-on: Launching a compute instance
:class: dropdown

- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances** and click on **Launch Instance**.  

![Create Instances](../fig/05-programmatic/19.png)

- Set the instance name and other parameters, then click **Next**

![Selecting source with instance](../fig/05-programmatic/20.png)

- Use the up arrow to select the **alpine** image as the allocated image. 
Click **Next**. 

![Selecting image to boot from](../fig/05-programmatic/21.png)

- Select **m1.tiny** as the compute flavor. Click **Next**. 

![Selecting compute resource](../fig/05-programmatic/22.png)

- Select **flat-lan-1-net** as the connected network. Click **Launch Instance**. 

![Selecting network resource](../fig/05-programmatic/23.png)

- It should take a few minute for the instance to become ready. 

![Active compute resource](../fig/05-programmatic/24.png)

```

```{admonition} 7. Hands-on: Volume attachment and Linux installation
:class: dropdown

- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance, 
then click **Attach Volume**.  

![Attach volume actions](../fig/05-programmatic/25.png)

- Select your `sda_****` volume ID created earlier, then click **Attach Volume**

![Attach volume](../fig/05-programmatic/26.png)

- Click on the drop-down arrow under **Actions** for the alpine instance. 
- Select **Console**.

![Provisioning resources](../fig/05-programmatic/27.png)

- Right click on **Click here to show only console** and select 
**Open link in new tab**.
- This helps with navigating back and forth.  

![Launch a console](../fig/05-programmatic/28.png)

- A new console tab appears! 
- You are now booting from the Alpine distro. 

![Login to the instance](../fig/05-programmatic/29.png)

- Type **root** into the`localhost login:` prompt and hit Enter to log in. 

![Logged into the system as root](../fig/05-programmatic/30.png)

- A quick review of Alpine installation process can be found 
on [their wiki](https://wiki.alpinelinux.org/wiki/Install_to_disk)
- Type `setup-alpine` and hit Enter to start the installation process. 
- Use the following options:
  - `Select keyboard layout`: `us`
  - `Select variant`: `us`
  - `Enter system hostname ...`: Hit Enter to accept default. 
  - `Which one do you want to initialize?`: Hit Enter to accept `eth0` as the default interface. 
  - `Ip address for eth0`: Hit Enter to accept `dhcp` as the default value. 
  - `Do you want to do any manual network configuration?`: Hit Enter to accept `n` as the default value. 
  - Enter a **complex** password for root. DO NOT MAKE AN EASY PASSWORD. If your cloud instance got 
  hacked and used for malicious purposes, you will be banned from CloudLab. Retype the password. 
  - `Which timezone are you in?`: Type `EST` and hit Enter. 
  - `HTTP/FTP proxy URL?`: Hit Enter to accept `none` as the default value. 
  - For the mirror question, type `30` (the one from princeton), then hit Enter. 
  - `Which SSH server?`: Hit Enter to accept `openssh` as the default value. 
  - `Which disk(s) would you like to use?`: Review the lines above, and select the listed disk. 
  There should be one as we already attached a volume to this instance. For me, it is `vdb`, so I 
  type in `vda` and hit Enter. 
  - `How would you like to use it?`: Type `sys` and hit Enter. 
  - `WARNING: Erase the above disk(s) and continue?`: Type `y` and hit Enter. 

![Finish setting up different options](../fig/05-programmatic/31.png)

- Once the installation process is completed, Leave this console running and return to the Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance.  
- Select the `sda_****` volume ID selected earlier, then click **Detach Volume**

![Option to detach volume](../fig/05-programmatic/32.png)

- Select the `sda_****` volume ID created earlier, then click **Detach Volume**

![Detaching for volumes](../fig/05-programmatic/33.png)

- Go to your CloudLab Dashboard. 
- Go to **Volumes**/**Volumes**.  
- In the **Actions** box of `sda_****`, click the drop-down arrow and select **Upload to Image**. 

![Volume options](../fig/05-programmatic/34.png)

- Set **Image Name** to `alpine-disk` and **Disk Format** as `Raw`, then click 
**Upload**. 

![Upload volumes to image](../fig/05-programmatic/35.png)

- Successful upload:

![Image appeared in list](../fig/05-programmatic/36.png)


```

```{admonition} 8. Challenge
:class: dropdown

- Launch another compute instance using the newly created `alpine-disk` image. 
  - Pay attention to the flavor. 
- Log into the console and confirm that you can use the root password created earlier to log in

![New launched instance with working image]](../fig/05-programmatic/37.png)

```


```{admonition} 9. Setup Apache webserver (from the volume-based Alpine from Challenge 8)
:class: dropdown

- You should be inside the console after log in as root and have the root password. 
- Run the following commands to install Apache webserver

~~~
$ apk update
$ apk add apache2
$ rc-service apache2 start
~~~

![Update and install apache2](../fig/05-programmatic/38.png)

```


```{admonition} 10. Setup public IP address
:class: dropdown

- To expose the webserver, we need a public IP address. 
- Go to your CloudLab Dashboard. 
- Go to **Compute**/**Instances**
- Click on the drop-down arrow under **Actions** for the alpine instance, 
then click **Associate Floating IP**. 

![Associating floating IPs](../fig/05-programmatic/39.png)

- Click on the `+` sign to allocate IP address. 

![Allocating public IP addresses](../fig/05-programmatic/40.png)

- Click on **Allocate IP**. 

![Associate public IP address with the running instance](../fig/05-programmatic/41.png)

- Click on **Associate**.

![Associating IP to instance](../fig/05-programmatic/42.png)

- You should see the public IP address with your instance

![IP address on instance](../fig/05-programmatic/43.png)

- Try visiting this IP address now, anything?

```


```{admonition} 11. Cloud security basic
:class: dropdown

- In the cloud, `egress` means traffic that’s leaving from inside the private network out to the 
public internet (similar to standard network definition).

![Egress traffic generated from inside the cloud](../fig/05-programmatic/44.png)

- In the cloud, `ingress` refers to unsolicited traffic sent from an address in public internet to 
the private network – it is not a response to a request initiated by an inside system. In this case, 
firewalls are designed to decline this request unless there are specific policy and configuration that 
allows ingress connections.

![Ingress traffic generated from inside the cloud](../fig/05-programmatic/45.png)

```


```{admonition} 12. Handle security
:class: dropdown

- Go to your CloudLab Dashboard. 
- Go to **Network**/**Security Group**
- Click on **Manage Rules**. 

![Security groups](../fig/05-programmatic/46.png)

- Click `Add Rules` 

![Security group rule lists](../fig/05-programmatic/47.png)

- In the `Rule` drop down box, select `HTTP`, then click `Add`. 

![HTTP port](../fig/05-programmatic/48.png)

- You can see the new `Ingress` rule for HTTP.

![Security rules for HTTP is added](../fig/05-programmatic/49.png)

- The apache webserver is now visible

![Apache2 webserver](../fig/05-programmatic/50.png)

```


