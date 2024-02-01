# 0x0E. Web stack debugging #1
DevOps  SysAdmin  Scripting  Debugging

### Concepts
For this project, we expect you to look at these concepts:

- [Network basics](https://intranet.alxswe.com/concepts/33)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)

## Requirements
### General
- Allowed editors: __vi__, __vim__, __emacs__
- All your files will be interpreted on Ubuntu **20.04 LTS**
- All your files should end with a new line
- A **README.md** file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass __Shellcheck__ without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly __#!/usr/bin/env bash__
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You are not allowed to use __wget__

## **Tasks**

Using your debugging skills, find out what’s keeping your Ubuntu container’s<br> Nginx installation from listening on port __80__. Feel free to install whatever tool you need,<br> start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum<br> number of commands to automate your fix.

**Requirements:**

- Nginx must be running, and listening on port __80__ of all the server’s active IPv4 IPs
- Write a Bash script that configures a server to the above requirements

1. Make it sweet and short

Using what you did for task #0, make your fix short and sweet.

**Requirements:**
- Your Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use __;__
- You cannot use __&&__
- You cannot use __wget__
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
- __service__ (init) must say that __nginx__ is not running ← for real
