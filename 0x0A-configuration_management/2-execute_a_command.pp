# kills a proccesss named killmenow
exec { 'killmenow':
command     => '/usr/bin/pkill -f killmenow',
refreshonly => true,
logoutput   => true,
}
