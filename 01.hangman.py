import sys

num_of_tries = 5
word = 'Enter'.upper()
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print('Good Letters: ', user_word)
    print('Attempts remain: ', num_of_tries)
    print('Letters used: ', used_letters)
    print()
# 
for _ in word:
    user_word.append('_')

while True:
    letter = input('Enter the letter: ').upper()
    used_letters.append(letter)
    foundIndexes = find_indexes(word, letter)
    if len(foundIndexes) == 0:
        print('No letter in the word!')
        num_of_tries -= 1
    # Game Over
        if num_of_tries == 0:
            print('Game Over! :(')
            sys.exit(0)
    else: 
        for index in foundIndexes:
            user_word[index] = letter
        if ''.join(user_word) == word:
            print('Well done! You win the game!')
            sys.exit(0)
    
    show_state_of_game()
