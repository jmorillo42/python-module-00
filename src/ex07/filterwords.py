import sys

try:
    if len(sys.argv) != 3:
        raise ValueError
    min_len = int(sys.argv[2])
except ValueError:
    print('ERROR')
    sys.exit()


def remove_punctuation(text):
    return ''.join(char for char in text if char.isalnum() or char.isspace())


words = [word for word in remove_punctuation(sys.argv[1]).split() if len(word) > min_len]
print(words)
