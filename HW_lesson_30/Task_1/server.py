#Task 1
"""
During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets.
In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication.
"""

import socket

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print("Connected by", addr)


while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
