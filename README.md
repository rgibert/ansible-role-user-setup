# User Setup

Ansible role to handle common user / group setup

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
    - { role: rgibert.user-setup, user_setup_group: users, user_setup_username: user0 }
```

License
-------

GPL-3

Author Information
------------------

Richard Gibert
richard@gibert.ca

