import sys

numOfTries = 5
word = 'Enter'.upper()
usedLetters = []
userWord = []

def findIndexes(word, letter):
    indexes = []
    for index, letterInWord in enumerate(word):
        if letter == letterInWord:
            indexes.append(index)
    return indexes

def showStateOfGame():
    print()
    print('Good Letters: ', userWord)
    print('Attempts remain: ', numOfTries)
    print('Letters used: ', usedLetters)
    print()
# 
for _ in word:
    userWord.append('_')

while True:
    letter = input('Enter the letter: ').upper()
    usedLetters.append(letter)
    foundIndexes = findIndexes(word, letter)
    if len(foundIndexes) == 0:
        print('No letter in the word!')
        numOfTries -= 1
    # Game Over
        if numOfTries == 0:
            print('Game Over! :(')
            sys.exit(0)
    else: 
        for index in foundIndexes:
            userWord[index] = letter
        if ''.join(userWord) == word:
            print('Well done! You win the game!')
            sys.exit(0)
    
    showStateOfGame()