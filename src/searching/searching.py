def linear_search(arr, target):
    # start at index 0
    index = 0
    # for each value in the array
    for x in arr:
        # compare the value to the target value
        if x == target:
            # if they're the same, return the current index
            return index
        # otherwise, increment the index
        index +=1


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set a low and high pointer
    low = 0
    high = len(arr)-1
    # set up a while loop
    while low <= high:
        # find the middle index
        mid = (low + high) // 2
        # retrieve the value at the middle index
        guess = arr[mid]
        # if our guess is correct...
        if guess == target:
            return mid
        # if our guess is too high...
        if guess > target:
            # set our new high to the current middle minus 1
            high = mid - 1
        # if our guess is too low...
        if guess < target:
            # set our new low to the current middle plus 1
            low = mid + 1



    return -1  # not found