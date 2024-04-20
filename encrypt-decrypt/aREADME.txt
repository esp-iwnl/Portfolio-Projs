IMPORTANT:
first two lines in the "encrypt.py" and "decrypt.py" have been commented out for saftey purposes and running either will throw an error.
However by uncommenting these lines the script will run fine.
This script only encrypts the files in the current working directory, therefore I have placed 2 .txt files to view.




This project encrypts all files in the current working directory and creates a new file called "thekey.key" when encrypt.py is ran.
Once ran, all files except the necessary ones (encrypt.py, decrypt.py and thekey.key)are encrypted using Fernet and can only be decrypted with the "thekey.key" key that is generated.
Once "decrypt.py" is ran, all files that were encrypted will be decrypted.


