import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=password.encode("utf-8"))
        return password
    except:
        print("[--] " + password)
        return

def main():
    zfile = zipfile.ZipFile("testzip.zip")
    passFile = open("passlist.txt")
    for line in passFile.readlines():
        password = line.strip("\n")
        guess = extractFile(zfile, password)
        if guess:
            print("[++] Password = " + password)
            break

main()
