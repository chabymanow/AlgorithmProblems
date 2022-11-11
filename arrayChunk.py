# This algorithm It expects two parameters, an array and a number.
# It returns with another array that contains as many subarrays as we gave it

def chunk(myArray, amount):
    returnArray = []
    for num in range(0, len(myArray), amount):  
        counter = len(myArray) - num
        if (len(myArray) - num > amount):
            returnArray.append(myArray[num:num + amount])
        else:
            returnArray.append(myArray[num:])         
    return returnArray

testArray = ["John", "Bob", "Jack", "Sylvia", "Samanta", "Julie", "William"]
print("Original array:")
print(testArray)
print("The result is: ")
print(chunk(testArray, 2))
