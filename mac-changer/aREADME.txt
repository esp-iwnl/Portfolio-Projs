This is a MAC address changer that works in kali linux (untested on other OS's). 

This will simply change your current mac address on the interface you decide (wlan0/eth0 etc) to your specified MAC.

An example would be:

python3 main.py --interface wlan0 --mac 00:11:22:33:44:55

The flags are:

Interface = -i or --interface
MAC = -m or --mac
help = -h or --help
