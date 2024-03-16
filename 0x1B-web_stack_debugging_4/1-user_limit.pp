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
}
