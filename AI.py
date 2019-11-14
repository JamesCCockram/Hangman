import re

letters = []
wordLength = 0
wordLengthDisplay = []
guess = 0
correctLetters = 0
distLetters = "zjqxkvbpgwyfmculdhrsnioate"
underscoreCount = 0

def playAIMode():
    global wordLength, wordLengthDisplay, guess, distLetters

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
    underscoreCount = wordLengthDisplay.count("_")

    #Get Words
    words = open("words.txt", "r")
    possibleWords = re.findall(r'\b[a-zA-Z]{%s}\b' % wordLength, ' '.join(words))
    possibleWords = list(dict.fromkeys(possibleWords))

    #First guess
    while underscoreCount > 2 and guess < 7:
        getGuess()
        underscoreCount = wordLengthDisplay.count("_")
    while underscoreCount <= 1 and guess <= 7:
        #Start Guessing Words
        guessedLetters = ''.join(wordLengthDisplay)
        guessedLetters = guessedLetters.replace("_", "")
        filterWords(possibleWords, guessedLetters)
        input("")

        

def filterWords(possibleWords, guessedLetters):
    regex = re.compile(".*".join(guessedLetters), re.IGNORECASE)
    filtered_words = [word for word in possibleWords if regex.search(word)]
    print(filtered_words)

def getGuess():
    global wordLengthDisplay, guess, correctLetters

    letter = letters.pop()
    AIguess = int(input("How many times does " + letter + " occur in your word?"))
    
    if AIguess == 0:
        guess += 1
    else:
        while AIguess >= 1:
            position = (int(input("What Position does " + letter + " occur?")) - 1)
            wordLengthDisplay[position] = letter
            AIguess -= 1
            correctLetters += 1
            print(correctLetters)
            print(wordLengthDisplay)
            print("Correct: ", correctLetters)
