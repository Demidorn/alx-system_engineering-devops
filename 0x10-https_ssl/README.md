# 0x10. HTTPS SSL
DevOps  SysAdmin  Security

### Concepts
For this project, we expect you to look at these concepts:
- [DNS](https://intranet.alxswe.com/concepts/12)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

## Requirements
> ### General
> - Allowed editors: vi, vim, emacs
> - All your files will be interpreted on Ubuntu 16.04 LTS
> - All your files should end with a new line
> - A README.md file, at the root of the folder of the project, is mandatory
> - All your Bash script files must be executable
> - Your Bash script must pass Shellcheck (version 0.3.7) without any error
> - The first line of all your Bash scripts should be exactly ```bash <br>#!/usr/bin/env bash```
> - The second line of all your Bash scripts should be a comment explaining > - what is the script doing

## Tasks
**0. World wide web**

Configure your domain zone so that the subdomain www points to your <br>load-balancer IP (lb-01). Let’s also add other subdomains to make our life <br>easier, and write a Bash script that will display information about subdomains.
**Requirements:**
- Add the subdomain www to your domain, point it to your lb-01 IP <br>(your domain name might be configured with default subdomains, <br>feel free to<br> remove them)
- Add the subdomain lb-01 to your domain, point it to your lb-01 IP
- Add the subdomain web-01 to your domain, point it to your web-01 IP
- Add the subdomain web-02 to your domain, point it to your web-02 IP
- Your Bash script must accept 2 arguments:
1. domain:
	- type: string
	- what: domain name to audit
	- mandatory: yes
2. subdomain:
	- type: string
	- what: specific subdomain to audit
	- mandatory: no
- Output: __The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and<br> points to [DESTINATION]__
- When only the parameter domain is provided, display information for its<br> subdomains www, lb-01, web-01 and web-02 - <br>in this specific order
- When passing domain and subdomain parameters, display information<br> for the specified subdomain
- Ignore shellcheck case SC2086
- Must use:
	- awk
	- at least one Bash function
- You do not need to handle edge cases such as:
	- Empty parameters
	- Nonexistent domain names
	- Nonexistent subdomains

**1. HAproxy SSL termination**
“Terminating SSL on HAproxy” means that HAproxy is configured to handle<br> encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept <br>encrypted traffic for your subdomain www..
**Requirements:**
- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the / of your web server
- When querying the root of your domain name, the page returned<br>must contain Holberton School
- Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 1-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.

**2. No loophole in your website traffic**
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
**Requirements:**
- This should be transparent to the user
- HAproxy should return a 301
- HAproxy should redirect HTTP traffic to HTTPS
- Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 100-redirect_http_to_https must be your HAproxy configuration file
Prepared by:[Demidorn](https://github.com/Demidorn/alx-system_engineering-devops/tree/master/0x10-https_ssl)
