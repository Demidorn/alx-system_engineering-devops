# installs flask package from pip3
package { 'pip3':
ensure   => '3..8.10',
}

package { 'flask':
ensure   => '2.1.0',
provider => 'pip3',
}

package { 'Werkzeug':
ensure   => '2.1.1',
provider => 'pip3',
}
