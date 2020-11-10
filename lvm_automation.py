import os

print()
os.system(" tput  setaf 1 ")
print(" \t\t\t!!....Welcome to this Automation World....!! ")
os.system(" tput setaf 0 ")
print(" \t\t\t---------------------------------------------- ")

r = input("How do you want to run the program ? ( local or remote )  :    ")

print()

print("Masternode   ------------>  Configured on Local VM")
print("Slavenode   ------------>  Configured on Remote VM")

print()

ip = input("Enter IP address where you want to remote login :  ")

while True:
	os.system("clear")

	print("""

	\tPress 1 :	Create Physical Volumes
	\tPress 2 :       Create Volume Group
	\tPress 3	:	Create LVM Partitions
	\tPress 4	:	Format & Mount the LVM Partitions
	\tPress 5	:	Start Namenode & Datanode
	\tPress 6	:	Check Contribution of Datanode Storage
	\tPress 7	:	Extend the size of LVM Partitions on the Fly
	\tPress 8	:	Again Check Contribution of Datanode Storage
	\tPress 9	:	Remove LVM
	\tPress 10:       Exit the Program
	""")
	print()

	ch = input("Enter Your Choice  :  ")
	print(ch)
	print()

	if int(ch) == 1:
		os.system(' ssh {} fdisk -l  '.format( ip ))
		x = input(' Enter name of disk_1 :   ')
		os.system(' ssh {} pvcreate {}  '.format( ip,x ))
		y = input(' Enter name of disk_2 :   ')
		os.system(' ssh {} pvcreate {}  '.format( ip,y ))
		os.system(' ssh {} pvdisplay {}  '.format( ip,x ))
		os.system(' ssh {} pvdisplay {}  '.format( ip,y ))
		print()

	elif int(ch) == 2:
		m = input(' Enter name of volume group :   ')
		os.system( " ssh {} vgcreate {} {} {} ".format( ip,m,x,y ))
		os.system(' ssh {} vgdisplay {}  '.format( ip,m ))
		os.system(' ssh {} pvdisplay {}'.format( ip,x ))
		os.system(' ssh {} pvdisplay {}  '.format( ip,y ))
		print()

	elif int(ch) == 3:
		n = input(' Enter name of LVM partition:   ')
		p = input(' Enter size of LVM partition:    ')
		os.system(' ssh {} lvcreate --size {}G --name {}  {} '.format( ip,p,n,m ))
		os.system(' ssh {} vgdisplay {}  '.format( ip,m ))
		os.system(' ssh {} lvdisplay {}/{}  '.format( ip,m,n ))
		print()

	elif int(ch) == 4:
		os.system(" ssh {} mkfs.ext4 /dev/{}/{} ".format( ip,m,n ))
		dir = input(' Enter the name of directory to mount with partition :   ')
		os.system(" ssh {}  mkdir {}".format(ip,dir ))
		os.system(" ssh {}  mount /dev/{}/{}  /{}".format( ip,m,n,dir ))
		os.system(" ssh {}  lsblk".format( ip ))
		print()

	elif int(ch) == 5:
		os.system(" systemctl stop firewalld; hadoop-daemon.sh start namenode; jps ")
		os.system(" ssh {} systemctl stop firewalld ".format( ip ))
		os.system(" ssh {} hadoop-daemon.sh start datanode ".format( ip ))
		os.system(" ssh {} jps ".format( ip ))
		print()

	elif int(ch) == 6:
		os.system(" hadoop dfsadmin -report ")
		print()

	elif int(ch) == 7:
		sz_lv = input(" Size of LV you want to increase :   ")
		os.system(' ssh {} lvextend --size +{}G  /dev/{}/{};lvdisplay /dev/{}/{} '.format( ip,sz_lv,m,n,m,n ))
		os.system(" ssh {} resize2fs /dev/{}/{} ".format( ip,m,n ))
		os.system(" hadoop dfsadmin -report ")
		print()

	
	elif int(ch) == 8:
		os.system(" hadoop dfsadmin -report ")
		print()

	elif int(ch) == 9:
		os.system(" ssh {} umount /mk ".format( ip ))                                    #Before unmounting restart your VM
		os.system(" ssh {} lvchange -an /dev/arthvg/lv1 ".format( ip ))
		os.system(" ssh {} lvremove /dev/arthvg/lv1 ".format( ip ))
		os.system(" ssh {} vgchange -an arthvg ".format( ip ))
		os.system(" ssh {} vgremove arthvg ".format( ip ))
		os.system(" ssh {} pvremove /dev/sdb /dev/sdc ".format( ip ))
		os.system(" ssh {} lsblk ".format( ip ))

	elif int(ch) == 10:
		break

		



