def reverseInt(myNum):
    originalNumber = str(myNum)
    originalNumber = originalNumber.replace("-", "") 
    newNum = ""
    for char in range(len(originalNumber)-1, -1, -1): 
        newNum = newNum + originalNumber[char]
    returnNum = int(newNum)
    if (int(myNum) < 0):
        returnNum = returnNum * -1

    return returnNum

def betterReverse(myNum):
    num = str(myNum)

    if num[0] == "-":
        return int("-" + num[:0:-1])
    else:
        return int(num[::-1])

print(reverseInt(-723419))
print(betterReverse(-723419))