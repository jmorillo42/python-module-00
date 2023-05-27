import sys

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', ' ': '/'}
if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        text = ' '.join(sys.argv[1:])
    else:
        text = sys.argv[1]
    morse_codes = []
    for letter in text:
        if letter.upper() in morse:
            morse_codes.append(morse[letter.upper()])
        else:
            morse_codes = ['ERROR']
            break
    print(' '.join(morse_codes))
