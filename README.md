requirements
---
```
$ cd dcube-ansible
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ansible --version
ansible 2.2.0.0
```

bootstrapping
---
```
$ ansible-playbook -i inventories/prod/hosts aws.yml --diff --check
```

configuration management
---
```
$ ansible-playbook -i inventories/prod/hosts web.yml --private-key ~/.ssh/dcube-prod.pem --diff --check
```
