# Integer sum
# It takes a single integer as input
# And returns the sum of the digits.
# It will return with an error message
# if a non-integer is passed in.

def integerSum(number):
    returnNumber = 0
    if (str(number).isnumeric()):
        for char in str(number):
            returnNumber = returnNumber + int(char)
    else:
        return "This is not a number!"

    return returnNumber

print(integerSum("1232"))