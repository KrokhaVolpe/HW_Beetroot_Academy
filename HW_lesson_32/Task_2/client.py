import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
PORT = int(sys.argv[2])

server.connect((IP_address, PORT))

while True:
    message = input("Your message: ")
    server.sendall(message.encode())
    data = server.recv(2048)
    print("Received:", data.decode())

server.close()
