requirements
---
```
$ cd ansible-sample
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ansible --version
ansible 2.2.1.0
```

prepare
---
```
$ echo "password" >vault_passwd
$ mkdir ~/.aws
$ cat <<EOL >>~/.aws/credentials
[dcube-prod]
aws_access_key_id = [AWS_ACCESS_KEY]
aws_secret_access_key = [AWS_SECRET_ACCESS_KEY]
region = ap-northeast-1
```

Bootstrapping
---
```
$ AWS_PROFILE=dcube-prod ansible-playbook -i inventories/prod/ec2.py playbooks/aws.yml --diff
```

Configuration
---
```
$ AWS_PROFILE=dcube-prod ansible-playbook -i inventories/prod/ec2.py playbooks/web.yml --diff
```

Orchestration
---
```
$ AWS_PROFILE=dcube-prod ansible-playbook -i inventories/prod/ec2.py playbooks/deploy.yml --diff
```

How to Destroy
---
```
$ export AWS_DEFAULT_PROFILE=dcube-prod
$ aws elb delete-load-balancer --load-balancer-name web-elb
$ aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances --filter "Name=tag:Role,Values=web" | jq -r '.Reservations[].Instances[].InstanceId' | xargs)
$ aws ec2 delete-key-pair --key-name dcube-prod
```
** Deleting vpc is dangerous, so do it with the AWS console **
