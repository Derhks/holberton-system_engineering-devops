# This puppet manifest modify a file fixing the
# 500 Internal Server Error

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/bin',
}
