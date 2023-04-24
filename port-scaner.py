import pyfiglet
import sys
import socket
from datetime import datetime

welcome = pyfiglet.figlet_format("Port Scanner")
print(welcome)

target = input(str("Target IP: "))

print("_" * 50)
print("Scanning Target: "+ target)
print("Scanning started at: "+ str(datetime.now()))
print("_" * 50)

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolver ")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()