

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def insertionSort(numList):
    for position in range(1, len(numList)):
        for position2 in range(position - 1, 0):
            if numList[position] > numList[position2]:
                swap(numList, numList[position], numList[position2])
    return numList


sorted = insertionSort(list_to_sort)
print('iSort', sorted)

