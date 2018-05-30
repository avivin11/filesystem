import os
from uuid import getnode as get_mac
mac = get_mac()


mac=mac%100
def Decryption(Filename,roll):
	
	fobject=open("/home/avi/down/"+str(roll)+"/"+Filename,"r")
	fobject.read(1)
	Data=fobject.read()
	Data1="";
	for c in Data:
		c=ord(c)-mac
		Data1=Data1+chr(c)
	fobject.close()
	fobject=open("/home/avi/dd/"+Filename,"w")
	
	fobject.write(Data1)
	fobject.close()
	return
	