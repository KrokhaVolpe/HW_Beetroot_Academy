#server.py
import socket
import caesarCip

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("localhost", 65432)
print("starting up on {} port {}".format(*server_address))
sock.bind(server_address)

while True:
    print("waiting for a connection")
    data, client_address = sock.recvfrom(1024)
    print("connection from", client_address)
    
    try:
        while True:
            data, client_address = sock.recvfrom(1024)
            if not data:
                print("no data from", client_address)
                break

            print("received {!r}".format(data))
            print("sending data back to the client")
            sock.sendto(data.upper(), client_address)

    finally:
        sock.close()
