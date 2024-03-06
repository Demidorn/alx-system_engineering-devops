# Web stack debugging #3
DevOps  SysAdmin  Scripting  Debugging

## Requirements
> *General*
> - All your files will be interpreted on Ubuntu 14.04 LTS
> - All your files should end with a new line
> - A README.md file at the root of the folder of the project is<br> mandatory
> - Your Puppet manifests must pass puppet-lint version 2.1.1<br> without any errors
> - Your Puppet manifests must run without error
> - Your Puppet manifests first line must be a comment explaining<br> what the Puppet manifest is about
> - Your Puppet manifests files must end with the extension .pp
> - Files will be checked with Puppet v3.4

### To Install __puppet-lint__ run;
``` bash $ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## TASK
|--------- | ----------- | ---------- |
| *Task | *Description* | *Hint* |
|Strace is your friend | Using strace, find out why Apache is returning <br>a 500 error. Once you find the issue, fix it and then automate it using <br>Puppet (instead of using Bash as you were previously doing). | strace can attach to a current running process.<br>You can use tmux to run strace in one window and curl in another one.<br>Requirements:<br>Your 0-strace_is_your_friend.pp file must contain Puppet code<br>You can use whatever Puppet resource type you want for you fix |

### Example
``` { 
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~# }
```
