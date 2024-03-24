# Puppet manifest to modify the default SSH configuration file to include an additional identity file
# and disable password authentication.

# Include the standard library module
include stdlib

# Modify the SSH configuration to include the new identity file (~/.ssh/school)
file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => 'IdentityFile ~/.ssh/school',  # New identity file to be added
  match              => '^\s*IdentityFile\s+~/.ssh/id_rsa$',  # Regular expression to match existing identity file line
  replace            => true,
  append_on_no_match => true
}

# Modify the SSH configuration to disable password authentication
file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => 'PasswordAuthentication no',  # Disable password authentication
  match              => '^\s*PasswordAuthentication\s+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}
