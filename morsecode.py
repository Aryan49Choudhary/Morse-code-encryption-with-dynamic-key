# Morse code dictionary
MORSE_CODE = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
  'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '0': '-----', ' ': '/'
}


def text_to_morse(text):
  #Converts text to Morse code.
  return ' '.join(MORSE_CODE.get(char.upper(), '*') for char in text)
# Get user input
text = input("Enter text to convert to Morse code: ")
# Convert text to Morse code
morse_code = text_to_morse(text)
# Print the Morse code
print("Morse code:", morse_code)



