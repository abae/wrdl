import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

inputFile = open(inputFileName, "r")
inputStrings = inputFile.readlines()
inputFile.close()

outputFile = open(outputFileName, "w")
for word in inputStrings:
    outputFile.write("\t\'" + word.strip() + "\',\n")
outputFile.close()
