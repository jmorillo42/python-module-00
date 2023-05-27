import sys

sys.tracebacklimit = 0


def text_analyzer(text):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    '''
    if not isinstance(text, str):
        raise AssertionError('argument is not a string')

    while not text:
        print('What is the text to analyze?')
        text = input('>> ')
    chars = {'upper': 0, 'lower': 0, 'mark': 0, 'space': 0, }
    for letter in text:
        chars['upper'] += int(letter.isupper())
        chars['lower'] += int(letter.islower())
        chars['mark'] += int(not (letter.isalnum() or letter.isspace()))
        chars['space'] += int(letter.isspace())
    print(f'The text contains {len(text)} character(s):')
    print(f'- {chars["upper"]} upper letter(s)')
    print(f'- {chars["lower"]} lower letter(s)')
    print(f'- {chars["mark"]} punctuation mark(s)')
    print(f'- {chars["space"]} space(s)')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise AssertionError('more than one argument are provided')
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer('')
