import base64
from Crypto.Random import get_random_bytes

# Dynamic key generation function
def generate_dynamic_key():
    # Generate a random key of 32 bytes (AES-256)
    return get_random_bytes(32)

# Main function
def main():
    # Generate dynamic key
    dynamic_key = generate_dynamic_key()

    # Encode the generated dynamic key using Base64
    encoded_key = base64.b64encode(dynamic_key).decode('utf-8')

    # Print the encoded dynamic key
    print("Generated Dynamic Key (Base64 Encoded):", encoded_key)

if __name__ == "__main__":
    main()
