import socket
import time
from Crypto.Cipher import AES

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# Receive encrypted text from the server
encrypted_text = client_socket.recv(1024)
print(f"Received encrypted text from server: {encrypted_text}")

# Receive dynamic key and Morse code from the server
dynamic_key = client_socket.recv(1024)
morse_code = client_socket.recv(1024)
print(f"Received dynamic key from server: {dynamic_key}")
print(f"Received Morse code from server: {morse_code}")

print("Decryption and additional details will be received.")

# Receive and print decrypted message, dynamic key, and original Morse code
received = client_socket.recv(1024).decode()
print(f"Received Plaintext from server: {received}")
received = client_socket.recv(1024).decode()
print(f"{received}")
