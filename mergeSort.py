# Merge sorting algorithm
# There are two functions
# The mergeSort function wait the array and cut it to two half
# Send these two arrays to the sorting function 
# This function take the smaller number from these two
# And append to an array and send this array back to the mergeSort function
# It will cut it again
# This will run until the given array is not sorted properly

def sorting(array_left, array_right):
    if (len(array_left) == 0):
        return array_right

    if (len(array_right) == 0):
        return array_left

    returnArray = []
    left_index = 0
    right_index = 0

    while len(returnArray) < len(array_right) + len(array_left):
        if array_left[left_index] <= array_right[right_index]:
            returnArray.append(array_left[left_index])
            left_index += 1
        else:
            returnArray.append(array_right[right_index])
            right_index += 1

        if (right_index == len(array_right)):
            returnArray += array_left[left_index:]
            break

        if (left_index == len(array_left)):
            returnArray += array_right[right_index:]
            break

    return returnArray

def mergeSort(array):
    if len(array) < 2:
        return array

    midpoint = int(len(array) // 2)

    return sorting(mergeSort(array[:midpoint]), mergeSort(array[midpoint:]))

myArray = [83, 6, 23, 56, 12, 74, 11, 21, 54, 123, 42]
print(mergeSort(myArray))