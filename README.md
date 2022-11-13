# Algorithm problems #
---

This is a collection of small ideas. Small algorithms that solve small problems, maybe sometimes can be useful.

**anagrams.py**

It examines two words and decides whether the two words are anagrams of each other or not.
During the analysis, the special characters will be removed and the two words will be converted to lowercase, since for anagram purposes, uppercase and lowercase letters do not matter.

**arrayChunk.py**

This algorithm It expects two parameters, an array and a number. It returns with an array that contains as many subarrays as we gave it

**averageWordLength.py**

It is coming soon.

**charCounter.py**

Char counter in a string. Small algorithm to count characters in a string, write out the most repeated character and how many times is repeated

**reverseInt.py**

Wait an integer and returns the integer with the digits reversed. If the number entered was negative, the number returned will also be negative.

**integerSum.py**

Integer sum
It takes a single integer as input and returns the sum of the digits.
It will return with an error message if a non-integer is passed in.

## Sorting algorithms ##

Examples the different types of sorting algorithms.

**bubbleSort.py**

Bubble sorting algorithm. This is one of the simplest types of sorting algorithms. It wait an unsorted array and returns the sorted version.

The file contains two versions. The first performs the sorting, but even if the resulting array was already sorted.
The second version monitors this and if the array is sorted, it does not deal with it, it just returns it.

**insertionSort.py**

Insertion sort algorithm. Wait an array and start with the second element, compair this element to the previous element and if this element is bigger than the previous, just swap.
Doing this while the current element is bigger then the previous if this element is in the right place, the algorithm take the next element

**mergeSort.py**

Merge sorting algorithm. There are two functions, the mergeSort function wait the array and cut it to two half, send these two arrays to the sorting function. This function take the smaller number from these two and append to an array and send this array back to the mergeSort function andt will cut it again. This will run until the given array is not sorted properly