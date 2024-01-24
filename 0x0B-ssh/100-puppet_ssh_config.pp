#!/usr/bin/env bash
# client SSH configuration file using puppet
file { '/home/ubuntu':
  ensure  => directory,
  mode    => '0755',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/home/ubuntu/.ssh':
  ensure  => directory,
  mode    => '0700',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => @(SSHCONFIG)
    Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  SSHCONFIG
  ,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
