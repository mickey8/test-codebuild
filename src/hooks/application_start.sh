#!/usr/bin/bash

cd /opt/ansible
ansible-playbook site.yml -i hosts -c local --tags application-start
