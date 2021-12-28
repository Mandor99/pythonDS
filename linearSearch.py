# search in every index to find the value index and return it || -1 => o(n)
def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
