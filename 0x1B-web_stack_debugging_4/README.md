# 0x1B. Web stack debugging #4
DevOps  SysAdmin  Scripting  Debugging
<<<<<<< HEAD

## Requirements
###General
> - All your files will be interpreted on Ubuntu 14.04 LTS
> - All your files should end with a new line
> - __A README.md__ file at the root of the folder of the project<br> is mandatory
> - Your Puppet manifests must pass puppet-lint version <br>2.1.1 without any errors
> - Your Puppet manifests must run without error
> - Your Puppet manifests first line must be a comment <br>explaining what the Puppet manifest is about
> - Your Puppet manifests files must end with the extension .pp
> - Files will be checked with Puppet v3.4

## SERVICES
- Install puppet-lint if not installed
``` bash $ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
- Install Apache Benchmark command-line tool
	``` sudo apt-get update
	     sudo apt-get install apache2-utils
	```

- Make sure your nginx is running .
 - Check Nginx status 
	``` service ngix status```
 - Run nginx service
	```service nginx start```
 - If not installed, install Nginx
	``` sudo apt-get update
	     sudo apt-get install nginx
	```
- Confirm that server is running on port 80
	``` sudo lsof -i :80``` using lsof command
		or
	```sudo netstat -tulpn | grep :80``` using netstat command
	```sudo ss -tulpn | grep :80``` using ss command


### Tasks
0. Sky is the limit, let's bring that limit higher.
1. User limit

=======
---
## Requirements
*General*
> - All your files will be interpreted on Ubuntu 14.04 LTS
> - All your files should end with a new line
> - __A README.md__ file at the root of the folder of the project is mandatory
> - Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
> - Your Puppet manifests must run without error
> - Your Puppet manifests first line must be a comment explaining <br>what the Puppet manifest is about
> - Your Puppet manifests files must end with the extension .pp
> - Files will be checked with Puppet v3.4
----
### Install puppet-lint
> ``` bash $ apt-get install -y ruby
> $ gem install puppet-lint -v 2.1.1
> ```

**Tasks**
0. Sky is the limit, let's bring that limit higher
1. User limit
>>>>>>> a84df4dc2007b5dc01088062fca5d65e66ac4e3a
