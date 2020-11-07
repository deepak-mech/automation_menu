import os

print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome to this Automation World....!! ")
os.system(" tput setaf 0 ")
print(" \t\t\t---------------------------------------------- ")

print("""

\tPress 0	:	Install Docker
\tPress 1 :       Start Docker Services
\tPress 2	:	Pull Docker Image
\tPress 3	:	Launch Container
\tPress 4	:	Configure Apache Web-Server
\tPress 5	:	Open Web page
\tPress 6	:	Install Python Interpretor
\tPress 7	:	Show Python Code
\tPress 8	:	Run python Code
\tPress 9	:	Exit the Program
""")

while True:
	ch = input("\tEnter Your Choice  :  ")
	print(ch)

	if int(ch) == 0:
		os.system(' yum install docker-ce --nobest ')
		print()

	elif int(ch) == 1:
		os.system( " systemctl stop firewalld ")
		os.system( " systemctl start docker ")
		os.system( " systemctl status docker ")
		print()

	
	elif int(ch) == 2:
		os.system(" docker pull centos ")
		os.system(" docker image ls ")
		print()

	elif int(ch) == 3:
		os.system(" docker run -dit --name myos -p 8080:80 centos ")
		print()

	elif int(ch) == 4:
		os.system(" docker exec -it  myos yum install httpd -y ")
		os.system(" docker exec -it  myos vi lw.html ")
		os.system(" docker exec -it  myos mv lw.html /var/www/html ")
		os.system(" docker exec -it  myos /usr/sbin/httpd ")
		print()

	elif int(ch) == 5:
		os.system("/usr/bin/firefox http://192.168.43.146:8080/lw.html ")
		print()

	elif int(ch) == 6:
		os.system(" docker exec -it  myos yum install python3 ")
		print()

	elif int(ch) == 7:
		os.system(" docker exec -it  myos vi practice.py ")
		os.system(" docker exec -it  myos cat practice.py ")
		print()

	elif int(ch) == 8:
		os.system(" docker exec -it  myos python3 practice.py ")
		print()

	elif int(ch) == 9:
		break


else:
	print(" Not Supported")

