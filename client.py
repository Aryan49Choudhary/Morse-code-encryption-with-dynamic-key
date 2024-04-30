import socket

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# Get plaintext input from the user
plain_text = input("Enter the plaintext to send to the server: ")
client_socket.send(plain_text.encode())

# Receive and print the response from the server
while True:
    response = client_socket.recv(1024).decode()
    
    if "Actual Plaintext" in response:
        print(response)
        break
    
    print(response)

client_socket.close()
