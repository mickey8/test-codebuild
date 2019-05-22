#!/usr/bin/bash

cd /opt/ansible
ansible-playbook site.yml -i hosts --connection=local --tags application-stop
