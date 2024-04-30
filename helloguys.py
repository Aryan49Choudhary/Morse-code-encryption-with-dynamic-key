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

# Get user input for the plaintext
plain_text = input('Enter the plaintext: ')

# Start time
start_time = time.time()

# Loop to generate dynamic key and random Morse code at every second
while True:
    current_time = time.time() - start_time
    
    if current_time >= 5:
        print(f"Actual Plaintext: {plain_text}")
        print(f"Morse Code: {text_to_morse(plain_text)}")
        break
    else:
        dynamic_key = ''.join(random.choice(string.ascii_uppercase) for _ in range(16))
        print(f"Time: {current_time:.0f} seconds")
        print(f"Dynamic Key: {dynamic_key}")
        print(f"Random Morse Code: {text_to_morse(dynamic_key)}")
    time.sleep(1)
