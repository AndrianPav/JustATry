unsortedArray = [0, 2, -1, 0, 55, 1, -4, 555]

def sortArray(tempArray):
    for y in range(len(tempArray)):
        for i in range(len(tempArray) - 1):
            if tempArray[i] > tempArray[i+1]:
                tempArray[i], tempArray[i+1] = tempArray[i+1], tempArray[i]
    sortedArray = tempArray.copy()
    return(sortedArray)

print('Unsorted array: ' + str(unsortedArray))
print('Sorted array: '+ str(sortArray(unsortedArray)))
