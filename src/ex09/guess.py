import random
import sys

print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
''')

number = random.randint(1, 99)
guess = 0
counter = 0
while guess != number:
    print('What\'s your guess between 1 and 99?')
    guess = input('>> ').strip().lower()
    counter += 1
    if guess == 'exit':
        print('Goodbye!')
        sys.exit()
    try:
        guess = int(guess)
    except ValueError:
        print('That\'s not a number.')
        continue
    if guess > number:
        print('Too high!')
    elif guess < number:
        print('Too low!')
if guess == 42:
    print('The answer to the ultimate question of life, the universe and everything is 42.')
if counter == 1:
    print('Congratulations! You got it on your first try!')
else:
    print(f'Congratulations, you\'ve got it!\nYou won in {counter} attempts!')
