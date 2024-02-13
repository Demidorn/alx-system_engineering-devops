# Firewall
DevOps  SysAdmin  Security

## **Warning!**
Containers on demand cannot be used for this project <br>(Docker container limitation)
Be very careful with firewall rules! For instance, if you <br>ever deny port 22/TCP and log out of your server, you>br> will not be able to reconnect to your server via SSH, <br>and we will not be able to recover it. When you install UFW, <br>port 22 is blocked by default, so you should unblock it immediately before logging out of <br>your server.

## Tasks
***0. Block all incoming traffic but***
Let’s install the ufw firewall and setup a few rules on web-01.
> Requirements:
> - The requirements below must be applied to web-01 <br>(feel free to do it on lb-01 and web-02, but it won’t be<br> checked)
> - Configure ufw so that it blocks all incoming traffic, <br>except the following TCP ports:
>> - 22 (SSH)
>> - 443 (HTTPS SSL)
>> - 80 (HTTP)
> - Share the ufw commands that you used in your answer file

**1. Port forwarding**
Firewalls can not only filter requests, they can also forward them.
> ***Requirements:***
> - Configure web-01 so that its firewall redirects port <br>8080/TCP to port 80/TCP.
> - Your answer file should be a copy of the ufw configuration <br>file that you modified to make this happen
> Terminal in web-01:
