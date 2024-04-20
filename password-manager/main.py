import json
import pyfiglet
from cryptography.fernet import Fernet
import os
import sys

ascii_banner = pyfiglet.figlet_format("Password Manager") # Applys the header text
print(ascii_banner)

def main():
    #encrypt_password_file()   #######################
   
    print("Select Option:")
    print("a: Add Password")
    print("s: Show Passwords")
    print("q: Quit")

    user_main_input = input(">> ").lower()
    
    if user_main_input == "a":
        add_new_password()

    if user_main_input == "s":
        show_passwords()
    
    if user_main_input == "q":
        encrypt_password_file()


def add_new_password():
    try:
        with open("passwd.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    name_for_password = input("Enter website/application name >> ")
    password_for_password = input("Enter password >> ")
    
    new_entry = {"name": name_for_password, "password": password_for_password}
    data.append(new_entry)

    with open("passwd.json", "w") as file:
        json.dump(data, file, indent=4)
    
    main()

def encrypt_password_file():
    # This block assigns the passwd.json file to the list to be encrypted later
    encrypt_file = []
    for file in os.listdir():
        if file == "passwd.json":
            encrypt_file.append(file)

    key = Fernet.generate_key() # Generates the key and stores in key variable
    
    with open("key.key", "wb") as thekey:
        thekey.write(key) # Writes the key to a file named "key.key"
    
    for file in encrypt_file:
        with open(file, "rb") as thefile:
            contents = thefile.read() # Stores the contents of the password file
        contents_encrypted = Fernet(key).encrypt(contents) # Encrypts the data of the file
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted) # Writes the encrypted contents back to the password file

    sys.exit()


def decrypt_password_file():
    files = [] 
    
    for file in os.listdir():       
        if file == "passwd.json":
            files.append(file)
    
    with open("key.key", "rb") as key:
        secretkey = key.read()
    
    for file in files: # loops through the files in the list 
        with open(file, "rb") as thefile: 
            contents = thefile.read() # stores the contents of each file into contents
        contents_decrypted = Fernet(secretkey).decrypt(contents) # decrypts all files within contents using Fernet and sets the key file as the decrypt key
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    main()

def show_passwords():
   with open("passwd.json", "r") as file:
        data = json.load(file)

        for entry in data:
            name = entry["name"]
            password = entry["password"]
            print(f"{name}: {password}")
            print("\n")
   main()

while True:
    pw = "admin"
    user_pw_input = input("Password > ")
    
    if user_pw_input == pw:
        decrypt_password_file()
        main()
    else:
        print("Incorrect Password, Try Again!")






