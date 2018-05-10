from datetime import datetime
from random import randint


def NumData(size):
    array = []
    for i in range(size):
        array.append(randint(0, 9))
    return array


def NumsData(size):
    array = []
    for i in range(size):
        array.append(randint(-10000, 10000))
    return array


def StrsData(size):
    array = []
    for i in range(size):
        array.append('')
        for j in range(randint(1, 9)):
            array[i] += chr(randint(48, 122)) #основная Латиница от 0 до z
    return array


def DatesData(size):
    array = []
    for i in range(size):
        year = randint(1700, 2100)
        month = randint(1, 12)
        day = randint(1, 28)
        date = datetime(year, month, day)
        array.append(date)
    return array

def NumDataEq(size):
    array = []
    for i in range(size):
        array.append(5)
    return array


def NumsDataEq(size):
    array = []
    for i in range(size):
        array.append(5000)
    return array


def StrsDataEq(size):
    array = []
    for i in range(size):
        array.append('algorithm')
    return array

def DatesDataEq(size):
    array = []
    for i in range(size):
        date = datetime(2004, 12, 31)
        array.append(date)
    return array
