# 0x0B. SSH
DevOps  SSH  Network  SysAdmin  Security
---
# Requirements
## General
- Allowed editors: __vi__, __vim__, __emacs___
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A **README.md** file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly ```bash #!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing

---

TASKS
1. Write a Bash script that uses ssh to connect to your server using the<br> private key ``` bash ~/.ssh/school``` with the user ubuntu.
### Requirements:
- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase

2. Write a Bash script that creates an RSA key pair.

### Requirements:
- Name of the created private key must be school
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty

3. Your machine has an SSH configuration file for the local SSH client, <br>let’s configure it to our needs so that you can connect to a server without typing a <br>password. Share your SSH client configuration in your answer file.
### Requirements:
- Your SSH client configuration must be configured to use the private key ```bash ~/.ssh/school```
- Your SSH client configuration must be configured to refuse to authenticate using a password

4. Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the __ubuntu__ user.

5. Let’s practice using Puppet to make changes to our configuration file. Just as<br> in the previous configuration file task, we’d like you to set up your client SSH <br>configuration file so that you can connect to a server without typing a password.
### Requirements:
- Your SSH client configuration must be configured to use the private key ```bash ~/.ssh/school```
- Your ***SSH*** client configuration must be configured to refuse to authenticate using a password
