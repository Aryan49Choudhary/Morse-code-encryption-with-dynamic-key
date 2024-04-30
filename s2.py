import socket
import random
import string
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to convert plain text to Morse code
def to_morse(text):
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',}
    
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += " "
    
    return morse_code.strip()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

print("Server is listening for connections...")

connection, address = server_socket.accept()
print(f"Connection from {address} has been established.")

# Generate dynamic encryption key
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

# Send plaintext to the server
plain_text = input("Send to client: ")

# Receive plaintext input from client
# plain_text = connection.recv(1024).decode()
# print(f"Received Plaintext from Client: {plain_text}")

# Encrypt plaintext
cipher_text = cipher.encrypt(plain_text.ljust(16).encode())
# Send the encrypted text to the client
connection.send(cipher_text)

# Generate the dynamic key and random Morse code
dynamic_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
morse_code = to_morse(dynamic_key)

# Introduce a 5-second delay before sending the dynamic key and Morse code
time.sleep(5)
# Send the dynamic key and Morse code to the client as separate messages
connection.send(f"Dynamic Key: {dynamic_key}".encode())
connection.send(f"Morse Code: {morse_code}".encode())
print("Sending dynamic key and Morse code...")

# Print changing dynamic keys and Morse codes every second for 5 seconds
for i in range(5):
    time.sleep(1)
    updated_dynamic_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
    updated_morse_code = to_morse(updated_dynamic_key)
    print(f"Updated Dynamic Key: {updated_dynamic_key}")
    print(f"Updated Morse Code: {updated_morse_code}")

# Introduce a 5-second delay before sending the decrypted message
time.sleep(5)
# Decrypt the message
decrypted_text = cipher.decrypt(cipher_text).strip()
# Send the decrypted message, dynamic key, and original Morse code to the client
connection.send(decrypted_text)
connection.send(f"Dynamic Key: {dynamic_key}\n".encode())
connection.send(f"Original Morse Code: {morse_code}".encode())

connection.close()
server_socket.close()
