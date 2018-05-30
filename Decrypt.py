import os

def Decrypt(Filename,roll):
	
	fobject=open("/home/avi/down/"+str(roll)+"/"+Filename,"r")
	mac1=fobject.read(1)
	mac=ord(mac1)
	Data=fobject.read()
	Data1="";
	for c in Data:
		c=ord(c)-mac
		Data1=Data1+chr(c)
	fobject.close()

	fobject=open("/home/avi/ds/"+str(roll)+"/"+Filename,"w")
	
	fobject.write(Data1)
	fobject.close()
	return
	