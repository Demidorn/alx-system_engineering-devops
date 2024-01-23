#!/usr/bin/env bash
# client SSH configuration file using puppet
file { '/home/ubuntu/.ssh/config':
ensure  => present,
mode	=> '0600',
content => @("SSHCONFIG"
Host *
IdentifyFile ~/.ssh/school
PasswordAuthentication no
SSHCONFIG
),
owner	=> 'ubuntu',
group	=> 'ubuntu',
}
