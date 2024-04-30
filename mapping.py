import base64
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

# Key generation function
def generate_dynamic_key():
    # Generate a random key of 32 bytes (AES-256)
    return get_random_bytes(32)

# Encrypt function
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Decrypt function
def decrypt_message(key, iv, ct):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

# Main function to perform encryption and decryption
def main():
    message = input("Enter the message to encrypt: ")  # Input message to be encrypted
    print("\nThe message is being encrypted and will be revealed after 5 seconds.")

    start_time = time.time()  # Get the start time
    message_received = False  # Flag to track if the message is received

    while not message_received and time.time() - start_time <= 6:
        # Generate dynamic key
        dynamic_key = generate_dynamic_key()
        print("\nGenerated Dynamic Key:", dynamic_key.hex())

        # Generate a new random message every second
        random_message = "This is a random message at " + str(int(time.time()))  # Example of changing plaintext
        iv, ct = encrypt_message(dynamic_key, random_message)
        
        # Print the dynamic key, ciphertext, and the random message
        print("Dynamic Key:", dynamic_key.hex())
        print("Ciphertext:", ct)
        print("Random Message:", random_message)

        if time.time() - start_time >= 5:
            # Set flag to indicate that the message is being received
            message_received = True
            # Encrypt the original message using the same dynamic key for the final reveal
            iv, ct = encrypt_message(dynamic_key, message)
            print("\nFinal Revealed Message:")
            print("Dynamic Key:", dynamic_key.hex())
            print("Ciphertext:", ct)
            print("Original Message:", message)

        # Pause for 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()
