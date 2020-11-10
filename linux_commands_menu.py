import os

print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome to this Automation World....!! ")
os.system(" tput setaf 0 ")
print(" \t\t\t---------------------------------------------- ")

print("""
Press 1	:	Show Date
Press 2	:	Show Calender
Press 3	:	Reboot the system
Press 4	:	Create a New User
Press 5	:	Show all Hadoop-Cluster Files
Press 6	:	Show all Files in Root Folder
Press 7	:	Open Firefox
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
			
		elif int(ch)==3:
        		os.system(" firefox ")

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

else:
	print(" Not Supported")

	
