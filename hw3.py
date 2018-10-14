"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""
from heapq import heappush, heappop


def matrix_multiply(arr0, arr1):

    # if neither arr0 nor arr1 are 1D arrays

    if len(arr0) == 0 or len(arr1) == 0:
        return None
        if not isinstance(arr0[0], list) and isinstance(arr1[0], list):
            return None
    else:
        arr0Rows = len(arr0)
        arr0Cols = len(arr0[0])
        arr1Rows = len(arr1)
        arr1Cols = len(arr1[0])
        if not arr0Rows == arr1Cols and not arr0Cols == arr1Rows:
            return None
        if arr0Cols == arr1Rows and not arr0Rows == arr1Cols:
            returnArray = [[0 for fillin in range(0, arr0Cols)]
                           for fillout in range(0, arr1Rows)]
            for arr1i in range(0, arr1Rows):
                for arr1jy in range(0, arr0Cols):  # equal to arr1Rows
                    for arr1jx in range(0, arr0Rows):
                        returnArray[arr1i][arr1jy] += \
                            arr1[arr1i][arr1jx] * arr0[arr1jx][arr1jy]
        returnArray = [[0 for fillin in range(0, arr1Cols)]
                       for fillout in range(0, arr0Rows)]
        for arr0i in range(0, arr0Rows):
            for arr0jy in range(0, arr1Cols):  # equal to arr1Rows
                for arr0jx in range(0, arr1Rows):
                    returnArray[arr0i][arr0jy] += arr0[arr0i][arr0jx] \
                        * arr1[arr0jx][arr0jy]
        return returnArray


def sortArray(arr):
    arrayHeap = []
    endArray = []
    for value in arr:
        heappush(arrayHeap, value)
    while arrayHeap:
        endArray.append(heappop(arrayHeap))
    return endArray


# complete

def nth_largest_element(arr, n):
    if len(arr) == 0:
        return 0
    if n <= 0:
        return 0
    arrayHeap = []
    endArray = []
    for value in arr:
        heappush(arrayHeap, value)
    while arrayHeap:
        endArray.append(heappop(arrayHeap))  # for i in range(len(arrayHeap)))
    length = len(endArray)
    return endArray[length - n]


# complete

def reverse_block(arr, n):
    returnArray = []
    if n > len(arr):
        for i in range(0, len(arr)):
            returnArray.append(arr[len(arr) - 1 - i])
        return returnArray
    if n <= 1:
        return arr
    numOfBlocks = len(arr) / n
    lastIndex = 0
    times = 0
    while times < numOfBlocks:
        index = range(lastIndex, lastIndex + n)
        for i in range(0, n):
            returnArray.append(arr[index[len(index) - i - 1]])
        times += 1
        lastIndex += n
    leftover = len(arr) % n
    if leftover != 0:
        index = 0
        while index < leftover:
            returnArray.append(arr[len(arr) - index - 1])
            index += 1
        return returnArray


def subset_sum(arr, target):
    if target == 0:
        return True
    if len(arr) == 0:
        return False
    if target in arr:
        return True
    return subsetRecursion(arr, len(arr), target)


def subsetRecursion(arr, length, target):
    if target == 0:
        return True
    if length == 0 and target != 0:
        return False
    if arr[length - 1] > target:
        return subsetRecursion(arr, length - 1, target)
    return subsetRecursion(arr, length - 1, target) \
        or subsetRecursion(arr, length - 1, target - arr[length - 1])


# complete

def spiral_matrix(arr):
    if not isinstance(arr[0], list):
        return None
    startRow = 0
    startCol = len(arr[0]) - 1
    returnArray = []
    RALength = len(arr) * len(arr[0])
    while len(returnArray) < RALength:
        for i in range(0, len(arr[0])):
            returnArray.append(arr[0][i])
        del arr[0]
        if len(returnArray) == RALength:
            break

        for i in range(0, len(arr)):
            returnArray.append(arr[i][len(arr[i]) - 1])
            del arr[i][len(arr[i]) - 1]
        if len(returnArray) == RALength:
            break

        for i in range(0, len(arr[0])):
            returnArray.append(arr[len(arr) - 1][len(arr[0]) - 1 - i])
        del arr[len(arr) - 1]
        if len(returnArray) == RALength:
            break

        for i in range(0, len(arr)):
            returnArray.append(arr[len(arr) - 1 - i][0])
            del arr[len(arr) - 1 - i][0]
        if len(returnArray) == RALength:
            break
    return returnArray
