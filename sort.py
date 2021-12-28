# bubble sort ==>>> compare every element with the next element and swap them if it less than
def BubbleSort(arr):
    isSorted = bool(False)
    for i in range(len(arr) - 1):  # range(stop)
        isSorted = bool(True)
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSorted = bool(False)
        if isSorted:
            break
    return arr


# ############################################################# #

# selectionSort ==>>> let minVal = first val in loop then swap it with the lesser

def SelectionSort(arr):
    for i in range(len(arr) - 1):
        minVal = i
        for j in range(i + 1, len(arr)):  # range(start, length)
            if arr[minVal] > arr[j]:
                arr[minVal], arr[j] = arr[j], arr[minVal]
    return arr


# ############################################################# #

# insertionSort ==>>> compare ele with ele-1 then store it in a temp and if smaller than the previous elements [don't swap them at once] first compare ele-1 with all the next elements and swap if smaller then put ele-1(temp) in ele+1

def InsertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]  # store ele+1 in temp
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]  # compare with the previous elements and swap/replace ele+1(which stored in temp) if smaller
            j -= 1
        arr[j + 1] = temp  # put ele+1 again in the [] after swapping/replacing
    return arr
