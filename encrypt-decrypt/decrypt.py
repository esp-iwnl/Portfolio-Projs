#import os
#from cryptography.fernet import Fernet

files = [] # creates empty list which will store all files in cwd

for file in os.listdir(): # loops through all files in cwd except needed ones and adds them to list above
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "aREADME.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key: # sets the key into a varibale called secretkey
    secretkey = key.read()

for file in files: # loops through the files in the list 
    with open(file, "rb") as thefile: 
        contents = thefile.read() # stores the contents of each file into contents
    contents_decrypted = Fernet(secretkey).decrypt(contents) # decrypts all files within contents using Fernet and sets the key file as the decrypt key
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
