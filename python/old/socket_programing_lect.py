# Scoket Program

# Within Process
# Between process in same Machine
# Between process in different machine

#Domain
#Type
#Protocal
#host
#Port

# Server Example
# listen
# Bind
# accept

# Client Example
# Accept

# General Example
# Send
# receive
# sendto
# receivefrom
# close
# gethostname
#host=socket.gethostbyname_ex("google.com")
#port=85
#print(host)
#print(s)


# Create scoket connection

import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print(s)
except Exception as ex:
    print(ex)

# GetHostName and local host name
try:
    host="127.0.0.1"
    port=85
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(socket.gethostbyname("www.google.com"))
    print(socket.getfqdn(host))
except Exception as ex:
    print(ex)


