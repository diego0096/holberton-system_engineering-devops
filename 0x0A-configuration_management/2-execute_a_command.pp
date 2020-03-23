# Puppet script to kill a process
exec {'killmenow':
  command => '/usr/bin/pkill --full killmenow'
}
