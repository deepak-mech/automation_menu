import os

print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome to this Automation World....!! ")
os.system(" tput setaf 0 ")
print(" \t\t\t---------------------------------------------- ")

print("""

Press 1	:	Show Date
Press 2	:	Show Calender
Press 3	:	Create a New User
Press 4	:	Show RAM Usage
Press 5	:	Clear Cache
Press 6	:	Start Namenode
Press 7	:	Configure Datanode
Press 8	:	Files in Hadoop-Cluster
Press 9	:	Stop Datanode
Press10 :      Exit the Program

""")
r = input("How do you want to run the program ? ( local or remote )  :    ")


def core():
	nn_ip = input(' Enter Name node ip & Hadoop port e.g. hdfs://1.2.3.4:9001 :  ')
	print(nn_ip)	

	os.system(' echo \<configuration\>  >>  core-site.xml ')
	os.system(' echo \<property\>  >>  core-site.xml ')
	os.system(' echo \<name\>fs.default.name\<\/name\>  >>  core-site.xml ')
	os.system(' echo \<value\>{}\<\/value\>  >>  core-site.xml '.format(nn_ip))
	os.system(' echo \<\/property\>  >>  core-site.xml ')
	os.system(' echo \<\/configuration\>  >>  core-site.xml ')
	os.system(' scp core-site.xml {}:/etc/hadoop/core-site.xml '.format(ip))
	os.system(' rm -rf core-site.xml ')


def hdfs():
	dn_dir = input(' Enter directory name for datanode :  ')
	print(dn_dir)	

	os.system(' echo \<configuration\>  >> hdfs-site.xml ')
	os.system(' echo \<property\>  >>  hdfs-site.xml ')
	os.system(' echo \<name\>dfs.data.dir\<\/name\>  >>  hdfs-site.xml ')
	os.system(' echo \<value\>{}\<\/value\>  >>  hdfs-site.xml '.format(dn_dir))
	os.system(' echo \<\/property\>  >>  hdfs-site.xml ')
	os.system(' echo \<\/configuration\>  >>  hdfs-site.xml ')
	os.system(' scp hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml '.format(ip))
	os.system(' rm -rf hdfs-site.xml ')

def data():
	dir = input(' Enter directory name where you have java & hadoop :  ')
	print(dir)

	os.system(' ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm '.format(ip, dir))
	os.system(' ssh {} rpm -i {}\/hadoop-1.2.1-1.x86_64.rpm --force '.format(ip, dir))
	core()
	hdfs()

	os.system(' ssh {} hadoop-daemon.sh start datanode '.format(ip))
	os.system(' ssh {} jps '.format(ip))
	os.system(' ssh {} hadoop dfsadmin -report '.format(ip))



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
			os.system(" useradd dk ")
			os.system(" passwd dk ")

		elif int(ch) == 4:
			os.system(" free -m ")

		elif int(ch) == 5:
			os.system(" echo 3 > /proc/sys/vm/drop_caches ")
			os.system("free -m")

		elif int(ch) == 6:
			os.system(" hadoop-daemon.sh start namenode ")
			os.system(" jps ")

		elif int(ch) == 8:
			os.system(" hadoop fs -ls  / ")

		elif int(ch) == 10:
			break


			

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
			os.system(" ssh {} useradd mj ".format(ip))
			os.system(" ssh {} passwd mj ".format(ip))

		elif int(ch) == 4:
			os.system(" ssh {} free -m ".format(ip))

		elif int(ch) == 5:
			os.system(" ssh {} echo 3 > /proc/sys/vm/drop_caches ".format(ip))
			os.system(" ssh {} free -m".format(ip))


		elif int(ch) == 6:
			os.system(" hadoop-daemon.sh start namenode ")
			os.system(" jps ")

		elif int(ch) == 7:
			data()

		elif int(ch) == 8:
			os.system(" hadoop fs -ls  / ")

		elif int(ch) == 9:
			os.system(" ssh {} hadoop-daemon.sh stop datanode ".format(ip))
			os.system(' ssh {} jps '.format(ip))

		elif int(ch) == 10:
			break


else:
	print(" Not Supported")

	
