#  This puppet manifest kill a process named killmenow

exec { 'kill_process':
  command => 'pkill -x killmenow',
  path    => '/usr/bin',
}
