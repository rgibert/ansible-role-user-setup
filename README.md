# User Setup

Ansible role to handle common user / group setup

[![Build Status](https://travis-ci.org/rgibert/ansible-role-user-setup.svg?branch=master)](https://travis-ci.org/rgibert/ansible-role-user-setup)
[![GitHub issues](https://img.shields.io/github/issues/rgibert/ansible-role-user-setup.svg)](https://github.com/rgibert/ansible-role-user-setup/issues)
[![GitHub forks](https://img.shields.io/github/forks/rgibert/ansible-role-user-setup.svg)](https://github.com/rgibert/ansible-role-user-setup/network)
[![GitHub stars](https://img.shields.io/github/stars/rgibert/ansible-role-user-setup.svg)](https://github.com/rgibert/ansible-role-user-setup/stargazers)
[![GitHub license](https://img.shields.io/github/license/rgibert/ansible-role-user-setup.svg)](https://github.com/rgibert/ansible-role-user-setup/blob/master/LICENSE)

## Requirements

- none

## Role Variables

| Variable | Default | Definition |
|----------|---------|------------|
| user_setup_group | | Default group for user |
| user_setup_home | /home/{{ user_setup_username }} | Home directory for user |
| user_setup_shell | /bin/sh | Shell for user |
| user_setup_username | | User to be created |

## Dependencies

- none

## Example Playbook

```
- hosts:
    - servers
  roles:
    - role: rgibert.user-setup
      user_setup_group: users
      user_setup_username: user0
```

## License

GPL-3

## Author Information

Richard Gibert
richard@gibert.ca
