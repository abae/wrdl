import random

#initialize variables
possibleDictionaryFileName = "dictionaryMap/possibleDictionaryMap.txt"
answerDictionaryFileName = "dictionaryMap/answerDictionaryMap.txt"
trueAnswerDictionaryFileName = "dictionaryMap/trueAnswerDictionaryMap.txt"

#get file
possibleDictionaryFile = open(possibleDictionaryFileName, "r")
possibleDictionary = []
for line in possibleDictionaryFile:
    possibleDictionary.append(line.strip()) 
possibleDictionaryFile.close()

answerDictionary = []
trueAnswerDictionary = []

#main loop to get choices
keepGoing = True
while keepGoing:
    randNum = random.randint(0,len(possibleDictionary)-1)
    selectedWord = possibleDictionary.pop(randNum)
    selectedWord = selectedWord.split(":")
    
    noValidInput = True
    #custom autoignorer
    if(selectedWord[0][-1] == 's'):
        noValidInput = False
    if(selectedWord[0][0] == 'a'):
        noValidInput = False
    if(selectedWord[0][0] == 'e'):
        if(selectedWord[0][1] != 'x'):
            noValidInput = False
    if(selectedWord[0][0] == 'i'):
        noValidInput = False
    if(selectedWord[0][0] == 'o'):
        noValidInput = False
    if(selectedWord[0][0] == 'u'):
        noValidInput = False
    if(selectedWord[0][0] == 'y'):
        noValidInput = False
    if(selectedWord[0].endswith('ing')):
        noValidInput = False
    if(selectedWord[0].endswith('est')):
        noValidInput = False

    while noValidInput:
        userInput = input("Should I keep " + selectedWord[0] + "?:")
        if userInput == "y":
            answerDictionary.append(selectedWord[1])
            trueAnswerDictionary.append(selectedWord[0])
            noValidInput = False
        if userInput == "n":
            noValidInput = False
        if userInput == "nq":
            noValidInput = False
            keepGoing = False

#save file
possibleDictionaryFile = open(possibleDictionaryFileName, "w")
for entry in possibleDictionary:
    possibleDictionaryFile.write(entry.strip() + "\n")
possibleDictionaryFile.close()

answerDictionaryFile = open(answerDictionaryFileName, "a")
for entry in answerDictionary:
    answerDictionaryFile.write("\t\'" + entry.strip() + "\',\n")
answerDictionaryFile.close()

trueAnswerDictionaryFile = open(trueAnswerDictionaryFileName, "a")
for entry in trueAnswerDictionary:
    trueAnswerDictionaryFile.write(entry.strip() + "\n")
trueAnswerDictionaryFile.close()

