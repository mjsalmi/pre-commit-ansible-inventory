from setuptools import setup

setup(
    name="pre_commit_ansible-inventory",
    url="https://github.com/mjsalmi/pre-commit-ansible-inventory",
    author="Mikko Salmi",
    author_email="43180721+mjsalmi@users.noreply.github.com",
    version=open("VERSION", "r").read().strip(),
    install_requires=["ansible"],
    license="MIT",
    packages=["pre_commit_hooks"],
    entry_points={
        "console_scripts": [
            "ansible-inventory-wrapper = pre_commit_hooks.ansible_inventory_wrapper:main",
        ]
    },
)
