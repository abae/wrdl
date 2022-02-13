import sys

#initialize variables
wordSize = 5
dictionaryFileName = sys.argv[1]
wrdlOutputFileName = sys.argv[2]
mapOutputFileName = sys.argv[3]

#get arg file contents
f = open(dictionaryFileName, "r")
dictionaryString = f.read()
f.close()

#remove json formatting
dictionary = dictionaryString.split("\"},{\"word\":\"")
dictionary[0] = dictionary[0][10:]
dictionary[-1] = dictionary[-1][:-3]

#build wrdl dictionary
trueDictionary = []
wrdlDictionary = []
for i in range(len(dictionary)):
    wrdlEntry = dictionary[i]
    wrdlEntry = wrdlEntry.replace("a", "")
    wrdlEntry = wrdlEntry.replace("e", "")
    wrdlEntry = wrdlEntry.replace("i", "")
    wrdlEntry = wrdlEntry.replace("o", "")
    wrdlEntry = wrdlEntry.replace("u", "")
    wrdlEntry = wrdlEntry.replace("y", "")
    if(len(wrdlEntry) == 5):
        trueDictionary.append(dictionary[i])
        wrdlDictionary.append(wrdlEntry)

#output wrdl dictionary
wrdlFile = open(wrdlOutputFileName, "w")
for word in wrdlDictionary:
    wrdlFile.write("\t\'"+word+"\',\n")
wrdlFile.close()

#output mapping
outFile = open(mapOutputFileName, "w")
for i in range(len(trueDictionary)):
    outFile.write(trueDictionary[i] + ":" + wrdlDictionary[i] + "\n")
outFile.close()

print(wrdlDictionary)
print("success")
