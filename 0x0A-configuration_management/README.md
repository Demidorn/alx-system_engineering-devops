# 0x0A. Configuration management
DevOps  SysAdmin  Scripting  CI/CD

---
## Requirements
### General
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp
---
### Note on Versioning
> - Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install puppet
> ```bash $ apt-get install -y ruby=1:2.7+1 --allow-downgrades
> $ apt-get install -y ruby-augeas
> $ apt-get install -y ruby-shadow
> $ apt-get install -y puppet
>```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://intranet.alxswe.com/rltoken/fsIr2xFkJHTkaXwqZFFcbA)

## Install __puppet-lint__
> $ gem install puppet-lint

## Tasks

|----------------- |--------------------------- | --------------------------------|
|Create a file |Using Puppet, create a file in __/tmp.__ |Requirements:<br>File path is /tmp/school<br>File permission is 0744<br><br>File owner is www-data<br>File group is www-data<br>
File contains I love Puppet|
|Install a package |Using Puppet, install __flask__ from __pip3.__ |Requirements:<br>Install __flask__<br>
Version must be 2.1.0 |
|Execute a command |Using Puppet, create a manifest that kills a<br> process named __killmenow__ |Requirements:<br> Must use the __exec__ Puppet resource<br>Must use pkill |
|--------------- |---------------------- |--------------------- |

---
### Example: 1

> ```bash root@6712bef7a528:~# puppet-lint --version
> puppet-lint 2.5.2
> root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
> root@6712bef7a528:~# 
> root@6712bef7a528:~# puppet apply 0-create_a_file.pp
> Notice: Compiled catalog for 6712bef7a528.ec2.internal in > environment production in 0.04 seconds
> Notice: /Stage[main]/Main/File[school]/ensure: defined content as > '{md5}f1b70c2a42a98d82224986a612400db9'
> Notice: Finished catalog run in 0.03 seconds
> root@6712bef7a528:~#
> root@6712bef7a528:~# ls -l /tmp/school
> -rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
> root@6712bef7a528:~# cat /tmp/school
>I love Puppetroot@6712bef7a528:~#
> ```


### Example: 2
> ```bash root@9665f0a47391:/# puppet apply 1-install_a_package.pp
> Notice: Compiled catalog for 9665f0a47391 in environment > production in 0.14 seconds
> Notice: /Stage[main]/Main/Package[Flask]/ensure: created
> Notice: Applied catalog in 0.20 seconds
> root@9665f0a47391:/# flask --version
> Python 3.8.10
> Flask 2.1.0
> Werkzeug 2.1.1
> ```


### Example: 3
### - Terminal #0 - starting my process

> root@d391259bf577:/# cat killmenow
> #!/bin/bash
> while [[ true ]]
> do
>    sleep 2
> done

> root@d391259bf577:/# ./killmenow

### - Terminal #1 - executing my manifest

> root@d391259bf577:/# puppet apply 2-execute_a_command.pp
> Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in > environment production in 0.01 seconds
> Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
> Notice: Finished catalog run in 0.10 seconds
> root@d391259bf577:/# 
### - Terminal #0 - process has been terminated

> root@d391259bf577:/# ./killmenow
> Terminated
> root@d391259bf577:/#
