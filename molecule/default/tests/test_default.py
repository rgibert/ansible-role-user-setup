import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_shell_installed(host):
    assert host.package("git").installed
    assert host.package("zsh").installed


def test_user(host):
    assert host.user('testuser0').exists
    assert host.user('testuser1').exists


def test_group(host):
    assert host.group('testgroup0').exists
    assert host.group('testgroup1').exists


def test_dir_home_config(host):
    assert host.file('/home/testuser0/.config').is_directory
    assert host.file('/home/testuser1/.config').is_directory


def test_dir_home_local_bin(host):
    assert host.file('/home/testuser0/.local/bin').is_directory
    assert host.file('/home/testuser1/.local/bin').is_directory


def test_dir_home_local_lib(host):
    assert host.file('/home/testuser0/.local/lib').is_directory
    assert host.file('/home/testuser1/.local/lib').is_directory


def test_dir_home_local_share(host):
    assert host.file('/home/testuser0/.local/share').is_directory
    assert host.file('/home/testuser1/.local/share').is_directory


def test_file_home_config_aliases(host):
    assert host.file('/home/testuser0/.config/aliases').is_file
    assert host.file('/home/testuser1/.config/aliases').is_file


def test_file_home_config_vars(host):
    assert host.file('/home/testuser0/.config/vars').is_file
    assert host.file('/home/testuser1/.config/vars').is_file


def test_file_home_gitignore(host):
    assert host.file('/home/testuser0/.gitignore').is_file
    assert host.file('/home/testuser1/.gitignore').is_file


def test_file_usr_local_share_ohmyzsh(host):
    assert host.file('/usr/local/share/oh-my-zsh').is_directory
