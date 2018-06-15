maven-rpm-test  
[root@slave-pp noarch]# rpm -ihv Hello_World-1.0-1.noarch.rpm  
Preparing...                          ################################# [100%]  
Updating / installing...  
   1:Hello_World-1.0-1                ################################# [100%]  
[root@slave-pp noarch]#  
[root@slave-pp noarch]# systemctl start hello && systemctl status hello  
● hello.service - HelloWorld  
   Loaded: loaded (/etc/systemd/system/hello.service; disabled; vendor preset: disabled)  
   Active: inactive (dead)  

июн 15 23:51:50 slave-pp.localdomain hello_world.sh[25866]: Hello World  
июн 16 00:00:04 slave-pp.localdomain systemd[1]: Started HelloWorld.  
июн 16 00:00:04 slave-pp.localdomain systemd[1]: Starting HelloWorld...  
июн 16 00:00:04 slave-pp.localdomain hello_world.sh[27481]: Hello World  
июн 16 01:53:19 slave-pp.localdomain systemd[1]: Started HelloWorld.  
июн 16 01:53:19 slave-pp.localdomain systemd[1]: Starting HelloWorld..  

