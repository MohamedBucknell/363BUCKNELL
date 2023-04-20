Encryption Ransomware Documentaion
Project for CSCI363

Overview of voldermort.exe
We use the fernet encryption library in python and generate a key which we use to do symmetric encryption
to all the files in the current directory, which was done by traversing through the usage of the os library.
In the code, I made sure not to encrypt the decrypt file, the encrypt file itself, and the key.key file.
Once the user finds out that their precious file is full of hashmat content, they will start sweating and try to
get their files back.
At this point, the genius of the decrypt.exe file comes to life. It will ask for a ransomware password, which 
only me, Mohamed, will provide when I recieve bitcoin. Then, after that, the decrypt.exe file does its magic decrypting the file using the key.key file.

Overview of decrypt.exe
We also use the fernet library and we will go through all the files in the directory that need to be decrypted, and add them in a list but making sure we do not try to decrypt the key or the voldermort.exe file. Once, we do that we will simply use the command: Fermet(secretkey).decrypt(contents). This will bring the encrypted content of each file back to a variable which we will then use to write back to the file.

This cool project could be even more devilish by converting it to a .exe file so that it works even on non python machines, which I did!

Enjoy,

Mohamed

