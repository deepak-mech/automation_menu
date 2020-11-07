import os

print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome in the Automation World....!! ")
os.system(" tput setaf 2 ")
print(" \t\t\t---------------------------------------------- ")

def menu():
	print("""

	\tPress 1	:	Create Key-Pairs\n    
	\tPress 2	:	Create Security Groups\n			
	\tPress 3	:	Launch EC2 Instances\n
	\tPress 4	:	Start EC2 Instances (Already Installed)\n
	\tPress 5	:	Describe EC2 Instances\n
	\tPress 6	:	Create EBS Volume\n
	\tPress 7	:	Attach EBS Volume to EC2 Instance\n
	\tPress 8	:	Create Partition  in EBS Volume\n
	\tPress 9	:	Format the Partition\n
	\tPress 10 :	Mount the Partition\n
	\tPress 11 :	Configure Web Server\n
	\tPress 12 :	Show Web Page\n
	\tPress 13 :      Create S3 Bucket\n
	\tPress 14 :      Upload file in S3 Bucket\n
	\tPress 15 :      Show Web Page having bucket file (High Latency)\n
	\tPress 16 :	Create CloudFront Distribution\n
	\tPress 17 :      Show Web Page having bucket file  (Low Latency)\n
	\tPress 18 :	Delete Bucket\n
	\tPress 19 :	Detach  Volume\n
	\tPress 20 :	Terminate Instance\n
	\tPress 21 :	Exit the Program\n

	""")

r = input("How do you want to run the program ? ( local or remote )  :    ")

print()

ip = input("Enter IP address where you want to remote login :  ")

while True:
	os.system(' clear ')
	menu()
	ch = input("\tEnter Your Choice  :  ")
	print()

	if int(ch) == 1:
		key_name = input(' Enter the name of key-pair :   ')
		os.system(' aws ec2 create-key-pair --key-name {} '.format(key_name))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
		print()

	elif int(ch) == 2:
		gp_name = input(' Enter name of security group :   ')
		dspr = input(' Give description for security group :   ')
		os.system( " aws ec2 create-security-group  --group-name  {}  --description {} ".format(gp_name, dspr))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
		print()

	elif int(ch) == 3:
		gp_id = input(' Enter security group ID :   ')
		os.system("  aws ec2 run-instances --image-id  ami-0e306788ff2473ccb  --instance-type  t2.micro --key-name  {}  --security-group-ids {} --subnet-id  subnet-c6767fae  --count  1 ".format(key_name, gp_id))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
		print()

	elif int(ch) == 4:
		inst_id = input(' Enter instance ID :   ')
		os.system(" aws ec2 start-instances --instance-ids {} ".format(inst_id))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
		print()

	elif int(ch) == 5:
		os.system(" aws ec2 describe-instances ")
		print()

	elif int(ch) == 6:
		os.system("aws ec2 create-volume   --volume-type gp2  --size 1  --availability-zone ap-south-1a")
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:volumeType")
		print()

	elif int(ch) == 7:
		vol_id = input(' Enter volume ID :   ')
		os.system(" aws  ec2  attach-volume --instance-id {}  --volume-id {}  --device /dev/xvdf ".format(inst_id, vol_id))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#InstanceDetails:instanceId=i-0ceac460b5aadae8f")
		print()

	elif int(ch) == 8:
		os.system(" ssh -i  {}.pem root@{} fdisk /dev/xvdf ".format(key_name, ip))
		os.system(' ssh -i  {}.pem root@{} lsblk '.format(key_name, ip))
		print()

	elif int(ch) == 9:
		os.system(" ssh -i  {}.pem root@{} mkfs.ext4 /dev/xvdf1 ".format(key_name, ip))
		print()

	elif int(ch) == 10:
		dir = input(' Create a directory to mount with partition :  ')
		os.system(' ssh -i  {}.pem root@{} mkdir  {} '.format(key_name, ip, dir))
		os.system(' ssh -i  {}.pem root@{} mount /dev/xvdf1  {} '.format(key_name, ip, dir))
		os.system(' ssh -i  {}.pem root@{} lsblk '.format(ip))

	elif int(ch) == 11:
		os.system(' ssh -i {}.pem root@{}  yum install httpd;systemctl start httpd;systemctl status httpd '.format(key_name, ip))
		web_page = input(' Enter the name of html file :   ')
		os.system(r' echo Hello Everybody, Deepak here  >> {} '.format(web_page))
		os.system(' scp -i {}.pem {} root@{}:/var/www/html '.format(key_name, web_page, ip))
		os.system('  ssh -i {}.pem root@{}  cd  /var/www/html; ls; cat {}; cd '.format(key_name, ip, web_page))
		os.system(' rm -rf {} '.format(web_page))
		print()

	elif int(ch) == 12:
		webbrowser.open('http://{}/{}'.format(ip, web_page))
		print()

	elif int(ch) == 13:
		bkt_name = input(' Enter the name of bucket :   ')
		os.system(" aws  s3api  create-bucket  --bucket {} --region us-east-1 ".format(bkt_name))
		webbrowser.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
		print()

	elif int(ch) == 14:
		os.system(" aws  s3  cp deepak_pic.png s3://my-bucket-87086/ --acl public-read-write ")
		webbrowser.open("https://s3.console.aws.amazon.com/s3/buckets/my-bucket-87086?region=us-east-1&tab=objects")
		print()

	elif int(ch) == 15:
		webbrowser.open('http://{}/{}'.format(ip, web_page))
		print()

	elif int(ch) == 16:
		os.system(" aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object deepak_pic.png ".format(bkt_name))
		webbrowser.open("https://console.aws.amazon.com/cloudfront/home?region=us-east-1#")
		print()

	elif int(ch) == 17:
		webbrowser.open('http://{}/{}'.format(ip, web_page))
		print()

	elif int(ch) == 18:
		os.system("aws s3api delete-bucket --bucket {} ".format(bkt_name))
		webbrowser.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
		print()

	elif int(ch) == 19:
		os.system(" aws ec2 detach-volume --volume-id {} ".format(vol_id))
		webbrowser.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#InstanceDetails:instanceId=i-0ceac460b5aadae8f")
		print()

	elif int(ch) == 20:
		os.system(" aws ec2 terminate-instances --instance-ids {} ".format(inst_id))
		print()

	elif int(ch) == 21:
		break

	else:
		print(" \tInvalid Input\n ")

	input(" Please press enter to continue... ")


		











		


