<<<<<<< HEAD
# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
=======
# Enable user holberton to login and open files without error

# Increase hard limit for Holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "s/^holberton hard nofile.*/holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
}

# Increase soft limit for Holberton user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "s/^holberton soft nofile.*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
>>>>>>> a84df4dc2007b5dc01088062fca5d65e66ac4e3a
}
