import socket


HOST = "127.0.0.1"
PORT = 65433


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print("Sending 'Hello World' to the server")
    s.sendto(b'Hello World', (HOST, PORT))
    
    data, server_address = s.recvfrom(1024)
    print("Received", repr(data))

finally:
    s.close()


                   
