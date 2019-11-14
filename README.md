# User Setup

![Ansible Role](https://img.shields.io/ansible/role/34486?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-user-setup?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/34486?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/34486?label=downloads&style=flat-square)

## Description

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

```yaml
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
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
