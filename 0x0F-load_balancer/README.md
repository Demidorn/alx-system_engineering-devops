# 0x0F. Load balancer
DevOps  SysAdmin

## Concepts
For this project, we expect you to look at these concepts:
[Load balancer](https://intranet.alxswe.com/concepts/46)
[Web stack debugging](https://intranet.alxswe.com/concepts/68)
# Resources
### Read or watch:
[Introduction to load-balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
[HTTP header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
[Debian/Ubuntu HAProxy packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

## Requirements
### General
- Allowed editors: __vi__, __vim__, __emacs__
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A **README.md** file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass __Shellcheck__ (version **0.3.7**) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
### 0. Double the number of webservers
In this first task you need to configure __web-02__ to be identical to __web-01__. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure __web-02__. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

**Requirements:**

- Configure Nginx so that its HTTP response contains a custom header (on __web-01__ and __web-02__)
 - The name of the custom HTTP header must be __X-Served-By__
 - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write __0-custom_http_response_header__ so that it configures a brand new Ubuntu machine to the requirements asked in this task
__Ignore SC2154__ for __shellcheck__
If your server’s hostnames are not properly configured (__[STUDENT_ID]-web-01__ and __[STUDENT_ID]-web-02__.), follow this [tutorial](https://intranet.alxswe.com/rltoken/qSor8ulAHl4HedrO6KJEoQ).

### 1. Install your load balancer
Install and configure HAproxy on your lb-01 server.
**Requirements:**
- Configure HAproxy so that it send traffic to __web-01__ and __web-02__
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: __[STUDENT_ID]-web-01__ and __[STUDENT_ID]-web-02__. If not, follow this [tutorial](https://intranet.alxswe.com/rltoken/YkfzgEa6xNHrQbkKmJN4zg).
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

### 2. Add a custom HTTP header with Puppet
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

- The name of the custom HTTP header must be __X-Served-By__
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write __2-puppet_custom_http_response_header.pp__ so that it configures a brand new Ubuntu machine to the requirements asked in this task
