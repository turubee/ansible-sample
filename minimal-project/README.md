requirements
---
```
$ cd dcube-ansible
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ansible --version
ansible 2.2.1.0
```

vagrant
---
```
$ vagrant up
```

playbook
---
```
$ ansible-playbook -i hosts site.yml --diff
```
