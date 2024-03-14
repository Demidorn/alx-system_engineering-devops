# 0x1A. Application server
DevOps  SysAdmin

### Resources
*Read or watch:*
- [Application server vs web server](https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA) <br>(As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- [Be careful with the way Flask manages slash](https://intranet.alxswe.com/rltoken/zTCSTQxrH2za4hxbkt8K3g) in [route](https://intranet.alxswe.com/rltoken/n5A0nmah-Si78zbNvdb4GA) - strict_slashes
- [Upstart documentation](https://intranet.alxswe.com/rltoken/cldrneY3Qr7LlDysygzRHw)

### Requirements
*General*
< - A README.md file, at the root of the folder of the project, is mandatory
> - Everything Python-related must be done using python3
> - All config files must have comments

> *Bash Scripts*
> - All your files will be interpreted on Ubuntu 16.04 LTS
> - All your files should end with a new line
> - All your Bash script files must be executable
> - Your Bash script must pass Shellcheck (version 0.3.7-<br>5~ubuntu16.04.1 via apt-get) without any error
> - The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
> - The second line of all your Bash scripts should be a comment <br>explaining what is the script doing

## TASKAS
> - 0. Set up development with Python
> - 1. Set up production with Gunicorn
> - 2. Serve a page with Nginx
> - 3. Add a route with query parameters
> - 4. Let's do this for your API
> - 5. Serve your AirBnB clone
> - 6. Deploy it!
> - 7. No service interruption
