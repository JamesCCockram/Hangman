import re

letters = []
wordLength = 0

def playAIMode():
    global wordLength
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
    words = open("wordlist.txt", "r")
    possibleWords = re.findall(r'\b[a-zA-Z]{%s}\b' % wordLength, ' '.join(words))

    #First guess  