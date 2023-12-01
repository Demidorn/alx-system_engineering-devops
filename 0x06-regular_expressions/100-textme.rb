#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([a-aA-Z0-9+]+)\]\s\[to:([a-zA-Z0-9+]+)\]\s\[flags:([a-zA-Z0-9:-]+)/).join(',')
