#Task 2
"""
Echo server with threading
Create a socket echo server which handles each connection in a separate Thread
"""


import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
PORT = int(sys.argv[2])

server.bind((IP_address, PORT))

server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    conn.send(b"Welcome to this chatroom!")

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + "> " + message.decode())
                message_to_send = "<" + addr[0] + "> " + message.decode()
                broadcast(message_to_send, conn)
            else:
                remove(conn)

        except:
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
        connection.close()

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    threading.Thread(target=clientthread, args=(conn, addr)).start()

server.close()

    
                

    
