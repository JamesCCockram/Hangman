import re

letters = []
wordLength = 0
wordLengthDisplay = []

def playAIMode():
    global wordLength
    global wordLengthDisplay
    guess = 0
    wordLengthDisplay = []
    distLetters = "zjqxkvbpgwyfmculdhrsnioate"


    for c in range(len(distLetters)):
      letters.append(distLetters[c])

    while wordLength == 0:
        try:
            wordLength = int(input("How many letters"))
        except:
            print("Invalid!")
            wordLength = 0
    
    #Draw Board
    for i in range(0, wordLength):
        wordLengthDisplay.append("_")
    print(wordLengthDisplay)
    #Get Words
    words = open("words.txt", "r")
    possibleWords = re.findall(r'\b[a-zA-Z]{%s}\b' % wordLength, ' '.join(words))

    #First guess
    while guess < 7:
        getGuess()
        guess += 1


def getGuess():
    global wordLengthDisplay
    letter = letters.pop()
    AIguess = int(input("How many times does " + letter + " occur in your word?"))
    
    while AIguess > 0:
        position = (int(input("What Position does " + letter + " occur?")) - 1)
        wordLengthDisplay[position] = letter
        AIguess -= 1
        print(wordLengthDisplay)