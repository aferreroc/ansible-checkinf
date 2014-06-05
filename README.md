Unix script in conjuntion with Ansible playbook to test multicast with iperf and open-mtools




Usage with iperf:
ansible-playbook -i hosts iperf_deploy_imas_a.yml
ansible-playbook -i hosts iperf_test_imas_a.yml --extra-vars "capacity=200m mydate=2014-06-05.12:22:31"
ansible-playbook -i hosts iperf_undeploy_imas_a.yml


Usage with mtools:
ansible-playbook -i hosts mtools_deploy_imas_a.yml
ansible-playbook -i hosts mtools_test_imas_a.yml --extra-vars "mydate=2014-06-05.12:22:31"
ansible-playbook -i hosts mtools_undeploy_imas_a.yml


Display counters:
ansible-playbook -i hosts counters.yml --extra-vars "iface=eth0 mydate=2014-06-05.12:22:31"

Display summary info of hardware:
ansible-playbook -i hosts hw.yml --extra-vars "iface=eth0 mydate=2014-06-05.12:22:31"


Or better with use of script:
./checkinf -h
