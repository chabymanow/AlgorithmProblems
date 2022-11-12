# Insertion sort algorithm
# Wait an array and start with the second element
# Compair this element to the previous element 
# And if this element is bigger than the previous, just swap
# Doing this while the current element is bigger then the previous
# If this element is in the right place, the algorithm take the next element

def insertionSort(array):
    for num in range(1, len(array)):
        currentItem = array[num]
        counter = num - 1

        while counter >= 0 and array[counter] > currentItem:
            array[counter + 1] = array[counter]
            counter -= 1
        
        array[counter + 1] = currentItem

    return array

myArray = [3, 6, 23, 56, 12, 74, 11, 21, 54, 123, 42]
print(insertionSort(myArray))