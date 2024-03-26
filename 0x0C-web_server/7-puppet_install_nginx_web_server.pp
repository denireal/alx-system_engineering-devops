# Puppet manifest to update the system, install Nginx, create a "Hello World!" HTML file,
# add a redirect configuration to the Nginx configuration file, and ensure the Nginx service is running.

# Update the system
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Create a "Hello World!" HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Add a redirect configuration to the Nginx configuration file
exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',  # Use shell provider for executing commands
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],  # Require Nginx package to be installed before starting the service
}
