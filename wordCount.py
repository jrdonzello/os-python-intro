import sys
import re

# parameter 1 = input, parameter 2 = output

inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

readFile = inputFile.read()
readFile = re.split(" ", readFile) #split words by whitespace
wordList = {}
count = 0
for current in readFile:
    current = current.lower().strip(",.-")
    if current in wordList:
        wordList[current] += 1
    else:
        wordList[current] = 1
wordList = sorted(wordList.items())
for key, val in wordList:
    outputFile.write(key+" "+str(val)+'\n')
