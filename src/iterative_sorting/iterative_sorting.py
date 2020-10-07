# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # set starting index
    # iterate through the array
    for i in range(len(arr)-1):
        # set the index for the next value
        counter = 1
        for j in range(i, len(arr)-1):
            following = i + counter
            if arr[i] > arr[following]:
                arr[i], arr[following] = arr[following], arr[i]
            counter += 1

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # find the length of the array
    n = len(arr)
    # for each element in the length of array...
    for i in range(n-1):
        # traverse through the list
        for j in range(n-i-1):
            # and compare the current value to the next value
            if arr[j] > arr[j+1]:
                # if the next value is greater than the current value
                # switch the two values
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr

'''
STRETCH: implement the Counting Sort function below
Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).
Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 
What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # if it's an empy list
    if len(arr) == 0:
        return arr
    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
    # creates an array of the same length to hold
    # the values of the counts of each occurrence
    counterArray = [0 for value in range(max(arr)+1)]
    # instantiate a blank sorted array
    sortedArray = []
    # count the occurences of each 
    for x in arr:
        counterArray[x] += 1
    for x in range(0, len(counterArray)):
        while counterArray[x] > 0:
            sortedArray.append(x)
            counterArray[x] -=1
    arr = sortedArray
    return arr