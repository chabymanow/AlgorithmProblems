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

print(reverseInt(723419))