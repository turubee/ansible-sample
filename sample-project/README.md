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

Bootstrapping
---
```
$ ansible-playbook -i inventories/prod/ec2.py playbooks/aws.yml --diff
```

Configuration
---
```
$ ansible-playbook -i inventories/prod/ec2.py playbooks/web.yml --diff
```

Orchestration
---
```
$ ansible-playbook -i inventories/prod/ec2.py playbooks/deploy.yml --diff
```

How to Destroy
---
```
$ aws elb delete-load-balancer --load-balancer-name web-elb
$ aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances --filter "Name=tag:Role,Values=web" | jq -r '.Reservations[].Instances[].InstanceId' | xargs)
```
** Deleting vpc is dangerous, so do it with the AWS console **
