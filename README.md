# Ansible-inventory pre-commit hook

This hook runs `ansible-inventory` against files defined in pre-commit config. As ansible-inventory doesn't seem to return non-zero exit codes, output in stderr is treated as error.

## Requirements

* Pre-commit
* Python 3.6 or later
* Ansible (will be installed by the hook)

## Adding hook to your pre-commit config

```yaml
- repo: https://github.com/mjsalmi/pre-commit-ansible-inventory
  rev: v0.1.0
  hooks:
    - id: ansible-inventory
      files: inventory.yaml
```

## License

This software is licensed under the MIT license (see the `LICENSE` file).
