# increase the amount of traffic an Nginx can handle
exec  { 'fix--for-nginx':
	#modify the ULIMIT value
	command	=> "sed -i 's/15/4096/g' /etc/default/nginx && service nginx restart",
	path	=> ['/bin', '/usr/bin', '/usr/sbin']
}
