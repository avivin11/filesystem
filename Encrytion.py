from uuid import getnode as get_mac
import os

mac = get_mac()

mac= mac%100
import os

def Encryption(Filename,roll):
	
	fobject=open("/home/avi/testing/"+Filename,"r");
	Data=fobject.read();
	Data1="";
	for c in Data:
		c=ord(c)+mac
		Data1=Data1+chr(c);	

	
	fobject=open("/home/avi/down/"+str(roll)+"/"+Filename,"w");
	fobject.write(chr(mac));
	fobject.write(Data1);
	fobject.close();
	return;


