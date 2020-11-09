import os
import docker
import lvm
import hadoop
import aws
print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome to this Automation World....!! ")
os.system(" tput setaf 0 ")
print(" \t\t\t---------------------------------------------- ")

print("""
Press 1	 :	Show Date
Press 2	 :	Show Calender
Press 3	 :	Reboot the system
Press 4	 :	Create a New User
Press 5	 :	Show all Hadoop-Cluster Files
Press 6	 :	Show all Files in Root Folder
Press 7	 :	Open Firefox
Press 8  :	To install any program.
Press 9  :  To Launch Docker Menu.
Press 10 :	To Launch LVM Menu.
Press 11 :  To Launch Hadoop Menu.
Press 12 :  To Launch AWS menu.
""")

r = input("How do you want to run the program ? ( local or remote )  :    ")

if r == "local":
	while True:
		print()
		ch = input("Enter Your Choice  :  ")
		print(ch)

		if int(ch) == 1:
			os.system(" date ")

		elif int(ch) == 2:
			os.system(" cal ")

		elif int(ch) == 3:
			os.system(" reboot ")

		elif int(ch) == 4:
			os.system(" useradd dk ")
			os.system(" passwd dk ")

		elif int(ch) == 5:
			os.system(" hadoop fs -ls  / ")

		elif int(ch) == 6:
			os.system(" ls -l ")

		elif int(ch) == 7:
			os.system("firefox")
	
		elif int(ch) == 8:
			y = input("Enter the name of the program you want to instal...")	
			os.system("yum install {}".format(y))

		elif int(ch) == 9:
			docker.docker()

		elif int(ch) == 10:
			lvm.lvm()

		elif int(ch) == 11:
			hadoop.hadoop()

		elif int(ch) == 12:
			aws.aws()

		
elif r == "remote":
	ip = input("Enter IP address where you want to remote login :  ")
	while True:
		ch = input("Enter Your Choice  :  ")
		#print(ch)

		if int(ch) == 1:
			os.system(' ssh {} date '.format(ip))

		elif int(ch) == 2:
			os.system( " ssh {} cal ".format(ip))

		elif int(ch) == 3:
			os.system(" ssh {} reboot ".format(ip))

		elif int(ch) == 4:
			os.system(" ssh {} useradd mk ".format(ip))
			os.system(" ssh {} passwd mk ".format(ip))

		elif int(ch) == 5:
			os.system(" ssh {} hadoop fs -ls  / ".format(ip))

		elif int(ch) == 6:
			os.system(" ssh {} ls -l ".format(ip))
			
		elif int(ch) == 7:
        		os.system(" ssh {} firefox ".format(ip))
		
		elif int(ch) == 8:
				pr = input("Enter the name of the program you wanna install...")
				os.system("ssh {} yum install {}".format(ip,pr ))
		
		elif int(ch) == 9:
				os.system("scp docker.py {}".format(ip))
				os.system("ssh {} python3 docker.py".format(ip))
				os.system("ssh {} rm docker.py -y".format())
		
		elif int(ch) == 10:
				os.system("scp lvm.py {}".format(ip))
				os.system("ssh {} python3 lvm.py".format(ip))
				os.system("ssh {} rm lvm.py".format())
		
		elif int(ch) == 11:
				os.system("scp hadoop.py {}".format(ip))
				os.system("ssh {} python3 hadoop.py".format(ip))
				os.system("ssh {} rm hadoop.py".format(ip))
		elif int(ch) == 12:
				os.system("scp aws.py {}".format(ip))
				os.system("ssh {} python3 aws.py".format(ip))
				os.system("ssh {} rm aws.py".format(ip))

else:
	print(" Not Supported")

	
