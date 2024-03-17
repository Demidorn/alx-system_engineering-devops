<<<<<<< HEAD
# fix nginx to accept and serve more requests

exec {'modify max open files limit setting':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
=======
# increase the amount of traffic an Nginx can handle
exec  { 'fix--for-nginx':
	#modify the ULIMIT value
	command	=> "sed -i 's/15/1000/' /etc/default/nginx && service nginx restart",
	path	=> ['/bin', '/usr/bin', '/usr/sbin']
>>>>>>> a84df4dc2007b5dc01088062fca5d65e66ac4e3a
}
