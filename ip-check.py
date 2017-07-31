import sys
from netaddr import *

ip_address = sys.argv[1]
network = sys.argv[2]

if IPAddress(ip_address) in IPNetwork(network):
    print("True")
