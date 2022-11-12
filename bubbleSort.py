# Simple bubble sort algorithm
# Get an unsorted array and sort it
# Iterate through the given array and sort it
# Get one element and compare to the next element
# If the element is greater than the next element
# Just swap the two element and go to the next
# The problem is, it will go through the array anyway
# Even if is sorted already and this take time 

def bubbleShort(array):
    for x in range(len(array)):
        for y in range(0, len(array) - x - 1):
            if (array[y] > array[y + 1]):
                tempNumber = array[y]
                array[y] = array[y + 1]
                array[y + 1] = tempNumber 

    return array

# The betterBubble check the array
# And if is sorted already, just break the algorithm
# This save time because does not work unnecessarily

def betterBubble(array):
    for x in range(len(array)):
        isSwapped = False
        for y in range(0, len(array) - x - 1):
            if (array[y] > array[y + 1]):
                print("Need to swap! I am workink on it")
                tempNumber = array[y]
                array[y] = array[y + 1]
                array[y + 1] = tempNumber 
                isSwapped = True

        if not isSwapped:
            print("It is sorted. Get some break.")
            break

    return array
myArray = [3, 6, 23, 56, 12, 74, 11, 21, 54, 123, 42]
myArray1 = [3, 6, 11, 12, 21, 23, 42, 54, 56, 74, 123]

print(betterBubble(myArray))