import time
import subprocess
import optparse
import sys


def main():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change e.g wlan0/eth0") 
    parser.add_option("-m", "--mac", dest="mac", help="MAC to change e.g 00:11:22:33:44:55")
   
    (options, arguments) = parser.parse_args()

    # Assigning the arguments to there unique variables
    interface = options.interface 
    new_mac = options.mac 
    
    animate_text(interface, new_mac) # Just a fancy text thing



def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
    print(f"MAC has been successfuly changed to {new_mac}")

def animate_text(interface, new_mac): # Just a fancy text thing
    # Define the text
    phrases = [
    "changing mac to " + new_mac + "/..",
    "changing mac to " + new_mac + ".\.",
    "changing mac to " + new_mac + "../"
    ]

    #Loops through the sequence twice
    for i in range(2):
        #Loops the the phrases and print each deleting the previous
        for phrase in phrases:
            sys.stdout.write(phrase)
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write('\r' + ' ' * len(phrase) + '\r')  # Clear the previous phrase
            sys.stdout.flush()
    
    change_mac(interface, new_mac)


main() 
