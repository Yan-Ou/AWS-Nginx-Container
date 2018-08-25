# Prerequisite
1. Python 2.7.x is installed.
2. Ansible 2.6.x is installed.
3. bot0, botocore and boto3 are installed. 
4. AWS account with necessary permissions. 
5. AWSAccessKey and AWSSecretKey ready for running the playbook.

# Playbook tasks:
- Create 1 x VPC (1 x public subnet, 1 x Internet gateway, and 1 public route table)
- Create 1 x Key pair
- Provision 1 x EC2 instance
- Firewall role
  - Install Firewalld
  - Enable Firewalld
  - Allow http service on port 80
- App role
  - Install pip
  - Install BeautifulSoup
  - Install docker
  - Copy web app source files (Dockerfile, default.conf, check.sh, health.sh, count.py) to EC2 instance
  - Build docker image and start up container
  - Execute check.sh to check container resource usage on every 10 seconds and export the result to ~/app/usage.txt
  - Execute health.sh to check nginx service status and export the result to ~/app/health.txt
  - Execute count.py to fetch default http page, count the most frequent word and export the result to ~/app/count.txt
  
 # How to run the playbook
 1. Issue the following command:
    ansible-playbook site.yml -i hosts
 2. After issuing the command, input your AWSAccessKey, AWSSecretKey and region name which you want to deploy to. Default region name is ap-southeast2 #Sydney.
  
 # File structure:
  - site.yml: contains all the tasks
  - hosts: contains all inventories
  - ansible.cfg: ansible configuration 
  - src/default.conf: nginx service configuration
  - src/check.sh: script to check cotainer resource usage on every 10 seconds 
  - src/health.sh: script to check nginx health status
  - src/count.py: script to fetch default http page and count the most frequent word
  - firewall: ansible role to install and configure firewall on EC2 instance
  - app: ansible role to deploy web app
  - aws: aws tasks to provision VPC, Keypair, and EC2
  
 # Count app:
 1. Implemented by Python with BeautifulSoup module.
 2. Use Beautifulsoup to scrap the default http page.
 3. Use regex to parse the http text.
 4. Use collections to count the most frequent word. 
  
