import socket

def Main():
    host='127.0.0.1'
    port=85
    s=socket.socket()
    s.connect((host,port))

    message=input("->")
    while message!='q':
        s.sendall(message.encode('utf-8'))
        message=input("->")
    s.close()


if __name__=='__main__':
    Main()