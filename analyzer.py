'''
LAB 04: Time complexity and Profiling
'''

__author__ = "Carlos Perez-Guzman, Jereme Yang"

from time import time
import stringdata


def linear_search(container, element):
    for i in range(len(container)):
        if container[i] == element:
            return i
    return -1


def binary_search(tuple, element):
    minIndex = 0
    maxIndex = len(tuple) - 1
    midPoint = minIndex + (maxIndex - minIndex) // 2
    while minIndex <= maxIndex:
        if tuple[midPoint] == element:
            return midPoint
        elif tuple[midPoint] < element:
            minIndex = midPoint + 1
            midPoint = minIndex + ((maxIndex - minIndex) // 2)
        elif tuple[midPoint] > element:
            maxIndex = midPoint - 1
            midPoint = minIndex + ((maxIndex - minIndex) // 2)
        else:
            return -1


def main():
    dataset = stringdata.get_data()

    #search for "not_here
    initial_time = time()
    linear_search(dataset, "not_here")
    end_time = time()
    print("Linear search time:", end='')
    print(end_time - initial_time)

    initial_time = time()
    binary_search(dataset, "not_here")
    end_time = time()
    print("Binary search time:", end='')
    print(end_time - initial_time)

    #search for "mzzzz"
    initial_time = time()
    linear_search(dataset, "mzzzz")
    end_time = time()
    print("Linear search time:", end='')
    print(end_time - initial_time)

    initial_time = time()
    binary_search(dataset, "mzzzz")
    end_time = time()
    print("Binary search time:", end='')
    print(end_time - initial_time)

    #search for "aaaaa"
    initial_time = time()
    linear_search(dataset, "aaaaa")
    end_time = time()
    print("Linear search time:", end='')
    print(end_time - initial_time)

    initial_time = time()
    binary_search(dataset, "aaaaa")
    end_time = time()
    print("Binary search time:", end='')
    print(end_time - initial_time)

if __name__ == "__main__":
    main()
