from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# AES encryption function
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext)

# AES decryption function
def aes_decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

# Morse code encoding function
def encode_morse_code(text):
    morse_code_dict = {
        'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',  'J': '.---', 
        'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-', 
        'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--', 
        'Z': '--..', ' ': '/',    '1': '.----','2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.', '0': '-----'
    }
    morse_code = ''
    for char in text.upper():
        morse_code += morse_code_dict.get(char, '')
        morse_code += ' '  # Add space between Morse code letters
    return morse_code.strip()  # Remove trailing space

# Morse code decoding function
def decode_morse_code(morse_code):
    morse_code_dict = {
        '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
        '-.-': 'K',  '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
        '..-': 'U',  '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
        '--..': 'Z', '/': ' ', '.----': '1', '..---': '2', '...--': '3', 
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', 
        '---..': '8', '----.': '9', '-----': '0'
    }
    decoded_text = ''
    morse_code_words = morse_code.split('/')
    for word in morse_code_words:
        chars = word.split()
        for char in chars:
            decoded_text += morse_code_dict.get(char, '')
        decoded_text += ' '  # Add space between words
    return decoded_text.strip()  # Remove trailing space

# Main function
def main():
    # Generate dynamic key
    dynamic_key = get_random_bytes(32)
    
    # Example plaintext message
    plaintext = input("Enter the plain text: ")
    
    # Encode plaintext to Morse code
    morse_code = encode_morse_code(plaintext)
    
    # Encrypt Morse code using AES with dynamic key
    ciphertext = aes_encrypt(morse_code, dynamic_key)
    
    # Decrypt ciphertext using AES with dynamic key
    decrypted_morse_code = aes_decrypt(ciphertext, dynamic_key)
    
    # Decode decrypted Morse code to plaintext
    decoded_plaintext = decode_morse_code(decrypted_morse_code)
    
    # Print results
    print("Plaintext:", plaintext)
    print("Morse Code:", morse_code)
    print("Ciphertext (AES encrypted Morse code):", ciphertext)
    print("Decrypted Morse Code:", decrypted_morse_code)
    print("Decoded Plaintext:", decoded_plaintext)

if __name__ == "__main__":
    main()
