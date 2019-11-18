import re

letters = []
wordLength = 0
wordLengthDisplay = []
guess = 0
correctLetters = 0
distLetters = "zjqxkvbpgwyfmculdhrsnioate"
underscoreCount = 0
filtered_words = []

def playAIMode():
    #Start guessing Letters
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

    gameOver = False
    #First guess
    while gameOver != True:
        if underscoreCount > 1 and guess < 7:
            getGuess()
            underscoreCount = wordLengthDisplay.count("_")
        elif underscoreCount <= 1 and guess <= 7:
            #Start Guessing Words
            guessedLetters = ''.join(wordLengthDisplay)
            guessedLetters = guessedLetters.replace("_", "")
            filterWords(possibleWords, guessedLetters)
            correct = ''
            while correct != "y":
                word = filtered_words.pop()
                correct = input("Is " + word +" your word? ").lower()
                guess += 1

                if correct == "y":
                    print("Game Over!, Thanks for Playing")
                    underscoreCount = wordLengthDisplay.count("_")
                    gameOver = True




        

def filterWords(possibleWords, guessedLetters):
    #remove unneeded words
    global filtered_words, gameOver
    regex = re.compile(".*".join(guessedLetters), re.IGNORECASE)
    firstFilter = [word for word in possibleWords if regex.search(word)]
    
    for i in range(len(firstFilter)):
        filtered_words.append(firstFilter[i])
        i += 1
    print(filtered_words)

def getGuess():
    #Get a guess from the user
    global wordLengthDisplay, guess, correctLetters

    #Ask the user how many times a letter appears in the word
    letter = letters.pop()
    AIguess = int(input("How many times does " + letter + " occur in your word?"))
    
    #Check if it is in the word or not, if it isn't add one to guess. if it is ask the user where it appears and remove one from AI Guess keep doing this until AIGuess < 1
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
