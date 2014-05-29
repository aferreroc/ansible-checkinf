Ansible playbook to test multicast with iperf and open-mtools

Usage with iperf:
ansible-playbook -i hosts iperf_deploy_imas_a.yml
ansible-playbook -i hosts iperf_test_imas_a.yml --extra-vars 200b
ansible-playbook -i hosts iperf_undeploy_imas_a.yml


Usage with iperf:
ansible-playbook -i hosts mtools_deploy_imas_a.yml
ansible-playbook -i hosts mtools_test_imas_a.yml
ansible-playbook -i hosts mtools_undeploy_imas_a.yml
