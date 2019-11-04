import random
import textwrap
import os
import interface
import re
import AI

wordLength = 0
letters = []
wordList = []
theWord = ""
displayWord = []
usedLetters = []
incorrectLetters = []
count = 0
gameOver = False

def randomWord():
    global theWord
    #Select a random word
    index = random.randint(0, len(wordList) - 1)
    theWord = wordList[index]

def drawInterface():
    print(" ".join(displayWord))
    interface.drawBoard(incorrectLetters, theWord)

def getGuess():
    global count
    global usedLetters
    guess = str(input("Guess: ")).lower()

    while True:
        isLetterOK = True
        for i in usedLetters:
            if i == guess:
                isLetterOK = False
        if isLetterOK == False:
            guess = str(input("Looks like you have already guessed that letter!: ")).lower()
        else:
            break

    usedLetters.append(guess)
    found = False

    #Linear Search
    for i in range(len(theWord)):
        if theWord[i] == guess:
            displayWord[i] = guess
            found = True

    if found == False:
        incorrectLetters.append(guess)

def checkWin():
    global gameOver
    count = len(incorrectLetters)
    if count >= 7:
        gameOver = True
        drawInterface()
    elif displayWord == list(theWord):
        print("Correct!")
        gameOver = True

def playAgain():
    global theWord, displayWord, usedLetters, incorrectLetters, count, gameOver
    playAgain = ""
    while playAgain != "y" or playAgain != "n":
        playAgain = input("Do you want to play Again? (Y/N) ")
        if playAgain == "y" or playAgain == "Y":
            #clear lists
            theWord = ""
            displayWord = []
            usedLetters = []
            incorrectLetters = []
            count = 0
            gameOver = False
            #clearScreen
            os.system('cls' if os.name == 'nt' else 'clear')
            #restart game
            randomWord()
            game()
            
        elif playAgain == "n" or playAgain == "N":
            exit()

def game():
    randomWord()
    print(theWord)
    count = len(incorrectLetters)
    #Build the display text
    for i in range(0, len(theWord)):
        displayWord.append("_")
    while True:
        checkWin()
        if gameOver == False:
            drawInterface()
            getGuess()
        else:
            playAgain()







#Start Program
def main():
    try:
        f = open('words.txt', "r")
        line = f.readline()

        while line:
            word = line.strip()
            wordList.append(word)
            line = f.readline()
        f.close()
    except IOError:
        print("Oops!, Something went wrong")
    else:
        choice = ""
        while choice != "q":
            choice = input("Would you like to play (A)I mode or (P)layer mode? ").lower()
            if choice == "a":
                AI.playAIMode()
            elif choice == "p":
                game()
if __name__ == "__main__":
    main()
