import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    assert host.user('testuser0').exists


def test_group(host):
    assert host.group('testgroup0').exists
