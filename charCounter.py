# Small algorithm to count characters in a string
# Write out the most repeated character
# and how many times is repeated

import re

def charCounter(string_1):
    string_1 = re.sub(r"[^a-zA-Z0-9]","",string_1)
    chars = {}
    counter = 0
    biggestNumber = 0
    biggestChar = ""
    for char in string_1:
        if (char in chars):
            counter = chars[char]
            counter += 1
            chars[char] = counter
            if (counter > biggestNumber):
                biggestNumber = counter
                biggestChar = char
        else:
            chars[char] = 1
    return biggestChar, biggestNumber, chars

testString = charCounter(":/myPhyton/AlgorithmProblems/charCounter.py")
for char in testString[2]:
    print(char + " : " + str(testString[2][char]))
print("The most repeated character is: " + testString[0])
print("Repeated " + str(testString[1]) +" times")