# increase the amount of traffic an Nginx can handle
exec  { 'fix--for-nginx':
	#modify the ULIMIT value
	command	=> '/bin/sed -i "s/15/4096/" /etc/default/nginx',
	path	=> '/usr/local/bin/:/bin/',
}

exec { 'nginx-restart':
	command	=> '/etc/init.d/nginx restart',
	path	=> '/etc/init.d/',
}	
