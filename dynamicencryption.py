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
    while True:
        # Generate dynamic key
        dynamic_key = generate_dynamic_key()
        print("Generated Dynamic Key:", dynamic_key.hex())

        # Input message to be encrypted
        message = input("Enter the message to encrypt: ")

        # Encrypt the message using the dynamic key
        iv, ct = encrypt_message(dynamic_key, message)
        print("Message encrypted.")

        # Simulate second terminal receiving the IV and ciphertext for decryption
        print("\nSimulating Second Terminal (Receiving IV and Ciphertext):")
        print("IV:", iv)
        print("Ciphertext:", ct)

        # Decrypt the message using the dynamic key
        decrypted_message = decrypt_message(dynamic_key, iv, ct)
        print("\nDecrypted Message:", decrypted_message)

        # Pause for 0.1 seconds
        time.sleep(0.1)

if __name__ == "__main__":
    main()
