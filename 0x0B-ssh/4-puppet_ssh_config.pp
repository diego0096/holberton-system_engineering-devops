#Puppet connect 
include stdlib

file_line { 'Create_identity_file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn_off_passwd_auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
