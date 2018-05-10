from timeit import timeit

import numpy as np

from Algorithms import BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort2, MergeSort, HeapSort, RadixSort
from Data import NumData, NumsData, StrsData, DatesData

sortings = reversed([BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort2, MergeSort, HeapSort, RadixSort, sorted])
tests = [NumData, NumsData, StrsData, DatesData]

tests_count = 100
sizes = [50, 500, 5000, 50000, 500000]


def create (size):
    num, nums, strings, dates = NumData(size), NumsData(size), StrsData(size), DatesData(size)
    num_s, nums_s, strings_s, dates_s = sorted(num), sorted(nums),sorted(strings), sorted(dates)

    return list(reversed(num_s)), list(reversed(nums_s)),list(reversed(strings_s)),list(reversed(dates_s))
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped

def testingreverse(size, array):
    data=[array]
    for sort in sortings:
        i=0
        for test in data:
            print('Preparing {} for {} by {}...'.format(sort.__name__, tests[i].__name__, size))
            sort_test = wrapper(sort, test)
            print('time:', timeit(sort_test, number=tests_count))

num_s, nums_s, strings_s, dates_s = create(500)

testingreverse(50, num_s)
#testingreverse(500)
#testingreverse(5000)
#testingreverse(50000)
#testingreverse(500000)



