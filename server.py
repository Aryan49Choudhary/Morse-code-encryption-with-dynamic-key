import socket
import random
import string
import time

# Function to convert plain text to Morse code
def text_to_morse(text):
    morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                      'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                      '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
    
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += " "
    
    return morse_code.strip()

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

print("Server is listening for connections...")

connection, address = server_socket.accept()
print(f"Connection from {address} has been established.")

# Get plaintext input from client
plain_text = connection.recv(1024).decode()
print(f"Received Plaintext from Client: {plain_text}")

# Start time
start_time = time.time()

# Loop to generate dynamic key and random Morse code at every second
while True:
    current_time = time.time() - start_time
    
    if current_time >= 5:
        connection.send(f"Actual Plaintext: {plain_text}\nMorse Code: {text_to_morse(plain_text)}".encode())
        break
    
    else:
        dynamic_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
        connection.send(f"Time: {current_time:.0f} seconds\nDynamic Key: {dynamic_key}\nRandom Morse Code: {text_to_morse(dynamic_key)}\n".encode())
        time.sleep(1)

connection.close()
server_socket.close()
