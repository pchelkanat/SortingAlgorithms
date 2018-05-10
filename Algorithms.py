import copy
import random

##Простые сортировки

# Сортировка пузырьком
def BubbleSort(arrayToSort):
    array = copy.copy(arrayToSort)

    for i in range(len(array), 0, -1):
        for j in range(1, i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


# Сортировка выбором
def SelectionSort(arrayToSort):
    array = copy.copy(arrayToSort)

    for i in range(len(array)):
        indxMin = i
        for j in range(i + 1, len(array)):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return array


# Сортировка вставками
def InsertionSort(arrayToSort):
    array = copy.copy(arrayToSort)

    for i in range(len(array)):
        tmp = array[i]
        j = i
        while (array[j - 1] > tmp) and (j > 0):
            array[j] = array[j - 1]
            j = j - 1
        array[j] = tmp
    return array


##Сортировка Шелла
def ShellSort(arrayToSort):
    array = copy.copy(arrayToSort)

    tmp = int(len(array) / 2)
    while tmp > 0:
        for i in range(len(array) - tmp):
            j = i
            while j >= 0 and array[j] > array[j + tmp]:
                array[j], array[j + tmp] = array[j + tmp], array[j]
                j -= 1
        tmp = int(tmp / 2)
    return array


##Быстрая сортировка
def QuickSort(arrayToSort, left, right):
    array = copy.copy(arrayToSort)

    if left >= right: return

    l, r = left, right
    pivot = array[random.randint(left, right)]
    while l <= r:
        while array[l] < pivot: l += 1
        while array[r] > pivot: r -= 1
        if l <= r:
            array[l], array[r] = array[r], array[l]
            l, r = l + 1, r - 1
    QuickSort(array, left, r)
    QuickSort(array, l, right)
    return array


def QuickSort2(arrayToSort):
    array = copy.copy(arrayToSort)

    if len(array) <= 1:
        return array
    else:
        q = array[int(len(array)/2)]
    l_nums = [n for n in array if n < q]

    e_nums = [q] * array.count(q)
    b_nums = [n for n in array if n > q]
    return QuickSort2(l_nums) + e_nums + QuickSort2(b_nums)


##Сортировка слиянием
def MergeSort(arrayToSort, ofs=0):
    array = copy.copy(arrayToSort)
    result = []

    if len(array) < 2: return array

    mid = round(len(array) / 2)
    y, z = MergeSort(array[:mid], ofs), MergeSort(array[mid:], mid + ofs)
    i, j = 0, 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    for item in y[i:]:
        result.append(item)
    for item in z[j:]:
        result.append(item)
    return result


##Сортировка кучей
def HeapSort(arrayToSort):
    array = copy.copy(arrayToSort)

    def shiftDown(array, start, end):
        while start * 2 + 1 < end:
            if start * 2 + 1 == end - 1 or array[start * 2 + 1] > array[start * 2 + 2]:
                maxChild = start * 2 + 1
            else:
                maxChild = start * 2 + 2
            if array[start] < array[maxChild]:
                array[start], array[maxChild] = array[maxChild], array[start]
                start = maxChild
            else:
                break

    for start in range(int(len(array) / 2 - 1), -1, -1):
        shiftDown(array, start, len(array))
    for start in range(len(array) - 1, 0, -1):
        array[0], array[start] = array[start], array[0]
        shiftDown(array, 0, start)
    return array


##Поразрядная сортировка
def RadixSort(arrayToSort):
    array = copy.copy(arrayToSort)

    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        buckets = [[] for _ in range(RADIX)]
        for i in array:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append(i)
            if tmp >= 1: maxLength = False
        if maxLength: break
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1
        placement *= RADIX
    return array
