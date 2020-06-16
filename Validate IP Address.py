import re
class Solution:
    def validIPAddress(self, IP: str) -> str:
        result_IPv4 = re.match(r"^([1-9][0-9]{0,2}\.){3}[1-9][0-9]{0,2}$",IP)
        result_IPv6 = re.match(r"^[a-f1-9]([a-f0-9]){0,3}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}$",IP,re.IGNORECASE)
        if result_IPv4 != None and IP[0:3]!='256' and IP[4:7]!='256' and IP[8:11]!='256' and IP[12:15]!='256':
            return("IPv4")
        elif result_IPv6 != None:
            return("IPv6")
        else:
            return("Neither")
