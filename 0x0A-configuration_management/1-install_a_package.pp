#  This puppet manifest install pupet-lint

package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
