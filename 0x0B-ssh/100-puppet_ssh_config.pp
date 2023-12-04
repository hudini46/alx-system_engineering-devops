package { 'augeas-tools':
  ensure => installed,
}

augeas { 'SSH configuration':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
    'set IdentityFile ~/.ssh/school',
  ],
}
