import socket 
import threading 
# import ssl 
bind_ip = "0.0.0.0"
bind_port = 9999 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server = ssl.wrap_socket(server, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

server.bind((bind_ip,bind_port))
server.listen(5)

print("server runing on %s:%d" %(bind_ip,bind_port))

def handle_clinet(clinet_socket):
    request = clinet_socket.recv(1024)
    print("[*] Received: %s" % request)
    clinet_socket.send('HTTP/1.1 200 OK\n')
    clinet_socket.send('Content-Type: text/html\n')
    clinet_socket.send('\n') # hea
    f = open("index.html", mode='rb')
    l = f.read(1024)
    while(l):
        clinet_socket.send(l)
        l = f.read(1024)

    clinet_socket.close()


while True:
    clinet,addr = server.accept()

    print("[*] Accpted conntction from: %s:%d" % (addr[0],addr[1]))

    clinet_handler = threading.Thread(target= handle_clinet,args=(clinet,))
    clinet_handler.start()

