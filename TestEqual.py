from timeit import timeit

from Algorithms import BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort2, MergeSort, HeapSort, RadixSort
from Data import NumDataEq, NumsDataEq, StrsDataEq, DatesDataEq

sortings = reversed(
    [BubbleSort, SelectionSort, InsertionSort, ShellSort, QuickSort2, MergeSort, HeapSort, sorted])  #RadixSort ]
tests = [NumDataEq, NumsDataEq, StrsDataEq, DatesDataEq]

tests_count = 100
sizes = [50, 500, 5000, 50000, 500000]


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


# SORT>>TEST>>SIZE
def testing(size):
    num, nums, strings, dates = NumDataEq(size), NumsDataEq(size), StrsDataEq(size), DatesDataEq(size)
    data = [strings]  # , nums, strings, dates]
    for sort in sortings:
        i = 3
        for test in data:
            print('Preparing {} for {} by {}...'.format(sort.__name__, tests[i].__name__, size))
            sort_test = wrapper(sort, test)
            print('time:', timeit(sort_test, number=tests_count))


#testing(50)
testing(500)
#testing(5000)
#testing(50000)
#testing(500000)
