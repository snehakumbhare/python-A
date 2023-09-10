
#Make a regular expression to check the format of IP address
import re
regex="^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def check(Ip):
    if(re.search(regex, Ip)):
        print("Valid Ip adderss")
    else:
        print("Invalid IP address")


IP= "192.168.0.1"
check(IP)

IP="110.234.52.124"
check(IP)

IP="366.1.2.2"
check(IP)
