#client.py
import socket
import caesarCip


HOST = "127.0.0.1"
PORT = 65432


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_msg = input("msg: ")
input_key = input("key: ")

encrypted_msg = caesarCip.encrypt_caesar_cipher(input_msg, input_key)

try:
    print("Sending message to the server")
    s.sendto(encrypted_msg.encode('utf-8'), (HOST, PORT))

    
    encrypted_data, server_address = s.recvfrom(1024)
    print("Received encrypted data:", repr(encrypted_data))
    
    key = int(input("Enter the Caesar cipher key to decrypt: "))
    decrypted_data = encrypted_data.decode('utf-8')
    decrypted_message = caesarCip.decrypt_caesar_cipher(decrypted_data, key)
    
    print("Decrypted message:", decrypted_message)

finally:
    s.close()


